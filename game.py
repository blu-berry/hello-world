import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Display")
clock = pygame.time.Clock()

exit = False
x = 150
y = 150



pygame.draw.circle(gameDisplay, (200, 200, 200), (x, y), 15, 0)

while not exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True


        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            y -= 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            y += 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            x -= 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            x += 1

        print(x, y)
        pygame.draw.circle(gameDisplay, (200, 200, 200), (x, y), 15, 0)



    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
