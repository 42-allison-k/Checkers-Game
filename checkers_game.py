import collections
from typing import Tuple, List
from dataclasses import dataclass
import operator


BLACK = "B"
WHITE = "W"
GOAL_ROW = {BLACK: 7, WHITE: 0}
PAWN = "P"
KING = "K"
Position = Tuple[int, int]

white_start_positions = {(1, 6), (3, 6), (5, 6), (7, 6), (0, 7), (2, 7), (4, 7), (6, 7)}
black_start_positions = {(1, 0), (3, 0), (5, 0), (7, 0), (0, 1), (2, 1), (4, 1), (6, 1)}


@dataclass
class Piece:
    type: str
    position: Position
    color: str


white_pieces = {
    pos: Piece(type=PAWN, position=pos, color=WHITE) for pos in white_start_positions
}
black_pieces = {
    pos: Piece(type=PAWN, position=pos, color=BLACK) for pos in black_start_positions
}


def translate_external_to_internal(user_input: str) -> Position:
    """
    Returns position as a tuple

    example: A2 -> (0, 1)
    """
    cols = "ABCDEFGH"
    piece_col = cols.index(user_input[0])
    piece_row = int(user_input[1]) - 1
    if piece_row > 7:
        raise ValueError("row must be not greater than 8")
    position = (piece_col, piece_row)
    return position


def translate_internal_to_external(position: Position) -> str:
    """
    Returns position as a letter + number pair

    example: (0, 1) -> A2
    """
    cols = "ABCDEFGH"
    piece_col = cols[position[0]]
    piece_row = int(position[1]) + 1
    external_piece = f"{piece_col}{piece_row}"
    return external_piece


# once the rest is set up use an if statement to check for black or white pieces
def get_user_input():
    """Returns the piece the player would like to move from a list of availible pieces"""
    print("Availible Pieces")
    for position in black_pieces.keys():
        print(translate_internal_to_external(position))
    player_input = input("What piece would you like to move?").upper()
    return player_input


# change name of variable
# look breaking into more functions
# function to determines forward moves and backward moves for pawns and kings
# def get_move_options(cur_position: Position) -> List:
# """
# Returns a list of possible moves

# Example: (2, 1) -> [(3, 2), (1, 2)]
# """


def get_forward_move(piece: Piece):
    """
    Returns a list of possible moves

    Example: (2, 1) -> [(3, 2), (1, 2)]
    """
    """
    check color
    if black row increasing
    if white row decreasing
    start with [] of moves and add moves if they are posible
    check for piece at destination
    check keys of each dict for black and white pieces
    if destination is in black and white dict its not a posible move
    TODO: add jumping pieces
    if destination is a posible move add it to the list
    return the list
    """

    possible_moves = []
    piece_row_pos = piece.position[1]
    dist_per_move = 1
    goal = GOAL_ROW[piece.color]
    row_destination_func = (
        operator.__add__ if goal > piece_row_pos else operator.__sub__
    )
    move_opt_1 = (
        (piece.position[0] + 1),
        row_destination_func(piece_row_pos, dist_per_move),
    )
    move_opt_2 = (
        (piece.position[0] - 1),
        row_destination_func(piece_row_pos, dist_per_move),
    )
    if (
        0 <= move_opt_1[0] < 8
        and move_opt_1 not in black_pieces.keys()
        and move_opt_1 not in white_pieces.keys()
    ):
        possible_moves.append(move_opt_1)

    if (
        0 <= move_opt_2[0] < 8
        and move_opt_2 not in black_pieces.keys()
        and move_opt_2 not in white_pieces.keys()
    ):
        possible_moves.append(move_opt_2)

    return possible_moves


print(get_forward_move(black_pieces[(2, 1)]))


def get_backward_move():
    pass
