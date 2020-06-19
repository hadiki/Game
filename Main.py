import pygame
from pip._vendor.html5lib._trie import py

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")

# This goes outside the while loop, near the top of the program
walkRight = [pygame.image.load('Game Pics/R1.png'), pygame.image.load('Game Pics/R2.png'), pygame.image.load('Game Pics/R3.png'), pygame.image.load('Game Pics/R4.png'), pygame.image.load('Game Pics/R5.png'), pygame.image.load('Game Pics/R6.png'), pygame.image.load('Game Pics/R7.png'), pygame.image.load('Game Pics/R8.png'), pygame.image.load('Game Pics/R9.png')]
walkLeft = [pygame.image.load('Game Pics/L1.png'), pygame.image.load('Game Pics/L2.png'), pygame.image.load('Game Pics/L3.png'), pygame.image.load('Game Pics/L4.png'), pygame.image.load('Game Pics/L5.png'), pygame.image.load('Game Pics/L6.png'), pygame.image.load('Game Pics/L7.png'), pygame.image.load('Game Pics/L8.png'), pygame.image.load('Game Pics/L9.png')]
bg = pygame.image.load('Game Pics/bg.jpg')
char = pygame.image.load('Game Pics/standing.png')

clock = pygame.time.Clock()

x = 50
y =  425
width = 64
height = 64
vel = 5
left = False
right = False
walkCount = 0

isJump = False
jumpCount = 10

def redrawGameWindow():
    global walkCount

    win.blit(bg, (0, 0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))


    pygame.display.update()


#Main Loop
run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
    if not(isJump):
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