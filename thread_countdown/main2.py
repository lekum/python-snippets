import time
from threading import Thread

class CountdownThread(Thread):

    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        while self.n > 0:
            print('->', self.n)
            self.n -= 1
            time.sleep(1)

if __name__ == "__main__":

    t = CountdownThread(5)
    t.start()
    t.join()
