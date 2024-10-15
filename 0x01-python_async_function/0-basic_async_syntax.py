#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine `wait_random` that waits for
a random delay between 0 and max_delay seconds (inclusive) and returns the
actual delay time as a float.

It can be used to simulate random delay scenarios in asynchronous code.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0
    and max_delay seconds (inclusive), and returns the delay value.

    Args:
        max_delay (int): Maximum delay time in seconds. Default is 10.

    Returns:
        float: The actual delay time (random float between 0 and max_delay).
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
