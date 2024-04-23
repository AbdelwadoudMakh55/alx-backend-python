#!/usr/bin/env python3
"""
Module: 2-measure_runtime
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure runtime of async comprehension """
    start_time = time.time()
    tasks = asyncio.gather(*[async_comprehension() for i in range(4)])
    await tasks
    end_time = time.time()
    return end_time - start_time
