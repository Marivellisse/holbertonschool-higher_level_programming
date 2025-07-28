#!/usr/bin/python3
"""Defines a class LockedClass that only allows 'first_name' as attribute."""


class LockedClass:
    __slots__ = ['first_name']
