"""Piece movement validator"""
import pygame
from pieces import white_locations, black_locations, turn_step, selection

def check_options(pieces: list, locations: list, turn: str) -> list:
    """
        Checks the location a piece, which piece has been selected and
        whose turn it is, and gather its legal moves.

        Uses the check_<insert_piece_name_here>() function  to find a piece's valid moves,
        stores it in the moves_list variable then appends it the all_moves_list
        which will be returned.

        :param pieces: contains name of the piecs
        :type pieces: list
        :param locations: pieces position in the board
        :type locations: list
        :param turn: whose turn is it? black or white.
        :type turn: str
        :returns: all_moves_lst: list containing a piece's legal moves.
        :rtype: list
    """
    moves_list = []
    all_moves_list = []

    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]

        # TODO: Confirm the data type of turn

        if piece == "pawn":
            moves_list = check_pawn(location, turn)
        elif piece == "rook":
            moves_list = check_rook(location, turn)
        elif piece == "knight":
            moves_list = check_knight(location, turn)
        elif piece == "bishop":
            moves_list = check_bishop(location, turn)
        elif piece == "queen":
            moves_list = check_queen(location, turn)
        elif piece == "king":
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list


def check_king(position, color):
    """
        A king can only move to one square in any direction, and as long as
        no friendly piece is at the desired position, and will not lead to a 
        self induced check, meaning an enemy piece is attacking the square.

        :param position: location of the king
        :type position: list
        :param color: name changed from turn as used in the check_options function
        :type color: str
        :returns: moves_list
        :rtype: list
    """
    moves_list = []
    if color == "white":
        enemies_list = black_locations
        friend_list = white_locations
    else:
        friend_list = black_locations
        enemies_list = white_locations

    targets = [(1, 0), (1, 1), (1, -1), (-1, 0),
              (-1, 1), (-1, -1), (0, 1), (0, -1)]

    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friend_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)

    return moves_list

def check_queen(position, color):
    """
        Queen can move to any direction and any number of steps.
        Thus a combination of the rook and the bishop.
    """
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    
    return moves_list.extend(second_list)

def check_bishop(position, color):
    moves_list = []
    if color == "white":
        enemies_list = black_locations
        friends_list = white_locations
    else:
        enemies_list = white_locations
        friends_list = black_locations

    path = True
    chain = 1
    for i in range(4):
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1

        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append(
                        (position[0] + (chain * x), position[1] + (chain * y)))

                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

def check_rook(position: list, color: str) -> list:
    moves_list = []
    if color == "white":
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations

    path = True
    chain = 1
    for i in range(4):
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i ==2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append(
                    (position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

def check_pawn(position: list, color: str) -> list:
    moves_list = []
    if color == "white":
        if(position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:
                    moves_list.append((position[0], position[1] + 1))
        if(position[0], position[1] + 2) not in black_locations and \
                (position[0], position[1] + 2) not in black_locations and position[1] == 1:
                    moves_list.append((position[0], position[1] + 2))
        if(position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if(position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

def check_knight(position: list, color: str) -> list:
    """
            (-1, 2)  (1, 2)
          ___ ___ ___ ___ ___
         |___|_+_|___|_+_|___|
(-2,1)   |_+_|___|___|___|_+_|<- (2, 1)
         |___|___|_k_|___|___|
(-2,-1)  |_+_|___|___|___|_+_|<- (2, -1)
         |___|_+_|___|_+_|___|
               ^       ^
               |       |  
            (-1,-2)  (1, -2)
        Diagram above are the possible coordinates that a knight can jump to.
    """
    moves_list = []
    if color == "white":
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    targets = [(1, 2), (1, -2), (2, 1), (2, -1),
               (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

def check_valid_moves() -> list:
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options

