import time
from threading import Thread

def countdown(n):
    while n > 0:
        print('->', n)
        n -= 1
        time.sleep(2)

if __name__ == "__main__":
    t = Thread(target=countdown, args=(10,), daemon=True)
    t.start()
    t.join()
