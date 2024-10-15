#!/usr/bin/env python3
"""
This module provides a function to create an asyncio task
that waits for a random delay.
"""
import asyncio
wait_random = ___import__.('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio task that waits for a random delay.

    Args:
        max_delay (int): The maximum delay in seconds for the random delay.

    Returns:
        asyncio.Task: An asyncio task that will execute wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
