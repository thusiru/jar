import pytest

from jar import jar


def test_string():
    assert jar("cat") == "Size cannot be a string"


def test_negative():
    assert jar("-1") == "Size cannot be negative"
    assert jar("-999") == "Size cannot be negative"
    assert jar("-5") == "Size cannot be negative"


def test_symbol():
    assert jar(".") == "Size cannot be a string"
    assert jar("'") == "Size cannot be a string"
    assert jar("$") == "Size cannot be a string"


def test_positive():
    assert jar("1") == "Okay, I created a size 1 jar!"
    assert jar("0") == "Okay, I created a size 0 jar!"
    assert jar("99") == "Okay, I created a size 99 jar!"
