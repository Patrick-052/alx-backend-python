#!/usr/bin/env python3
"""Coroutine that uses an imported async_comprehension."""

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, wait_delay: int) -> list[float]:
    """Coroutine that takes in 2 int arguments (in this order): n and
    max_delay and returns the list of all the delays (float values)
    from wait_random coroutine"""
    delays = [await wait_random(wait_delay) for _ in range(n)]
    return sorted(delays)
