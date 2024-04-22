#!/usr/bin/env python3
"""
Module of 1-concurrent_coroutines
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    """ Multiple coroutines at the same time """
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    for t in asyncio.as_completed(tasks):
        delay = await t
        delays.append(delay)
    return delays
