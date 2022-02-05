# -*- coding: utf-8 -*-
"""Test for radium."""
import asyncio
import hashlib
from random import SystemRandom

import aioconsole

vacancy_data = [
    '80 000 руб',
    'Стажёр-программист Python / Python Developer Trainee',
    'Владислав',
]


async def print_text(text: str) -> None:
    """Print text."""
    delay = SystemRandom().uniform(0, 5)
    await asyncio.sleep(delay)
    await aioconsole.aprint(text)


def make_hash(for_hash: str) -> str:
    """Make hash."""
    return hashlib.sha256(for_hash.encode('utf-8')).hexdigest()


async def do_complete_work(data_for_output: list[str]) -> None:
    """Print vacancy data and sha256 for input."""
    functions = [print_text(text) for text in data_for_output]
    await asyncio.gather(*functions)
    input_data = await aioconsole.ainput()
    hash_from_input = make_hash(input_data)
    await aioconsole.aprint(hash_from_input)


if __name__ == '__main__':
    asyncio.run(do_complete_work(vacancy_data))
