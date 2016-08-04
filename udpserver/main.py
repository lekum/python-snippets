from socketserver import BaseRequestHandler, ThreadingUDPServer
import time

class TimeHandler(BaseRequestHandler):

    def handle(self):
        print('Got connection from', self.client_address)
        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode(), self.client_address)

if __name__ == '__main__':

    serv = ThreadingUDPServer(('', 20000), TimeHandler)
    serv.serve_forever()
