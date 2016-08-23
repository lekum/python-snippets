from queue import Queue
from threading import Thread

def producer(out_q):
    for i in range(10):
        out_q.put(i)
    out_q.put("end")

def consumer(in_q):
    while True:
        data = in_q.get()
        if data == "end":
            return
        print("I got {}".format(data))

if __name__ == "__main__":
    q = Queue()
    t1 = Thread(target=consumer, args=(q,))
    t2 = Thread(target=producer, args=(q,))
    t1.start()
    t2.start()
    t2.join()
    t1.join()
