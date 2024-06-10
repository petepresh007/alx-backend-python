#!/usr/bin/env python3
"""a module module that creates a function"""
import asyncio
from typing import List
from heapq import heappush, heappop
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns task_wait_random n times
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Use asyncio.gather to run all the coroutines concurrently
    delays = await asyncio.gather(*tasks)

    # Sort the delays using a heap (min-heap ensures ascending order)
    sorted_delays = []
    for delay in delays:
        heappush(sorted_delays, delay)

    return [heappop(sorted_delays) for _ in range(len(sorted_delays))]
