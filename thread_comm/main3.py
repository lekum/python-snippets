import logging
import time
from queue import Queue, Full
from threading import Thread

_sentinel = object()
log = logging.getLogger()

def producer(out_q):
    for i in range(10):
        #time.sleep(0.0001)
        try:
            out_q.put(i, block=False)
        except Full:
            log.warning('Queue item %r discarded!', i)
    out_q.put(_sentinel)

def consumer(in_q):
    while True:
        data = in_q.get()
        if data is _sentinel:
            break
        print("I got {}".format(data))

if __name__ == "__main__":
    q = Queue(2)
    t1 = Thread(target=consumer, args=(q,))
    t2 = Thread(target=producer, args=(q,))
    t1.start()
    t2.start()
    t2.join()
    t1.join()
