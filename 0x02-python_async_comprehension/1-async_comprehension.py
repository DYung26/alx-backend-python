#!/usr/bin/env python3
"""
This module demonstrates an asynchronous comprehension in Python.
It collects 10 random floating-point numbers generated by an asynchronous
generator into a list using an asynchronous comprehension.
"""
from typing import List
from importlib import import_module as using
async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List(float):
    """
    Asynchronous comprehension that collects random float numbers from
    an async generator into a list.

    This function asynchronously collects 10 random floating-point numbers
    generated by `async_generator` using an async comprehension.

    Returns:
        list: A list of random float numbers.
    """
    return [num async for num in async_generator()]
