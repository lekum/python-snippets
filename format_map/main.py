import sys

class safesub(dict):
    def __missing__(self, key):
        return '¿' + key +'?'

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))


name = "Guido"
n = 37
print(sub("Hello {name}!"))
print(sub("You have {n} messages."))
print(sub("Your favourite color is {color}"))
