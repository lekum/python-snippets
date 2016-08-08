import hmac
from socket import socket, AF_INET, SOCK_STREAM

def handler(connection, secret):
    message = connection.recv(512)
    print("Received:", message.decode())
    hash = hmac.new(secret, message)
    digest = hash.digest()
    connection.send(digest)
    connection.close()

if __name__ == "__main__":

    secret_key = b'mysecret'
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', 18000))
    s.listen(5)
    while True:
        c, a = s.accept()
        handler(c, secret_key)
