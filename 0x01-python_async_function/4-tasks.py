#!/usr/bin/env python3
"""
Module: 4-tasks
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Multiple coroutines at the same time """
    delays = []
    tasks = [task_wait_random(max_delay) for i in range(n)]
    for t in asyncio.as_completed(tasks):
        delay = await t
        delays.append(delay)
    return delays
