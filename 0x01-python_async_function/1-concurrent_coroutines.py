#!/usr/bin/env python3
"""
This module provides an asynchronous function to wait for random delays
and collect the results in a sorted list.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for a specified number of random delays.

    Args:
        n (int): The number of random delays to wait for.
        max_delay (int): The maximum delay in seconds for the random delays.

    Returns:
        List[float]: A list of random delays (sorted) that were waited for.
    """
    random_delays = await async.io.gather(
            *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return (sorted(random_delays))
