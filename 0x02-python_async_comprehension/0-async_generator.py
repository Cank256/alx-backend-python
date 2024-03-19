#!/usr/bin/env python3
"""
This module contains an asynchronous generator that yields a random
number between 0 and 10 after waiting one second.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yields a random number between 0 and 10 every second for 10 times."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
