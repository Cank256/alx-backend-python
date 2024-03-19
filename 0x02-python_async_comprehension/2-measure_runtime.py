#!/usr/bin/env python3
"""
This module contains a coroutine that measures the total runtime
for executing async_comprehension four times in parallel.
"""
import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime for executing async_comprehension
    four times in parallel.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return end - start
