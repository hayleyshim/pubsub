#subscriber.py
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://127.0.0.1:2000')
socket.setsockopt(zmq.SUBSCRIBE,b'')

listener = 0

while(True):
    message = socket.recv_pyobj()
    if(message.get(listener) != None):
       print(message.get(listener))