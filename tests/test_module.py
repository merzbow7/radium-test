# -*- coding: utf-8 -*-
"""Test module for app.py."""
import hashlib
import random
from string import printable

import pytest

from app import do_main_job, make_hash, output_data, print_text

new_random = random.SystemRandom()


def make_random_string(length: int = 25) -> str:
    """Make random string with printable symbols."""
    return ''.join(new_random.choice(printable) for _ in range(length))


async def rewrite_input() -> str:
    return make_random_string()


@pytest.mark.asyncio()
async def test_output(capsys: pytest.CaptureFixture) -> None:
    """Test output."""
    test_str = make_random_string()
    await print_text(test_str)
    captured = capsys.readouterr()
    assert test_str in captured.out


def test_hash() -> None:
    """Test hash generation."""
    str_for_hash = make_random_string()
    sha256 = hashlib.sha256()
    sha256.update(str_for_hash.encode())
    assert sha256.hexdigest() == make_hash(str_for_hash)


@pytest.mark.asyncio()
async def test_main_func(
    capsys: pytest.CaptureFixture,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test main function."""
    monkeypatch.setattr('aioconsole.ainput', rewrite_input)
    await do_main_job(output_data)
    captured = capsys.readouterr()

    assert all(test_str in captured.out for test_str in output_data)
