import pytest
from snake_game import Snake, food_spawn

@pytest.fixture
def snake_instance():
    return Snake([{'x': 60, 'y': 20}, {'x': 40, 'y': 20}, {'x': 20, 'y': 20}], 20, 0)

def test_move(snake_instance):
    initial_position = snake_instance.snake_pos.copy()
    snake_instance.move()
    new_position = snake_instance.snake_pos.copy()
    assert initial_position != new_position

def test_wrapping(snake_instance):
    snake_instance.snake_pos[0]['x'] = -10
    snake_instance.wrapping()
    assert snake_instance.snake_pos[0]['x'] == 600

def test_collision(snake_instance):
    assert not snake_instance.collision()  # No collision initially
    snake_instance.snake_pos[0] = snake_instance.snake_pos[1].copy()  # Create a collision
    assert snake_instance.collision(), f"Collision not detected"

def test_eat(snake_instance):
    initial_length = len(snake_instance.snake_pos)
    snake_instance.eat({'x': 40, 'y': 20})  # Simulate eating food
    new_length = len(snake_instance.snake_pos)
    assert new_length > initial_length

def test_food_spawn():
    food_pos = {'x': 0, 'y': 0}
    food_spawn()
    assert food_pos['x'] > 0
    assert food_pos['y'] > 0
