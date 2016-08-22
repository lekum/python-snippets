import threading
import time


class PeriodicTimer:

    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        """
        Run the timer and notify waiting threads after each interval
        """
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all()

    def wait_for_tick(self):
        """
        Wait for the next tick of the timer
        """
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()

if __name__ == "__main__":

    ptimer = PeriodicTimer(1)
    ptimer.start()

    def countdown(nticks):
        while nticks > 0:
            ptimer.wait_for_tick()
            print('T-minus', nticks)
            nticks -= 1

    def countup(last):
        n = 0
        while n < last:
            ptimer.wait_for_tick()
            print('Counting', n)
            n += 1

    threading.Thread(target=countdown, args=(10,)).start()
    threading.Thread(target=countup, args=(5,)).start()