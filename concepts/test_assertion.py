import pytest


def test_title():
    actual_title="vinay kumar"
    new_title="bablu"

    assert actual_title==new_title
    assert "kumar" in actual_title, "title is wrong"
    assert False  #forceful failing a test

