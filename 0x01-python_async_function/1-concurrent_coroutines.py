#!/usr/bin/env python3
"""Coroutine that uses an imported async_comprehension."""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Coroutine that takes in 2 int arguments (in this order): n and
    max_delay and returns the list of all the delays (float values)
    from wait_random coroutine"""
    delays: List[float] = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
