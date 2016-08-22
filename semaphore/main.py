import threading
import time

def worker(i, sema):
    sema.acquire()
    print("Worker {} working!".format(i))

if __name__ == "__main__":
    sema = threading.Semaphore(0)
    nworkers = 10
    for n in range(nworkers):
        t = threading.Thread(target=worker, args=(n, sema))
        t.start()
    time.sleep(1)
    for n in range(nworkers):
        sema.release()
