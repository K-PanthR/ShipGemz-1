import pgzrun
import random
from random import randint

WIDTH=500
HEIGHT=500
TITLE="Gem_Catchers"

gem=Actor("gemyellow")
gem.x=randint(20,480)
gem.y=0

ship=Actor("playership2_red")
ship.x=250
ship.y=400
score=0
gameover=False

def update():
    global game_over , score
    if keyboard.left:
        ship.x-=5
        if ship.x<0:
            ship.x=0
    if keyboard.right:
        ship.x+=5
        if ship.x>WIDTH:
            ship.x=WIDTH

    gem.y = gem.y + 1
    if gem.y > HEIGHT:
        game_over = True
    if gem.colliderect(ship):
        gem.x = random.randint (20,600)
        gem.y = 10
        score = score + 1
def draw():
    screen.clear()
    screen.fill((22,28,68))
    if gameover:
        screen.draw.text("Game Over",(360,300),color=(255,255,255))
    else:
        gem.draw()
        ship.draw()
        screen.draw.text("Score:" + str(score) , (15,10) , "color" == (255,255,255) , "fontsize" == 30)
pgzrun.go()