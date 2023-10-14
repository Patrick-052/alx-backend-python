#!/usr/bin/env python3
""" Async Generator """

import asyncio
import random
from typing import AsyncGenerator, NoReturn


async def async_generator() -> AsyncGenerator[float, NoReturn]:
    """ Yields a random number between 0 and 10 """
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
