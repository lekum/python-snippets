from concurrent.futures import ThreadPoolExecutor

def greet(id_):
    return "Hi, my ID is {}".format(id_)

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as pool:
        submissions = []
        submissions = (pool.submit(greet, i) for i in range(25))
        results = (s.result() for s in submissions)
        print(list(results))

