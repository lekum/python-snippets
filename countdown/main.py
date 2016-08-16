import time
import random
from threading import Thread

class CountdownTask:

    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('->', n)
            n -= 1
            time.sleep(1)

if __name__ == "__main__":
    c = CountdownTask()
    t = Thread(target=c.run, args=(10,))
    t.start()
    time.sleep(random.randrange(10))
    c.terminate()
    t.join()
