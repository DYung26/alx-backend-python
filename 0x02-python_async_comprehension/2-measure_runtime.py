#!/usr/bin/env python3
"""
This module measures the total runtime for executing an asynchronous
comprehension  four times concurrently using asyncio.gather. It calculates and
returns the time taken for all four async comprehensions to complete.
"""
import asyncio
import time
from importlib import import_module as using
async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime for concurrently running async comprehensions.

    This function runs the `async_comprehension` function four times in
    parallel using `asyncio.gather`, and calculates the time taken for
    all executions to complete.

    Returns:
        float: The total runtime in seconds for running the comprehensions
        concurrently.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
