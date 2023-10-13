#!/usr/bin/env python3
"""Basic Async Syntax and Random Uniform usage"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Implementing a simple coroutine that takes in an integer argument
    that waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it."""
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
