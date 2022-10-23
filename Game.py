import pygame

pygame.init()
pygame.display.set_caption('Platformer')

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))


def run():
    game = True

    while game:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()

run()