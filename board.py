import pygame
from main import WIDTH, HEIGHT, screen, big_font, medium_font
from pieces import turn_step

def draw_board():
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
