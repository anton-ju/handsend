import socketserver
from hhparser import HHParser


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(10240).decode(encoding='utf-8')
        print("{} wrote:".format(self.client_address[0]))
        # just send back the same data, but upper-cased
        hh = HHParser(self.data)
        request = bytes(' - '.join([hh.tid, str(hh.datetime)]), encoding='utf-8')
        self.request.sendall(request)


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
