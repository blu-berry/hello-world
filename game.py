import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Display")
clock = pygame.time.Clock()
gameDisplay.fill((42, 44, 48))

exit = False
x = 150
y = 150



pygame.draw.circle(gameDisplay, (40, 119, 252), (x, y), 10, 5)

pygame.key.set_repeat(10, 10)

while not exit:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            x -= 3
            gameDisplay.fill((42, 44, 48))
            if x < 0:
                x = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            x += 3
            gameDisplay.fill((42, 44, 48))
            if x > 800:
                x = 800
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            y -= 3
            gameDisplay.fill((42, 44, 48))
            if y < 0:
                y = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            y += 3
            gameDisplay.fill((42, 44, 48))
            if y > 600:
                y = 600

        print(x, y)
        pygame.draw.circle(gameDisplay, (40, 119, 252), (x, y), 10, 5)



    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
