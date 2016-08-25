from queue import Queue
from threading import Thread, Event

def producer(out_q):
    for i in range(10):
        evt = Event()
        out_q.put((i, evt))
        print("Sent {}".format(i))
        # Wait for the consumer to process the item
        evt.wait()
        print("ACK, carrying on")

def consumer(in_q):
    while True:
        data, evt = in_q.get()
        print("Processed {}".format(data))
        evt.set()
        in_q.task_done()

if __name__ == "__main__":
    q = Queue()
    t1 = Thread(target=consumer, args=(q,), daemon=True)
    t2= Thread(target=producer, args=(q,))
    t1.start()
    t2.start()
    # Wait for all produced items to be consumed
    q.join()
