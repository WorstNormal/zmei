import pygame
import random
import time
def drawline(screen, size):
    for i in range(0, size[1]+ 1, 50):
        pygame.draw.line(screen, pygame.Color('white'), [0, i], [size[0], i], width=1)
    for i in range(0, size[0] + 1, 50):
        pygame.draw.line(screen, pygame.Color('white'), [i, 0], [i, size[1]], width=1)
    
def drawzmei(screen, size, list):
    for i in range(h // 50):
        for j in range(w // 50):
            if list[i][j] == 0:
                pygame.draw.polygon(screen, pygame.Color("black"),
                                    [(j * 50 + 1, i * 50 + 1), (j * 50 + 49, i * 50 + 1),
                                     (j * 50 + 49, i * 50 + 49), (j * 50 + 1, i * 50 + 49)]
                                    , 0)
            if list[i][j] == 1:
                pygame.draw.polygon(screen, pygame.Color("green"),
                                    [(j * 50 + 1, i * 50 + 1), (j * 50 + 49, i * 50 + 1),
                                     (j * 50 + 49, i * 50 + 49), (j * 50 + 1, i * 50 + 49)]
                                    , 0)
            if list[i][j] == 2:
                pygame.draw.polygon(screen, pygame.Color("green"),
                                    [(j * 50 + 1, i * 50 + 1), (j * 50 + 49, i * 50 + 1),
                                     (j * 50 + 49, i * 50 + 49), (j * 50 + 1, i * 50 + 49)]
                                    , 0)
                pygame.draw.polygon(screen, pygame.Color("black"),
                                    [(g[1] * 50 + 20, i * 50 + 20), (j * 50 + 20, i * 50 + 30)
                                        , (j * 50 + 30, i * 50 + 30) , (j * 50 + 30, i * 50 + 20)]
                                    , 0)
            if list[i][j] == 3:
                pygame.draw.circle(screen, pygame.Color("red"), (j * 50 + 25, i * 50 + 25), 24)
                
                
if __name__ == '__main__':
    pygame.init()
    w, h = 300, 300 #map(int, input().split())
    size = w, h
    list = []
    for i in range(h // 50):
        list.append([0] * (w // 50))
    g = [0, 2]
    list[0][0] = 1
    list[0][1] = 1
    list[0][2] = 2
    i1, j1 = 0, 0
    while list[i1][j1] == 1 or list[i1][j1] == 2:
        i1, j1 = random.randint(0, h // 50 - 1), random.randint(0, w // 50 - 1)
    list[i1][j1] = 3
    lis_z = [[0, 2], [0, 1], [0, 0]]
    screen = pygame.display.set_mode(size)
    running = True
    x = 0
    y = 0
    drawline(screen, size)
    drawzmei(screen, size, list)
    while running:
        t = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    x = 0
                    y = -1
                    t = True
                elif keys[pygame.K_s]:
                    x = 0
                    y = 1
                    t = True
                elif keys[pygame.K_a]:
                    x = -1
                    y = 0
                    t = True
                elif keys[pygame.K_d]:
                    x = 1
                    y = 0
                    t = True
                print(x, y)
        if t:
            t = False
            if g[0] + y < 0 or g[1] + x < 0 or g[0] + y == h // 50 or g[1] + x == w // 50:
                print("Поражение")
                exit()
            if list[g[0] + y][g[1] + x] == 3:
                f = True
                for i in list:
                    f *= all(i)
                if f:
                    print("Победа!")
                    exit()
                list[g[0]][g[1]] = 1
                list[g[0] + y][g[1] + x] = 2
                while list[i1][j1] == 1 or list[i1][j1] == 2:
                    i1, j1 = random.randint(0, h // 50 - 1), random.randint(0, w // 50 - 1)
                list[i1][j1] = 3
            elif list[g[0] + y][g[1] + x] == 1:
                print("Поражение")
                exit()
            else:
                list[g[0]][g[1]] = 1
                list[g[0] + y][g[1] + x] = 2
                k = lis_z.pop()
                list[k[0]][k[1]] = 0
            g[0], g[1] = g[0] + y, g[1] + x
            lis_z = [[g[0], g[1]]] + lis_z
            print(lis_z)
            for i in list:
                print(i)
        drawline(screen, size)
        drawzmei(screen, size, list)
        pygame.display.update()
    pygame.quit()
    