import pytest
from checkers_game import (
    get_user_input,
    translate_external_to_internal,
    translate_internal_to_external,
    get_move_options,
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


@pytest.mark.parametrize(
    ["input_row", "output_row"],
    [(0, "1"), (1, "2"), (2, "3"), (3, "4"), (4, "5"), (5, "6"), (6, "7"), (7, "8")],
)
@pytest.mark.parametrize(
    ["input_col", "output_col"],
    [(0, "A"), (1, "B"), (2, "C"), (3, "D"), (4, "E"), (5, "F"), (6, "G"), (7, "H")],
)
def test_translate_internal_to_external_success(
    input_col, output_col, input_row, output_row
):
    trans_output = translate_internal_to_external((input_col, input_row))
    expected_output = output_col + output_row
    assert trans_output == expected_output


# need to figure out how to do this so it works
@pytest.mark.parametrize(
    ["input_tup, output_list"],
    [((0, 1), [(1, 2)]), ((2, 1), [(1, 2), (3, 2)]), ((6, 1), [(7, 2)])],
)
def test_get_move_options(input_tup, output_list):
    move_output = get_move_options(input_tup)
    expected_moves = output_list
    assert move_output == expected_moves
