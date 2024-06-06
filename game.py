import pygame
from main import screen
from pieces import draw_pieces
from board import draw_board
pygame.init()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill("dark grey")
    draw_board()
    draw_pieces()
    pygame.display.flip()
