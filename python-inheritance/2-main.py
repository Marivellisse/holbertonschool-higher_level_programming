#!/usr/bin/python3
is_same_class = __import__('2-is_same_class').is_same_class

a = 1
print(is_same_class(a, int))         # True
print(is_same_class(a, float))       # False
print(is_same_class(a, object))      # False
