#!/usr/bin/env python3
"""Implementing creation of asyncio.Tasks"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Function that returns an asyncio.Task"""
    list_task = asyncio.create_task(wait_random(max_delay))
    return list_task
