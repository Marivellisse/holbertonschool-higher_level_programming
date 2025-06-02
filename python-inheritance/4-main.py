#!/usr/bin/python3
inherits_from = __import__('4-inherits_from').inherits_from

a = True
print(inherits_from(a, int))        # True (bool is subclass of int)
print(inherits_from(a, bool))       # False (same class, not subclass)
