import pygame
from main import WIDTH, HEIGHT, screen, big_font, medium_font
from pieces import (turn_step, small_white_images,
                    small_black_images, piece_list,
                    white_locations, black_locations,
                    white_pieces, black_pieces,
                    selection, counter,
                    captured_pieces_black, captured_pieces_white)
from game_logic import black_options, white_options # may cause circular importation error

def draw_board() -> None:
    for i in range(32):
        column = i % 4
        row = i // 4

        if row % 2 == 0:
            pygame.draw.rect(screen, 'purple', [
                    600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'purple', [
                700 - (column * 200), row * 100, 100, 100])
        pygame.draw.rect(screen, 'white', [0, 800, WIDTH, 100])
        pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5)
        pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5)
        status_text = ['white: Select a Piece to move!', 'White: Select a destination',
                       'Black: Select a Piece to move', 'Black: Select a destination']

        screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, 820))

        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)
        screen.blit(medium_font.render('Forfeit', True, 'black'), (810, 830))


def draw_valid(moves: list) -> None:
    """
        visually represent valid moves on the screen by drawing small circles
        using red cirles for white and blue circles for black's turn.

        :param moves: list of valid moves
        :type moves: list
   """
    if turn_step < 2:
        color = "red"
    else:
        color = "blue"
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)


def draw_captured() -> None:
    """will display the captured pieces on the right side of the board"""

    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index[captured_piece]
        screen.blit(small_black_images[index], (825, 5 + 50 * i))

    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (925, 5 + 50 * i))


def draw_check() -> None:
    if turn_step < 2:
        if "king" in white_pieces:
            king_index = white_pieces.index("king")
            king_location = white_locations[king_index]
            
            for i in range(len(black_options)):
                if king_location in black_options[i] and black_options[i] != None:
                    if counter < 15:
                        pygame.draw.rect(screen, "dark red", 
                            [white_locations[king_index][0] * 100 + 1, 
                             white_locations[king_index][1] * 100 +1, 100, 100], 5)
    else:
        if "king" in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark blue', [black_locations[king_index][0] * 100 + 1,
                                                               black_locations[king_index][1] * 100 + 1, 100, 100], 5)
                else:
                    break

