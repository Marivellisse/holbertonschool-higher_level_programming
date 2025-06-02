#!/usr/bin/python3
is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

a = 1
print(is_kind_of_class(a, int))       # True
print(is_kind_of_class(a, float))     # False
print(is_kind_of_class(a, object))    # True
