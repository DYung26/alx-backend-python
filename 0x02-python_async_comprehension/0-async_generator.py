#!/usr/bin/env python3

"""
This module demonstrates an asynchronous generator in Python.
It generates a list of 10 random floating-point numbers between 0 and 10,
yielding each number after a 1-second delay.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random float numbers between 0 and 10.

    It generates 10 random floating-point numbers with a 1-second delay between
    each number and yields them sequentially.

    Yields:
        float: A random float number between 0 and 10.
    """
    random_list = []
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
