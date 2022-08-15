import pytest


def test_raise():
    with pytest.raises((ValueError, ZeroDivisionError)):
        raise ZeroDivisionError("除数为0")
