#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

# Valid case
bg.integer_validator("my_int", 12)

# Not an int
try:
    bg.integer_validator("age", "29")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

# Not > 0
try:
    bg.integer_validator("level", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
