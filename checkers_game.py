import collections
from typing import Tuple, List
from dataclasses import dataclass
import operator

white_pawn = "o"
black_pawn = "x"
white_king = "O"
black_king = "X"
white_square = " "
black_square = "#"

board = [
    [
        black_square,
        white_square,
        black_square,
        white_square,
        black_square,
        white_square,
        black_square,
        white_square,
    ],
    [
        white_square,
        black_square,
        white_square,
        black_square,
        white_square,
        black_square,
        white_square,
        black_square,
    ],
    [
        black_square,
        white_square,
        black_square,
        white_square,
        black_square,
        white_square,
        black_square,
        white_square,
    ],
    [
        white_square,
        black_square,
        white_square,
        black_square,
        white_square,
        black_square,
        white_square,
        black_square,
    ],
    [
        black_square,
        white_square,
        black_square,
        white_square,
        black_square,
        white_square,
        black_square,
        white_square,
    ],
    [
        white_square,
        black_square,
        white_square,
        black_square,
        white_square,
        black_square,
        white_square,
        black_square,
    ],
    [
        black_square,
        white_square,
        black_square,
        white_square,
        black_square,
        white_square,
        black_square,
        white_square,
    ],
    [
        white_square,
        black_square,
        white_square,
        black_square,
        white_square,
        black_square,
        white_square,
        black_square,
    ],
]


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


def display_board():
    print("    ABCDEFGH ")
    print("  +----------+")

    for r, row in enumerate(board):
        print(r + 1, "| ", end="")
        for s, square in enumerate(row):
            if (s, r) in black_pieces.keys():
                print(black_pawn, end="")
            elif (s, r) in white_pieces.keys():
                print(white_pawn, end="")
            else:
                print(square, end="")
        print(" |")

    print("  +----------+")


display_board()


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


def filter_available_spaces(moves: List, goal: int) -> List:
    availible_moves = []
    for move in moves:
        if (
            0 <= move[0] < 8
            and move not in black_pieces.keys()
            and move not in white_pieces.keys()
        ):
            availible_moves.append(move)
        elif 1 <= move[0] <= 6 and (
            move in black_pieces.keys() or move in white_pieces.keys()
        ):
            if goal == 7:
                jump_move = (move[0] + 1, move[1] + 1)
                if (
                    jump_move not in black_pieces.keys()
                    and move not in white_pieces.keys()
                ):
                    availible_moves.append(jump_move)
            else:
                jump_move = (move[0] - 1, move[1] - 1)
            if jump_move not in black_pieces.keys() and move not in white_pieces.keys():
                availible_moves.append(jump_move)

    return availible_moves


# Could write helper function to check for a jump if is_availible_space returns false to check if a jump is possible
def get_forward_move(piece: Piece, direction: str) -> List:
    """
    Returns a list of possible forward moves

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
    # breakpoint()
    possible_moves = []
    piece_row_pos = piece.position[1]
    dist_per_move = 1
    goal = GOAL_ROW[piece.color]
    if direction == "forward":
        row_destination_func = (
            operator.__add__ if goal > piece_row_pos else operator.__sub__
        )
    elif direction == "back":
        row_destination_func = (
            operator.__add__ if goal < piece_row_pos else operator.__sub__
        )

    move_right = (
        operator.__add__(piece.position[0], dist_per_move),
        row_destination_func(piece_row_pos, dist_per_move),
    )
    # Could put an if in here to allow for a jump by changing dist_per_move to 2
    move_left = (
        operator.__sub__(piece.position[0], dist_per_move),
        row_destination_func(piece_row_pos, dist_per_move),
    )
    # make helper function is_available_space for this
    moves = [move_right, move_left]
    possible_moves = filter_available_spaces(moves, goal)

    return possible_moves
