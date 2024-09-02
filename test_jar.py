import pytest

from jar import jar


def test_string():
    with pytest.raises(SystemExit):
        jar("cat")
    with pytest.raises(SystemExit):
        jar("dog")
    with pytest.raises(SystemExit):
        jar("ooo")


def test_negative():
    with pytest.raises(SystemExit):
        jar("-1")
    with pytest.raises(SystemExit):
        jar("-999")
    with pytest.raises(SystemExit):
        jar("-5")


def test_symbol():
    with pytest.raises(SystemExit):
        jar(".")
    with pytest.raises(SystemExit):
        jar("-")
    with pytest.raises(SystemExit):
        jar("'")


def test_positive():
    assert jar("1") == "Okay, I created a size 1 jar!"
    assert jar("0") == "Okay, I created a size 0 jar!"
    assert jar("99") == "Okay, I created a size 99 jar!"
