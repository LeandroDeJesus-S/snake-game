import pygame, sys
from objects import Snake, Points, Food

pygame.init()
    
screen_size = screen_x, screen_y = 1200, 600
fps = pygame.time.Clock()

window = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Snake Game')

snake = Snake()
food = Food(screen_size)
points = Points()

direction = 'right'
while True:
    window.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'down':
                direction = 'up'
            
            elif event.key == pygame.K_DOWN and direction != 'up':
                direction = 'down'
                
            elif event.key == pygame.K_RIGHT and direction != 'left':
                direction = 'right'
                
            elif event.key == pygame.K_LEFT and direction != 'right':
                direction = 'left'

    snake.move(direction)
    snake.screen_borders(*screen_size)
    
    snake.draw_snake(window)
    food.draw_food(window)
    points.show_points(window)
    
    if food.snake_collision(snake.snake[0]):
        points.score += 1
        food.position = food.on_grid_random()
        snake.update_body()
    
    if snake.body_collision():
        points.score = 0
        snake.__init__()
        food.__init__(screen_size)
    

    pygame.display.update()
    fps.tick(25)
