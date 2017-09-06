import pygame
import math
import pickle

# display resolution
width = 1024
height = 768

# display, imports and FPS setup
pygame.init()
gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption("Display")
clock = pygame.time.Clock()
victoryImg = pygame.image.load("win.png")

exit = False

# starting position of player
x = 512
y = 758

# basic level
def map():
    gameDisplay.fill((42, 44, 48))
    pygame.draw.rect(gameDisplay, (255, 0, 0), (492, 0, 40, 40), 0)

# victory screen
def win():
    gameDisplay.fill((42, 44, 48))
    gameDisplay.blit(victoryImg, (362, 134))

# maps list and map counter
maps_list = [map, win]
map_num = 0

# save and load system
load_times = 0


def save_progress(map_position):
    pickle.dump(map_position, open("save.p", "wb"))

def load_progress(load_limit):
    if load_limit == 0:
        map_num = pickle.load(open("save.p", "rb"))
        return map_num
    load_limit += 1
    print("file loaded")


# bullet starting positions
bullet1_x = 1024
bullet1_y = 512
bullet2_x = 0
bullet2_y = 128
bullet3_x = 0
bullet3_y = 256
bullet4_x = 1024
bullet4_y = 700

# bullet positions lists
x_axis = [bullet1_x, bullet2_x, bullet3_x, bullet4_x]
y_axis = [bullet1_y, bullet2_y, bullet3_y, bullet4_y]


map()

# drawing of all basic objects
pygame.draw.circle(gameDisplay, (40, 119, 252), (x, y), 10, 5)
pygame.draw.circle(gameDisplay, (255, 255, 255), (bullet1_x, bullet1_y), 2, 0)
pygame.draw.circle(gameDisplay, (255, 255, 255), (bullet2_x, bullet2_y), 2, 0)
pygame.draw.circle(gameDisplay, (255, 255, 255), (bullet3_x, bullet3_y), 2, 0)
pygame.draw.circle(gameDisplay, (255, 255, 255), (bullet4_x, bullet4_y), 2, 0)

pygame.key.set_repeat(10, 10)

while not exit:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

        # save and load logic
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            save_progress(map_num)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
            map_num = load_progress(load_times)

        # movement logic
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            x -= 2
            maps_list[map_num]()
            if x < 10:
                x = 10
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            x += 2
            maps_list[map_num]()
            if x > (width - 10):
                x = (width - 10)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            y -= 2
            maps_list[map_num]()
            if y < 10:
                y = 10
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            y += 2
            maps_list[map_num]()
            if y > (height - 10):
                y = (height - 10)


# map change and finish logic
    maps_list[map_num]()

    pygame.draw.circle(gameDisplay, (40, 119, 252), (x, y), 10, 5)

    if y < 40:
        if x < 532 and x > 492:
            map_num += 1
            if map_num >= len(maps_list):
                map_num = (len(maps_list) - 1)
            x = 512
            y = 758

    # bullets logic
    if map_num == 0:
        # bullet1
        pygame.draw.circle(gameDisplay, (255, 255, 255), (bullet1_x, bullet1_y), 2, 0)
        bullet1_x -= 5
        if bullet1_x < 0:
            bullet1_x = width
        # bullet2
        pygame.draw.circle(gameDisplay, (255, 255, 255), (bullet2_x, bullet2_y), 2, 0)
        bullet2_x += 7
        if bullet2_x > width:
            bullet2_x = 0
        # bullet3
        pygame.draw.circle(gameDisplay, (255, 255, 255), (bullet3_x, bullet3_y), 2, 0)
        bullet3_x += 1
        if bullet3_x > width:
            bullet3_x = 0
        # bullet4
        pygame.draw.circle(gameDisplay, (255, 255, 255), (bullet4_x, bullet4_y), 2, 0)
        bullet4_x -= 3
        if bullet4_x < 0:
            bullet4_x = width

# collision detection
    if (math.sqrt(((x - bullet1_x)**2) + ((y - bullet1_y)**2))) < 12:
        x = 512
        y = 758
    if (math.sqrt(((x - bullet2_x)**2) + ((y - bullet2_y)**2))) < 12:
        x = 512
        y = 758
    if (math.sqrt(((x - bullet3_x)**2) + ((y - bullet3_y)**2))) < 12:
        x = 512
        y = 758
    if (math.sqrt(((x - bullet4_x)**2) + ((y - bullet4_y)**2))) < 12:
        x = 512
        y = 758


# display update and FPS
    pygame.display.update()
    clock.tick(500)

pygame.quit()
quit()
