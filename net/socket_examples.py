import socket
s = socket.socket()
s.bind(('', 64444))
s.listen(5)
c1, a = s.accept()
c1.recv(50)
c1.sendall(b'data')

import socket
c = socket.socket()
c.connect(('192.168.1.159', 64444))
c.recv(50)
c.sendall(b'data')

data = 'čeština'.encode('utf-8')
string = data.decode('utf-8')

import struct
data = struct.pack('!I', length)
length, = struct.unpack('!I', data)

import pickle
data = pickle.dumps(test)
test = pickle.loads(data)

import threading