#!/usr/bin/env python3
"""
This module provides a function to measure the average time it takes
to execute the wait_n coroutine.
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average time taken to execute wait_n.

    Args:
        n (int): The number of random delays to wait for.
        max_delay (int): The maximum delay in seconds for the random delays.

    Returns:
        float: The average time per call to wait_n in seconds.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return ((time.time() - start_time) / n)
