import pygame


width = 1024
height = 768


pygame.init()
gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption("Display")
clock = pygame.time.Clock()
victoryImg = pygame.image.load("victory.jpg")

WIN = False
exit = False
x = 512
y = 758

def map():
    gameDisplay.fill((42, 44, 48))
    pygame.draw.rect(gameDisplay, (255, 0, 0), (492, 0, 40, 40), 0)



map()

def win():
    gameDisplay.fill((42, 44, 48))
    gameDisplay.blit(victoryImg, (212, 84))

pygame.draw.circle(gameDisplay, (40, 119, 252), (x, y), 10, 5)

pygame.key.set_repeat(10, 10)

while not exit and not WIN:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            x -= 3
            map()
            if x < 10:
                x = 10
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            x += 3
            map()
            if x > (width - 10):
                x = (width - 10)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            y -= 3
            map()
            if y < 10:
                y = 10
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            y += 3
            map()
            if y > (height - 10):
                y = (height - 10)
        if y < 40:
            if x < 532 and x > 492:
                win()
                WIN = True


        print(x, y)
        pygame.draw.circle(gameDisplay, (40, 119, 252), (x, y), 10, 5)



    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
