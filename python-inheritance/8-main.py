#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

r = Rectangle(3, 5)
print(r)

try:
    r2 = Rectangle("3", -1)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
