#https://www.youtube.com/watch?v=UdsNBIzsmlI&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5&index=3

import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")

#pygame.image.load(pygame.path.join('image','R1.png')) or
#pygame.image.load('image/R1.png')
walkRight = [pygame.image.load('image/R1.png'), pygame.image.load('image/R2.png'), pygame.image.load('image/R3.png'), pygame.image.load('image/R4.png'), pygame.image.load('image/R5.png'), pygame.image.load('image/R6.png'), pygame.image.load('image/R7.png'), pygame.image.load('image/R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('image/L1.png'), pygame.image.load('image/L2.png'), pygame.image.load('image/L3.png'), pygame.image.load('image/L4.png'), pygame.image.load('image/L5.png'), pygame.image.load('image/L6.png'), pygame.image.load('image/L7.png'), pygame.image.load('image/L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('image/bg.jpg')
char = pygame.image.load('image/standing.png')

clock = pygame.time.Clock()

x = 50
y = 425
width = 64
height =64
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    win.blit(bg, (0,0))

    if walkCount + 1 >= 27:
        walkcOUNT = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight(walkCount//3), (x,y))
    else:
        win.blit(char, (x,y))
    pygame.display.update()

#mainloop
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x<500-width-vel:  #500 is the window width
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    if not(isJump):    # The only way to move up and down is by jumping
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()


pygame.quit()
