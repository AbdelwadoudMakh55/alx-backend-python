#!/usr/bin/env python3
"""
Module of 0-basic_async_syntax
- Discovering basic async syntax
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ async syntax
      - asyncio.sleep, await
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
