from actor import Actor

class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print("Got:", msg)


class TaggedActor(Actor):

    def run(self):
        while True:
            tag, *payload = self.recv()
            getattr(self,'do_'+tag)(*payload)

    # Methods correponding to different message tags
    def do_A(self, x):
        print('Running A', x)

    def do_B(self, x, y):
        print('Running B', x, y)

if __name__ == "__main__":

    p = PrintActor()
    p.start()
    p.send("Hello")
    p.send("World!")
    p.close()
    p.join()

    t = TaggedActor()
    t.start()
    t.send(("A", "hello"))
    t.send(("B", "hello", "world!"))
    t.close()
    t.join()
