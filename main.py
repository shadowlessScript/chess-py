import pygame
from pieces import winner, black_pieces, black_locations, white_locations, white_pieces
from game_logic import check_options
# intialize the pygame module
pygame.init()

# setting the width and height of the window
WIDTH = 1000 
HEIGHT = 900



black_options = check_options(black_pieces, black_locations, "black")
white_options = check_options(white_pieces, white_locations, "white")

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Chess Game")

# fonts
main_font = "freesansbold.ttf"
font = pygame.font.Font(main_font, 20)
medium_font = pygame.font.Font(main_font, 40)
big_font = pygame.font.Font(main_font, 50)

# fps
timer = pygame.time.Clock()
fps = 60

def draw_game_over() -> None:
    pygame.draw.rect(screen, "black", [200, 200, 400, 70])
    screen.blit(font.render(
        f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart!',
                            True, 'white'), (210, 240))
