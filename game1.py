import pygame, sys            #when no sys, running no error, exit will give error
from pygame.locals import *

pygame.init()
win = pygame.display.set_mode((400, 600))  #mode, not model
pygame.display.set_caption('Hello World!')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()          #??
    #pygame.display.update()     #so far, no changes


# import pygame
# pygame.init()
#
# win = pygame.display.set_mode((400, 400))
# pygame.display.set_caption("Hello World!")
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#         pygame.display.update()
