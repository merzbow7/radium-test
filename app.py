# -*- coding: utf-8 -*-
"""Test for radium."""
import asyncio
import hashlib
from random import SystemRandom

import aioconsole

output_data = [
    '100 000 руб',
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


async def do_main_job(data_for_output: list[str]) -> None:
    """Do main job."""
    functions = [print_text(text) for text in data_for_output]
    await asyncio.gather(*functions)
    await aioconsole.aprint('Введите что-нибудь:', end='')
    input_data = await aioconsole.ainput()
    hash_from_input = make_hash(input_data)
    await aioconsole.aprint(hash_from_input)


if __name__ == '__main__':
    asyncio.run(do_main_job(output_data))
