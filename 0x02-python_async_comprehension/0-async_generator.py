#!/usr/bin/env python3
"""Write a coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module. """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None]:
    """Async generator that yields random numbers
    between 0 and 10.
    This function loops 10 times, each time
    asynchronously waiting 1 second."""
    for _ in range(10):
        await asyncio.sleep(1)
        num = random.random() * 10
        yield num
