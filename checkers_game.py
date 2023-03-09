import collections
from typing import Tuple, List

PAWN = "P"
KING = "K"
Position = Tuple[int, int]

white_start_positions = {(1, 6), (3, 6), (5, 6), (7, 6), (0, 7), (2, 7), (4, 7), (6, 7)}
black_start_positions = {(1, 0), (3, 0), (5, 0), (7, 0), (0, 1), (2, 1), (4, 1), (6, 1)}
PieceNT = collections.namedtuple("Piece", ["type", "position"])
white_pieces = [PieceNT(type=PAWN, position=pos) for pos in white_start_positions]
black_pieces = [PieceNT(type=PAWN, position=pos) for pos in black_start_positions]


def translate_external_to_internal(user_input: str) -> Position:
    """Takes in the string version of a pieces position and turns it in to a tuple"""
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
    """Shows the user the availible pieces and asks which on they would like to move"""
    print("Availible Pieces")
    for pos in black_pieces:
        print(translate_internal_to_external(pos.position))
    player_input = input("What piece would you like to move?").upper()
    return player_input


# still need to add king opts
def get_move_options(cur_position: Position) -> List:
    for piece in black_pieces:
        if piece.position == cur_position:
            cur_piece = piece

            move_opt_1 = (cur_piece.position[0] + 1, cur_piece.position[1] + 1)
            move_opt_2 = (cur_piece.position[0] - 1, cur_piece.position[1] + 1)
            move_opt_3 = (cur_piece.position[0] + 1, cur_piece.position[1] - 1)
            move_opt_4 = (cur_piece.position[0] - 1, cur_piece.position[1] - 1)

            if (
                cur_piece.type == "P"
                and cur_piece.position[0] != 0
                and cur_piece.position[1] != 7
            ):
                move_opts = [move_opt_1, move_opt_2]
                return move_opts
            elif cur_piece.type == "P" and cur_piece.position[0] == 0:
                move_opts = [move_opt_1]
                return move_opts
            elif cur_piece.type == "P" and cur_piece.position[1] == 7:
                move_opts = [move_opt_2]
                return move_opts
