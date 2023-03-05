import pytest
from checkers_game import (
    get_user_input,
    translate_external_to_internal,
    translate_internal_to_external,
)


def test_get_user_input():
    pass


@pytest.mark.parametrize(
    ["input_row", "output_row"],
    [("1", 0), ("2", 1), ("3", 2), ("4", 3), ("5", 4), ("6", 5), ("7", 6), ("8", 7)],
)
@pytest.mark.parametrize(
    ["input_col", "output_col"],
    [("A", 0), ("B", 1), ("C", 2), ("D", 3), ("E", 4), ("F", 5), ("G", 6), ("H", 7)],
)
def test_translate_external_to_internal_success(
    input_col, output_col, input_row, output_row
):
    trans_output = translate_external_to_internal(input_col + input_row)
    expected_output = (output_col, output_row)
    assert trans_output == expected_output


@pytest.mark.parametrize(["user_input"], [("A9",), ("I0",), ("2B",)])
def test_translate_external_to_internal_failure(user_input):
    with pytest.raises(ValueError):
        translate_external_to_internal(user_input)


def test_translate_internal_to_external():
    trans_output = translate_internal_to_external((0, 1))
    expected_output = "A2"
    assert trans_output == expected_output
