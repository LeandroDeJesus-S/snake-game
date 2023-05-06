from __future__ import annotations
from random import randint
import pygame

class Snake:
    def __init__(self) -> None:
        self.snake = [(200, 200), (210, 200), (220, 200)]
        self.snake_skin = pygame.Surface((10, 10))
        self.snake_skin.fill((255, 0, 255))
    
    def move(self, direction: str):
        """move the snake body"""
        d = {'right': self.move_right, 'left': self.move_left,
             'up': self.move_up, 'down': self.move_down}
        
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i] = (self.snake[i - 1][0], self.snake[i - 1][1])
        
        return d[direction]()
        
    def move_up(self):
        """move to up"""
        self.snake[0] = (self.snake[0][0], self.snake[0][1] - 10)
    
    def move_down(self):
        """move to down"""
        self.snake[0] = (self.snake[0][0], self.snake[0][1] + 10)
    
    def move_right(self):
        """move to right"""
        self.snake[0] = (self.snake[0][0]  + 10, self.snake[0][1])
    
    def move_left(self):
        """move to left"""
        self.snake[0] = (self.snake[0][0]  - 10, self.snake[0][1])
    
    def draw_snake(self, surface):
        """draw the snake on the screen"""
        for pos in self.snake:
            surface.blit(self.snake_skin, pos)
    
    def update_body(self):
        """add a new body part in the snake"""
        self.snake.append((0, 0))
    
    def body_collision(self):
        """verify snake collisions with their body"""
        for i in range(len(self.snake) - 1, 0, -1):
            if self.snake[0] == self.snake[i] and len(self.snake) > 3:
                return True
        return False

    def screen_borders(self, screen_x, screen_y):
        """relocate the snake when it leaves the edges of the screen"""
        x = self.snake[0][0]
        y = self.snake[0][1]
        
        if x < 0:
            self.snake[0] = (screen_x - 10, self.snake[0][1])
        elif x >= screen_x:
            self.snake[0] = (0, self.snake[0][1])
            
        if y < 0:
            self.snake[0] = (self.snake[0][0], screen_y - 10)
        elif y >= screen_y:
            self.snake[0] = (self.snake[0][0], 0)


class Food:
    def __init__(self, screen_size) -> None:
        self.screen_size = screen_size
        self.food_skin = pygame.Surface((10, 10))
        self.food_skin.fill((255, 0, 0))
        
        self.position = self.on_grid_random()

    def on_grid_random(self):
        """randomize x and y to food position"""
        x = randint(0, self.screen_size[0] - 10)
        y = randint(0, self.screen_size[1] - 10)
        
        return (x // 10 * 10, y // 10 * 10)
        
    def draw_food(self, surface):
        """draw the food on the screen"""
        surface.blit(self.food_skin, self.position)
    
    def snake_collision(self, snake_pos):
        """verify snake collision with food"""
        return snake_pos[0] == self.position[0] and snake_pos[1] == self.position[1] 


class Points:
    def __init__(self) -> None:
        self.score = 0
        self.color = pygame.Color(107, 119, 115)
        self.font_name = 'consolas'
        self.font_size = 20
        self.font_pos = [50, 50]
        
        self.font = pygame.font.SysFont(self.font_name, self.font_size)
    
    def show_points(self, window_surface):
        """show the points on the screen"""
        score_surface = self.font.render(
            f"Score: {self.score}", True, self.color
        )
        window_surface.blit(score_surface, self.font_pos)
    