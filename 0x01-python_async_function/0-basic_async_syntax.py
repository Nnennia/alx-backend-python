#!/usr/bin/env python3
"""Write an asynchronous coroutine that takes in an integer
argument (max_delay, with a default value of 10)
named wait_random that waits for a random delay between
0 and max_delay (included and float value) seconds and
eventually returns it."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Introduce a random delay using the asyncio
    library and return the delay time as a float value.

    Args:
        max_delay (int, optional): The maximum delay time in seconds.
        Defaults to 10.

    Returns:
        float: The delay time in seconds.

    This function is used to simulate asynchronous behavior in Python code."""
    delay: float = random.uniform(1, float(max_delay))
    await asyncio.sleep(delay)
    return delay
