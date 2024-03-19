#!/usr/bin/env python3
"""
This module contains an altered function task_wait_n from wait_n which
uses task_wait_random.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.
    Returns the list of all the delays (float values) in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await t for t in asyncio.as_completed(tasks)]
