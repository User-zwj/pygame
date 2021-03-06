#https://www.youtube.com/watch?v=i6xMBig-pP4&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5

import pygame
pygame.init()    #MUST

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height =60
vel = 5

run = True
while run:
    # pygame.time.delay(100)    #pause the program for some time (milliseconds)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:  #don't forget pygame
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    win.fill((0,0,0))   #if not, rect will connect to each other
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()   #refresh the screen, if no, just white window

pygame.quit()
