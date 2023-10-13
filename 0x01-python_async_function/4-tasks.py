#!/usr/bin/env python3
"""Implementing Async Task Usage"""

from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Coroutine that takes in 2 int arguments and returns a list
    of floats from an asyncio Task"""
    delays: List[float] = [
        await task_wait_random(max_delay) for _ in range(n)
    ]
    return sorted(delays)
