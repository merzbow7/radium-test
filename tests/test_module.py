# -*- coding: utf-8 -*-
"""Test module for app.py."""
import asyncio
import hashlib
import random
from string import printable
from typing import TypeVar

import pytest

from app import do_complete_work, make_hash, print_text, vacancy_data

sys_random = random.SystemRandom()

TReplace = TypeVar('TReplace', bound='Replace')


class Replace(object):
    """Class for replace string as callable."""

    def __init__(self: TReplace, replace: str = '') -> None:
        """Init replace string."""
        self.replace = replace

    async def __call__(self: TReplace, *args) -> str:
        """Return replace string."""
        await asyncio.sleep(0)
        return self.replace


async def make_random_string(length: int = 25) -> str:
    """Make random string with printable symbols."""
    await asyncio.sleep(0)
    return ''.join(sys_random.choice(printable) for _ in range(length))


@pytest.mark.asyncio()
async def test_output(capsys: pytest.CaptureFixture) -> None:
    """Test output."""
    test_str = await make_random_string()
    await print_text(test_str)
    captured = capsys.readouterr()
    assert test_str in captured.out


@pytest.mark.asyncio()
async def test_hash() -> None:
    """Test hash generation."""
    str_for_hash = await make_random_string()
    sha256 = hashlib.sha256()
    sha256.update(str_for_hash.encode())
    assert sha256.hexdigest() == make_hash(str_for_hash)


@pytest.mark.asyncio()
async def test_main_func(
    capsys: pytest.CaptureFixture,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test main function."""
    random_string = Replace(await make_random_string())
    hashed_random = make_hash(random_string.replace)

    monkeypatch.setattr('aioconsole.ainput', random_string)
    await do_complete_work(vacancy_data)
    captured = capsys.readouterr()

    expected_out = [*vacancy_data, hashed_random]
    assert all(expected_str in captured.out for expected_str in expected_out)
    print(captured)

