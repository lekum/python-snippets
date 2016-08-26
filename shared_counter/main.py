import threading

class SharedCounter:

    def __init__(self, initial_value = 0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def incr(self, delta=1):
        """
        Increment the counter with locking
        """
        with self._value_lock:
            self._value += delta

    def decr(self, delta=1):
        """
        Decrement the counter with locking
        """
        with self._value_lock:
            self._value -= delta

    def __str__(self):
        return str(self._value)

def incr_decr(c):
    for i in range(100):
        c.incr(i)
        c.decr(i)
        print(i)

if __name__ == "__main__":
    from concurrent.futures import ThreadPoolExecutor
    c = SharedCounter()
    print("Initial value: {}".format(c))
    pool = ThreadPoolExecutor(128)
    results = []
    for j in range(3000):
        results.append(pool.submit(incr_decr, c))
    for j in results:
        j.result()
    print("Final value: {}".format(c))
