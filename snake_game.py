import pygame
import random
import sys

# Variable Initialization
snake_pos = [{'x': 60, 'y': 20}, {'x': 40, 'y': 20}, {'x': 20, 'y': 20}]
snake_size = 20

food_pos = {'x': 280, 'y': 280}

grid_size = 20

class Snake:
    def __init__(self, snake_pos, x_dir, y_dir):
        self.snake_pos = snake_pos
        self.x_dir = x_dir
        self.y_dir = y_dir

    def move(self):
        # Snake Move
        self.snake_pos.insert(0, {'x': self.snake_pos[0]['x'] + self.x_dir, 'y': self.snake_pos[0]['y'] + self.y_dir})
        self.snake_pos.pop()
        
    def wrapping(self):
        # Snake wrapping
        if self.snake_pos[0]['x'] < 0:
            self.snake_pos[0]['x'] = 600
        elif snake_pos[0]['x'] > 600:
            self.snake_pos[0]['x'] = 0
        elif snake_pos[0]['y'] < 0:
            self.snake_pos[0]['y'] = 600
        elif snake_pos[0]['y'] > 600:
            self.snake_pos[0]['y'] = 0
    
    def collision(self):
        # Snake Collision
        if self.snake_pos[0] in self.snake_pos[1:]:
            sys.exit()
    
    def eat(self, food_pos):
        if self.snake_pos[0]['x'] == food_pos['x'] and self.snake_pos[0]['y'] == food_pos['y']:
            self.snake_pos.append({'x': self.snake_pos[-1]['x'], 'y': self.snake_pos[-1]['y']})
            food_spawn()

    def update(self, food_pos):
        self.move()
        self.wrapping()
        self.collision()
        self.eat(food_pos)
    
        

def main():
    global screen
    #Pygame Setup
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Snake Game')
    #food_spawn()

    snake = Snake(snake_pos,20,0)
    

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check for key presses
            if event.type == pygame.KEYDOWN:
                key_press(event, snake)
        
        snake.update(food_pos)

        # Draw
        draw()

        # Update
        pygame.display.update()

        # FPS
        clock = pygame.time.Clock()
        clock.tick(15)

        
def key_press(event, snake):

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            snake.x_dir = 0
            snake.y_dir = -20
        elif event.key == pygame.K_s:
            snake.x_dir = 0
            snake.y_dir = 20
        elif event.key == pygame.K_a:
            snake.x_dir = -20
            snake.y_dir = 0
        elif event.key == pygame.K_d:
            snake.x_dir = 20
            snake.y_dir = 0

def food_spawn():
    global food_pos
    food_pos['x'] = random.randint(1, 29) * 20
    food_pos['y'] = random.randint(1, 29) * 20

        

def draw():
    # Draw Background
    screen.fill((0, 0, 0))

    # Draw Food
    pygame.draw.rect(screen, (255, 0, 0), (food_pos['x'], food_pos['y'], snake_size, snake_size))

    # Draw Snake
    for pos in snake_pos:
         pygame.draw.rect(screen, (0, 255, 0), (pos['x'], pos['y'], snake_size, snake_size))

    #Draw Grid 
    for x in range(30):
        for y in range(30):
            rect = pygame.Rect(x*grid_size, y*grid_size, grid_size, grid_size)
            pygame.draw.rect(screen, (5, 5, 5), rect, 1)

if __name__ == "__main__":
    main()