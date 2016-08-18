import time
from threading import Thread, Event

def countdown(n, started_evt):
    print('Countdown starting')
    started_evt.set()
    while n > 0:
        print('->', n)
        n -= 1
        time.sleep(2)

if __name__ == "__main__":
    started_evt = Event()
    print('Launching countdown')
    t = Thread(target=countdown, args=(10, started_evt), daemon=True)
    t.start()
    started_evt.wait()
    print('Countdown is running')
    t.join()
