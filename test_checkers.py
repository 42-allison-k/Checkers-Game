import pytest
import checkers_game
from checkers_game import (
    get_user_input,
    translate_external_to_internal,
    translate_internal_to_external,
    get_forward_move,
    get_backward_move,
    Piece,
    PAWN,
    BLACK,
    WHITE,
    KING,
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


"""
a piece in col 0
a piece in col 7
a piece in the middle
a piece with one in the way of the same color going forward
a piece with one in the way of the same color going back
a piece with one in the way of a different color going back
a piece with one in the way of a different color going forward

"""


@pytest.mark.parametrize(
    ["test_piece", "white_pieces", "black_pieces", "expected_moves"],
    [
        pytest.param(
            Piece(type=PAWN, position=(0, 6), color=WHITE),
            {},
            {},
            [(1, 5)],
            id="single white piece on the left edge of the board",
        ),
        pytest.param(
            Piece(type=PAWN, position=(0, 1), color=BLACK),
            {},
            {},
            [(1, 2)],
            id="single black piece on the left edge of the board",
        ),
        pytest.param(
            Piece(type=PAWN, position=(0, 6), color=WHITE),
            {(1, 5): Piece(type=PAWN, position=(1, 5), color=WHITE)},
            {},
            [(2, 4)],
            id="White Piece with a white piece in the way",
        ),
        pytest.param(
            Piece(type=PAWN, position=(1, 1), color=BLACK),
            {(2, 2): Piece(type=PAWN, position=(2, 2), color=WHITE)},
            {},
            [(3, 3), (0, 2)],
            id="Black Piece with a white piece in the way",
        ),
    ],
)
def test_get_forward_move(
    test_piece, white_pieces, black_pieces, expected_moves, monkeypatch
):
    # GIVEN
    if test_piece.color == WHITE:
        white_pieces[test_piece.position] = test_piece
    else:
        black_pieces[test_piece.position] = test_piece

    monkeypatch.setattr(checkers_game, "white_pieces", white_pieces)
    monkeypatch.setattr(checkers_game, "black_pieces", black_pieces)

    # WHEN
    move_output = get_forward_move(test_piece)

    # THEN
    assert move_output == expected_moves


"""
a piece in col 0
a piece in col 7
a piece in the middle
a piece with one in the way of the same color going back
a piece with one in the way of a different color going back

"""


def test_get_backward_move():
    pass
