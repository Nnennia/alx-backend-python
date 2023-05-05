#!/usr/bin/env python3
"""Import async_comprehension from the previous file
and write a measure_runtime coroutine that will
execute async_comprehension four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it."""

from time import perf_counter
from asyncio import gather
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension four times in
    parallel using asyncio.gather.
    Returns the total runtime as a float value.
    """
    start = perf_counter()
    tasks = [async_comprehension() for i in range(4)]
    await gather(*tasks)
    end = perf_counter()
    return (end - start)
