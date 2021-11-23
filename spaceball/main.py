import pygame
from table import *

pygame.init()
pygame.display.set_caption("spaceball")


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

clock = pygame.time.Clock()

boardstatus = Board()


while boardstatus.board_level() < 4:

    






    pygame.display.flip()

pygame.quit()