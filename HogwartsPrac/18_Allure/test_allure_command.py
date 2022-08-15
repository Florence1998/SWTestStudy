import pytest


def test_success():
    """this test success"""
    assert True


def test_failure():
    """this test fail"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip("for a reason!")


def test_broken():
    raise  Exception("OOPS")
