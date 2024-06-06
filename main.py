import pygame

# intialize the pygame module
pygame.init()

# setting the width and height of the window
WIDTH = 1000 
HEIGHT = 900

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

