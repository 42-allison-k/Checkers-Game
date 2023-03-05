import pytest
from checkers_game import (
    get_user_input,
    translate_external_to_internal,
    translate_internal_to_external,
)


def test_get_user_input():
    pass


def test_translate_external_to_internal():
    trans_output = translate_external_to_internal("A2")
    expected_output = (0, 1)
    assert trans_output == expected_output


def test_translate_internal_to_external():
    trans_output = translate_internal_to_external((0, 1))
    expected_output = "A2"
    assert trans_output == expected_output
