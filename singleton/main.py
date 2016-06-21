class Singleton(type):

    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance

class Example(metaclass=Singleton):

    def __init__(self, message):
        self.message = message

    def greet(self):
        print(self.message)

if __name__ == "__main__":
    x = Example("Hello")
    y = Example("World")
    x.greet()
    y.greet()
    print(x is y)
