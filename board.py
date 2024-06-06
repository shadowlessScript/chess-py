import pygame
from main import WIDTH, HEIGHT, screen, big_font, medium_font
from pieces import turn_step


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



