#!/usr/bin/env python3
"""a module to calculate time"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    """
    start_time = time.time()

    # Run wait_n(n, max_delay) and wait for it to complete
    await wait_n(n, max_delay)

    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
