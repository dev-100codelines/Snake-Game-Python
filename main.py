import random
import pygame
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
x_axis = SCREEN_WIDTH / 2
y_axis = SCREEN_HEIGHT / 2
x_axis_change = 0
y_axis_change = 0
direction = ''
snake_size = 10
snake_length = 1
snake_list = []
highest_score = 0
food_x_axis = round(random.randint(0, SCREEN_WIDTH - snake_size) / 10.0) * 10.0
food_y_axis = round(random.randint(0, SCREEN_HEIGHT - snake_size) / 10.0) * 10.0
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                break
            elif event.key == pygame.K_UP and direction != 'bottom':
                x_axis_change = 0
                y_axis_change = -snake_size
                direction = 'up'
            elif event.key == pygame.K_RIGHT and direction != 'left':
                x_axis_change = snake_size
                y_axis_change = 0
                direction = 'right'
            elif event.key == pygame.K_DOWN and direction != 'up':
                x_axis_change = 0
                y_axis_change = snake_size
                direction = 'down'
            elif event.key == pygame.K_LEFT and direction != 'right':
                x_axis_change = -snake_size
                y_axis_change = 0
                direction = 'left'
            elif event.key == pygame.K_RETURN and game_over:
                x_axis_change = 0
                y_axis_change = 0
                snake_length = 1
                snake_list = []
                x_axis = SCREEN_WIDTH / 2
                y_axis = SCREEN_HEIGHT / 2
                food_x_axis = round(random.randint(0, SCREEN_WIDTH - snake_size) / 10.0) * 10.0
                food_y_axis = round(random.randint(0, SCREEN_HEIGHT - snake_size) / 10.0) * 10.0
                direction = ''
                game_over = False
        if event.type == pygame.QUIT:
            running = False
            break
    if game_over:
        screen.fill((255, 255, 255))
        msg = pygame.font.SysFont('comicsansms', 40).render('Score: ' + str(snake_length - 1), True, (0, 0, 255))
        screen.blit(msg, [80, 80])
        if snake_length - 1 > highest_score:
            highest_score = snake_length - 1
        msg1 = pygame.font.SysFont('comicsansms', 40).render('Highest Score: ' + str(highest_score), True, (0, 0, 255))
        screen.blit(msg1, [80, 160])
    else:
        if x_axis >= SCREEN_WIDTH or y_axis >= SCREEN_HEIGHT or x_axis <= 0 or y_axis <= 0:
            game_over = True
        x_axis += x_axis_change
        y_axis += y_axis_change
        if x_axis == food_x_axis and y_axis == food_y_axis:
            food_x_axis = round(random.randint(0, SCREEN_WIDTH - snake_size) / 10.0) * 10.0
            food_y_axis = round(random.randint(0, SCREEN_HEIGHT - snake_size) / 10.0) * 10.0
            snake_length += 1
        snake_head = [x_axis, y_axis]
        snake_head.append(snake_head)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        screen.fill((255, 255, 255))
        message = pygame.font.SysFont('comicsansms', 20).render('Score: ' + str(snake_length - 1), True, (0, 0, 255))
        screen.blit(message, [0, 0])
        message1 = pygame.font.SysFont('comicsansms', 20).render('Highest Score: ' + str(highest_score), True,
                                                                 (0, 0, 255))
        screen.blit(message1, [475, 0])
        pygame.draw.rect(screen, (255, 0, 0), [food_x_axis, food_y_axis, snake_size, snake_size])
        for i in range(len(snake_list)):
            if i == len(snake_list) - 1:
                pygame.draw.rect(screen, (0, 255, 0), [snake_list[i][0], snake_list[i][1], snake_size, snake_size])
            else:
                try:
                    if snake_head == snake_list[i]:
                        game_over = True
                        break
                except RecursionError:
                    game_over = True
                    break
                pygame.draw.rect(screen, (0, 0, 0), [snake_list[i][0], snake_list[i][1], snake_size, snake_size])
    pygame.display.update()
    clock.tick(10)
