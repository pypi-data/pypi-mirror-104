import zmq.green as zmq
from gevent.queue import Queue
from gevent_fsm.fsm import FSMController, Channel, NullChannel
from .messages import msg_types
import gevent
import yaml
from . import server_fsm


class ZMQServerChannel(object):

    def __init__(self, outbox, tracer):
        self.tracer = tracer
        self.buffered_messages = Queue()
        self.outbox = outbox
        self.context = zmq.Context.instance()
        self.socket = self.context.socket(zmq.ROUTER)
        self.socket.bind('tcp://127.0.0.1:5555')
        self.controller = FSMController(self,
                                        "server_fsm",
                                        1,
                                        server_fsm.Start,
                                        self.tracer,
                                        self.tracer)
        self.controller.outboxes['default'] = Channel(self.controller,
                                                      self.controller,
                                                      self.tracer,
                                                      self.buffered_messages)
        self.controller.outboxes['output'] = NullChannel(self.controller, self)
        self.queue = self.controller.inboxes['default']

        self.zmq_thread = gevent.spawn(self.receive_messages)
        self.controller_thread = gevent.spawn(self.controller.receive_messages)

    def receive_messages(self):
        while True:
            message = self.socket.recv_multipart()
            id = message.pop(0)
            msg_type = message.pop(0).decode()
            msg_data = yaml.safe_load(message.pop(0).decode())
            print(id, msg_type, msg_data)
            msg_data['client_id'] = id
            print(msg_types[msg_type](**msg_data))
            self.queue.put(msg_types[msg_type](**msg_data))
            self.socket.send_multipart([id, b'Submitted'])
