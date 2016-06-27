import sys
from socketserver import BaseRequestHandler, ThreadingTCPServer

class EchoHandler(BaseRequestHandler):

    def handle(self):
        print("Got connection from", self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            print("Replying:", msg)
            self.request.send(msg)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python main.py port")
        sys.exit(1)
    port = int(sys.argv[1])
    try:
        serv = ThreadingTCPServer(('', port), EchoHandler)
        serv.serve_forever()
    except KeyboardInterrupt:
        serv.shutdown()
        serv.server_close()
