#!/usr/bin/env python3
"""Measure the average runtime of wait_n(n, max_delay)."""

import asyncio
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Function to return the average runtime of wait_n """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = perf_counter()
    total_time = end - start

    return total_time / n
