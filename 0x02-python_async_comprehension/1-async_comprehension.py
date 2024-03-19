#!/usr/bin/env python3
"""
This module contains an asynchronous comprehension that collects
10 random numbers from an asynchronous generator.
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using an async comprehension."""
    return [i async for i in async_generator()]
