from actor import Actor

class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print("Got:", msg)

if __name__ == "__main__":

    p = PrintActor()
    p.start()
    p.send("Hello")
    p.send("World!")
    p.close()
    p.join()
