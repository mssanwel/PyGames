import pygame
import random

# Initialize
pygame.init()
# set icon and bar
pygame.display.set_caption("Space Invader")
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)
# Screen setup
screenWidth=800
screenHeight=600
screen = pygame.display.set_mode((screenWidth,screenHeight))
# Player setup
playerImage=pygame.image.load("spaceship.png")
playerWidth=50
playerHeight=30
playerImage=pygame.transform.scale(playerImage,(playerWidth,playerHeight))
pX=(screenWidth-playerWidth)*0.5
pY=screenHeight*0.9
# Draw player
def player(pX,pY):
    screen.blit(playerImage,(pX,pY))

# Enemy setup
enemyImage=pygame.image.load("enemy.png")
enemyWidth=50
enemyHeight=40
enemyImage=pygame.transform.rotate((pygame.transform.scale(enemyImage,(enemyWidth,enemyHeight))),180)
eX=random.randint(0,(screenWidth-enemyWidth))
eY=screenHeight*0.1
# Draw bullet
def enemy(eX,eY):
    screen.blit(enemyImage,(eX,eY))


# Bullet setup
bulletImage=pygame.image.load("bullet.png")
bulletWidth=10
bulletHeight=20
bulletImage=pygame.transform.scale(bulletImage,(bulletWidth,bulletHeight))
bX=pX+playerWidth*0.5
bY=screenHeight*0.9
# Draw bullet
def bullet(bX,bY):
    screen.blit(bulletImage,(bX,bY))

# Main loop
xDiff=0
eXDiff=0.5
eYDiff=15
bYDiff=0
fire=True
running=True
while running:
    screen.fill((100, 110, 130))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        # Key pressed
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                xDiff=1
            if event.key==pygame.K_LEFT:
                xDiff=-1
            if event.key==pygame.K_SPACE:
                bYDiff=-5
                fire=True
        # Key up
        if event.type==pygame.KEYUP:
            xDiff=0

    # update change in x for player
    pX+=xDiff
    # Setting boundaries for player
    if pX<0:
        pX=0
    elif pX>(screenWidth-playerWidth):
        pX=screenWidth-playerWidth
    # Draw player
    player(pX,pY)


    # update x of enemy
    eX+=eXDiff
    # Setting boundaries for enemy
    if eX>=(screenWidth-enemyWidth):
        eXDiff=-eXDiff
        eY += eYDiff
    if eX<=(0):
        eXDiff=-eXDiff
        eY += eYDiff
    # Draw enemy
    enemy(eX,eY)

    # update y of bullet
    bY += bYDiff
    if not(fire):
        bX=pX
    # Setting boundaries for bullet
    if bY <= 0:
        bYDiff=0
        bY=0.9*screenHeight
        fire=False
    # Draw enemy
    bullet(bX, bY)
    # update screen
    pygame.display.update()