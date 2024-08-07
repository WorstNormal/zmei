import pygame
import random
import time
import sys


def draw_line(screen, size):
    for i in range(0, size[1]+ 1, 50):
        pygame.draw.line(screen, (100,100,100), [0, i], [size[0], i], width=1)
    for i in range(0, size[0] + 1, 50):
        pygame.draw.line(screen, (100,100,100), [i, 0], [i, size[1]], width=1)

def draw_snake(screen, list, width, height):
    for i in range(0, height * 50, 50):
        for j in range(0, width * 50, 50):
            match list[i // 50][j // 50]:
                case 0:
                    pygame.draw.polygon(screen, pygame.Color("black"),
                                    [(j + 1, i + 1), (j + 49, i + 1),
                                     (j + 49, i + 49), (j + 1, i + 49)]
                                    , 0)
                case 1:
                    pygame.draw.polygon(screen, (0,150,0),
                                    [(j + 1, i + 1), (j + 49, i + 1),
                                     (j + 49, i + 49), (j + 1, i + 49)]
                                    , 0)
                case 2:
                    pygame.draw.polygon(screen, (0,150,0),
                                        [(j + 1, i + 1), (j + 49, i + 1),
                                         (j + 49, i + 49), (j + 1, i + 49)]
                                        , 0)
                    pygame.draw.polygon(screen, pygame.Color("black"),
                                        [(j + 20, i + 20), (j + 20, i + 30)
                                            , (j + 30, i + 30) , (j + 30, i + 20)]
                                        , 0)
                case 3:
                    pygame.draw.circle(screen, (155, 31, 42), (j + 25, i + 25), 24)

def predict(playground, move_set, apple, head, size):
    min_step = [10000, [0, 0]]
    head_y, head_x = head[0], head[1]
    size_x, size_y = size[0], size[1]
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            if abs(x) ^ abs(y):
                if 0 <= head_x + x < size_x and 0 <= head_y + y < size_y:
                    if (move_set[head_y + y][head_x + x] - move_set[head_y][head_x] == 1 or
                            move_set[head_y + y][head_x + x] - move_set[head_y][head_x] == (size[0] * size[1] - 1) * -1):
                        min_step = [0, [x, y]]
    return min_step[1]

def move_set_create(move_set_local, n, coord, size):
    global move_set_best, max_n, flag_create
    n += 1
    size_x, size_y = size[0], size[1]
    coord_y, coord_x = coord[0], coord[1]
    move_set_change = move_set_local[::]
    if coord_y + coord_x == 1 and ((n == size_y * size_x + 1) or
            (size_x % 2 == 1 and size_y % 2 == 1 and size_y * size_x == n)):
        move_set_best = move_set_local.copy()
        max_n = n
        flag_create = False
    for x in range(1, -2, -1):
        for y in range(-1, 2, 1):
            if abs(x) ^ abs(y):
                if (0 <= coord_x + x < size_x and 0 <= coord_y + y < size_y and move_set_change[coord_y + y][coord_x + x] == 0
                        and flag_create):
                    move_set_change[coord_y + y][coord_x + x] = n
                    move_set_create(move_set_change, n, [coord_y + y, coord_x + x], size)
                    if flag_create:
                        move_set_change[coord_y + y][coord_x + x] = 0







if __name__=='__main__':
    start_pos = [1, [0, 2]]
    width, height = 10, 10
    timer = 0.01


    playground = []
    for i in range(height):
        playground.append([0] * width)
    move_set = []
    for i in range(height):
        move_set.append([0] * width)
    max_n = 0
    move_set[0][0] = 1
    flag_create = True
    move_set_best = []
    move_set_create(move_set, 1, [0, 0], [width, height])
    print(move_set_best)
    last_move = [0, 2]
    head_snake = [0, 2]
    pygame.init()
    playground[0][0] = 1
    playground[0][1] = 1
    playground[0][2] = 2
    apple_y, apple_x = 0, 0
    while playground[apple_y][apple_x] == 1 or playground[apple_y][apple_x] == 2:
        apple_y, apple_x = random.randint(0, height - 1), random.randint(0, width - 1)
    playground[apple_y][apple_x] = 3
    list_snake = [[0, 2], [0, 1], [0, 0]]
    running = True
    move_x = 1
    move_y = 0
    size = (width * 50, height * 50)
    screen = pygame.display.set_mode(size)
    draw_line(screen, size)
    draw_snake(screen, playground, width, height)
    step_time = time.time()
    control = "auto"
    flag = True
    while running:
        if flag:
            match control:
                case "manual":
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        if event.type == pygame.KEYDOWN and flag:
                            keys = pygame.key.get_pressed()
                            if keys[pygame.K_w] and [move_x, move_y] != [0, 1]:
                                move_x = 0
                                move_y = -1
                                flag = False
                            elif keys[pygame.K_s] and [move_x, move_y] != [0, -1]:
                                move_x = 0
                                move_y = 1
                                flag = False
                            elif keys[pygame.K_a] and [move_x, move_y] != [1, 0]:
                                move_x = -1
                                move_y = 0
                                flag = False
                            elif keys[pygame.K_d] and [move_x, move_y] != [-1, 0]:
                                move_x = 1
                                move_y = 0
                                flag = False
                case "auto":
                    move_x, move_y = predict(playground, move_set, [apple_y, apple_x], head_snake, [width, height])
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                    flag = False
        if time.time() - step_time >= timer:
            flag = True
            step_time = time.time()
            if head_snake[0] + move_y < 0 or head_snake[1] + move_x < 0 or head_snake[0] + move_y == height or head_snake[1] + move_x == width:
                print("Поражение")
                exit()
            if playground[head_snake[0] + move_y][head_snake[1] + move_x] == 3:
                f = True
                for i in playground:
                    f *= all(i)
                if f:
                    print("Победа!")
                    exit()
                playground[head_snake[0]][head_snake[1]] = 1
                playground[head_snake[0 ] + move_y][head_snake[1] + move_x] = 2
                while playground[apple_y][apple_x] == 1 or playground[apple_y][apple_x] == 2:
                    apple_y, apple_x = random.randint(0, height - 1), random.randint(0, width - 1)
                playground[apple_y][apple_x] = 3
            elif (playground[head_snake[0] + move_y][head_snake[1] + move_x] == 1
                  and list_snake[-1] != [head_snake[0] + move_y, head_snake[1] + move_x]):
                print("Поражение")
                exit()
            else:
                k = list_snake.pop()
                playground[k[0]][k[1]] = 0
                playground[head_snake[0]][head_snake[1]] = 1
                playground[head_snake[0] + move_y][head_snake[1] + move_x] = 2
            head_snake[0], head_snake[1] = head_snake[0] + move_y, head_snake[1] + move_x
            list_snake = [[head_snake[0], head_snake[1]]] + list_snake
        draw_line(screen, size)
        draw_snake(screen, playground, width, height)
        pygame.display.update()
    pygame.quit()
    