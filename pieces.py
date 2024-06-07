"""
    This will deal with the pieces logic, their coordinate in the board.
"""

import pygame
from io import BytesIO
import rembg
#from main import screen


WIDTH = 1000 
HEIGHT = 900

screen = pygame.display.set_mode([WIDTH, HEIGHT])

white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                  (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

captured_pieces_white = []
captured_pieces_black = []

# setting the foundation for taking turns playing.
turn_step = 0 # meaning white will start
selection = 100
valid_moves = []

# load the game pieces
normal_piece_size = (80, 80)
small_piece_size = (45, 45)

b_pieces_path = "assets/pieces/b_pieces"
w_pieces_path = "assets/pieces/w_pieces"
# ------ loading black pieces --------
b_queen = pygame.image.load(f"{b_pieces_path}/b_queen.png").convert_alpha()
b_queen = pygame.transform.scale(b_queen, normal_piece_size)
b_queen_small = pygame.transform.scale(b_queen, small_piece_size)

b_king = pygame.image.load(f"{b_pieces_path}/b_king.png").convert_alpha()
b_king = pygame.transform.scale(b_king, normal_piece_size)
b_king_small = pygame.transform.scale(b_king, small_piece_size)

b_rook = pygame.image.load(f"{b_pieces_path}/b_rook.png").convert_alpha()
b_rook = pygame.transform.scale(b_rook, normal_piece_size)
b_rook_small = pygame.transform.scale(b_rook, small_piece_size)

b_knight = pygame.image.load(f"{b_pieces_path}/b_knight.png").convert_alpha()
b_knight = pygame.transform.scale(b_knight, normal_piece_size)
b_knight_small = pygame.transform.scale(b_knight, small_piece_size)

b_bishop = pygame.image.load(f"{b_pieces_path}/b_bishop.png").convert_alpha()
b_bishop = pygame.transform.scale(b_bishop, normal_piece_size)
b_bishop_small = pygame.transform.scale(b_bishop, small_piece_size)

b_pawn = pygame.image.load(f"{b_pieces_path}/b_pawn.png").convert_alpha()
b_pawn = pygame.transform.scale(b_pawn, normal_piece_size)
b_pawn_small = pygame.transform.scale(b_pawn, small_piece_size)

# --------- loading white pieces -------------
w_queen = pygame.image.load(f"{w_pieces_path}/w_queen.png").convert_alpha()
w_queen = pygame.transform.scale(w_queen, normal_piece_size)
w_queen_small = pygame.transform.scale(w_queen, small_piece_size)

w_king = pygame.image.load(f"{w_pieces_path}/w_king.png").convert_alpha()
w_king = pygame.transform.scale(w_king, normal_piece_size)
w_king_small = pygame.transform.scale(w_king, small_piece_size)

w_rook = pygame.image.load(f"{w_pieces_path}/w_rook.png").convert_alpha()
w_rook = pygame.transform.scale(w_rook, normal_piece_size)
w_rook_small = pygame.transform.scale(w_rook, small_piece_size)

w_knight = pygame.image.load(f"{w_pieces_path}/w_knight.png").convert_alpha()
w_knight = pygame.transform.scale(w_knight, normal_piece_size)
w_knight_small = pygame.transform.scale(w_knight, small_piece_size)

w_bishop = pygame.image.load(f"{w_pieces_path}/w_bishop.png").convert_alpha()
w_bishop = pygame.transform.scale(w_bishop, normal_piece_size)
w_bishop_small = pygame.transform.scale(w_bishop, small_piece_size)

w_pawn = pygame.image.load(f"{w_pieces_path}/w_pawn.png").convert_alpha()
w_pawn = pygame.transform.scale(w_pawn, normal_piece_size)
w_pawn_small = pygame.transform.scale(w_pawn, small_piece_size)

# grouping white pieces

white_images = [w_pawn, w_king, w_queen, w_knight, w_rook, w_bishop]
small_white_images = [w_pawn_small, w_king_small, w_queen_small,
                      w_knight_small, w_rook_small, w_bishop_small]

# grouping black pieces
black_images = [b_pawn, b_king, b_queen, b_knight, b_rook, b_bishop]
small_black_images = [b_pawn_small, b_king_small, b_queen_small, b_knight_small,
                      b_rook_small, b_bishop_small]

piece_list = ["pawn", "queen", "king", "knight", "rook", "bishop"]

counter = 0
winner = ""
game_over = False

def draw_pieces():
    for i in range(len(white_pieces)):
        white_piece = white_pieces[i]
        index = piece_list.index(white_piece)

        if white_piece == "pawn":
            screen.blit( w_pawn, (
                white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30))
        else:
            screen.blit(white_images[index], (
                white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))

        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(
                        screen, 'red', [white_locations[i][0] * 100 + 1, 
                                       white_locations[i][1] + 100 + 1, 100, 100], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        black_piece = black_pieces[i]

        if black_piece == 'pawn':
            screen.blit(
                    b_pawn, (black_locations[i][0] * 100 + 22, black_locations[i][1] * 100 + 30))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 100 + 10,
                                            black_locations[i][1] * 100 + 10))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [
                    black_locations[i][0] * 100 + 1, 100, black_locations[i][1] * 100 + 1, 100, 100], 2)

