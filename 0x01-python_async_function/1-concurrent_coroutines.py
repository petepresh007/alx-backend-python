#!/usr/bin/env python3
"""a module to create double async"""
import asyncio
from typing import List
from heapq import heappush, heappop
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times
    """
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Use asyncio.gather to run all the coroutines concurrently
    delays = await asyncio.gather(*tasks)

    # Sort the delays using a heap (min-heap ensures ascending order)
    sorted_delays = []
    for delay in delays:
        heappush(sorted_delays, delay)

    return [heappop(sorted_delays) for _ in range(len(sorted_delays))]
