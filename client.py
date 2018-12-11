import socket
import sys
from hand_storage import HandStorage
from hhparser import HHParser
from pprint import pprint

fn = 'hh_example.txt'

with open(fn, 'r') as f:
    data = f.read()


HOST, PORT = "localhost", 9999
# data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data, encoding='utf-8'))

    # Receive data from the server and shut down
    received = sock.recv(10240)

pprint("Sent:     {}".format(data))
pprint("Received: {}".format(received))
