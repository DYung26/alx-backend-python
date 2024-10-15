#!/usr/bin/env python3
"""
This module provides an asynchronous function to wait for random delays
and collect the results in a sorted list.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for a specified number of random delays and returns
    a sorted list of the delays.

    Args:
        n (int): The number of random delays to wait for.
        max_delay (int): The maximum delay in seconds for the random delays.

    Returns:
        List[float]: A list of random delays (sorted) that were waited for.
    """
    random_delays = await asyncio.gather(
            *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(random_delays)
