from collections import Counter

text = """
A vane display is a type of 7-segment display. Unlike LED and VFD segmented displays, vane displays are composed of seven physical surfaces, typically painted white, but occasionally other colors, such as yellow or fluorescent green. If a segment is to be displayed as "off", it will be rotated so that its edge faces forward, with the painted surface pointing away and not visible. A segment that is to be displayed as "on" will be rotated so that the painted surface is shown.
"""
words = text.lower().split()
c = Counter(words)
print("Five most common words:")
for word, occurences in c.most_common(5):
    print(word, "->", occurences)
