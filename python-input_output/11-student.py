#!/usr/bin/python3
"""
Student class with support for JSON serialization and reloading.
"""


class Student:
    """
    Represents a student with JSON serialization capabilities.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary of selected attributes or all attributes.
        """
        if isinstance(attrs, list) and all(
            isinstance(attr, str) for attr in attrs
        ):
            return {
                key: getattr(self, key)
                for key in attrs if hasattr(self, key)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes using the provided JSON dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
