#!/usr/bin/env python3
"""
Module of 0-basic_async_syntax
"""
import asyncio
from random import uniform


async def wait_random(max_delay=10):
    """ async syntax """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
