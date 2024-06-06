import pygame
from main import screen
from pieces import draw_pieces
from board import draw_board
pygame.init()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("dark grey")
    draw_board()
    draw_pieces()
    pygame.display.flip()
pygame.quit()
