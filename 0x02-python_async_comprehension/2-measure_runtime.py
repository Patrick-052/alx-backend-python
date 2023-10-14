#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

import asyncio
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime and return it"""
    start = perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = perf_counter()
    return end - start
