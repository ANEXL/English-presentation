from ulib import remote, display
import time
import random

# --- Game Constants ---
MATRIX_WIDTH = 16
MATRIX_HEIGHT = 16
GAME_SPEED = 0.2  # Seconds per frame (smaller is faster)

# Colors (R, G, B)
COLOR_SNAKE = (0, 20, 0)      # Green
COLOR_FOOD = (20, 0, 0)       # Red
COLOR_EMPTY = (0, 0, 0)       # Black (pixel off)
COLOR_GAME_OVER = (10, 0, 0)  # Dark red for Game Over
COLOR_Q = (255, 255, 255)     # White for 'Q' on the title screen

# --- Global Game Variables ---
snake = []                   # List of (x,y) segments for the snake
snake_direction = (1, 0)     # Current movement direction (dx, dy), default: right
food_position = None         # (x,y) position of the apple
game_over = False            # Game status
score = 0                    # Score (not displayed, but counted internally)
last_input_direction = None  # Stores the last received direction from the PC
start_game = False           # Flag to check if the game has started

# --- Game Initialization ---
def initialize_game():
    global snake, snake_direction, food_position, game_over, score
    snake = [(MATRIX_WIDTH // 2, MATRIX_HEIGHT // 2)] # Start in the middle
    snake_direction = (1, 0) # Start moving to the right
    food_position = None
    game_over = False
    score = 0
    place_food()      # Place the first apple
    title_screen()    # Display the title screen
    
def title_screen():
    """Displays the title screen."""
    # PUSH Q
    display.clear() # Clear matrix
    display.set_xy((3, 2), COLOR_FOOD)
    display.set_xy((3, 3), COLOR_FOOD)
    display.set_xy((4, 2), COLOR_FOOD)
    display.set_xy((5, 3), COLOR_FOOD)
    display.set_xy((5, 4), COLOR_FOOD)
    display.set_xy((4, 5), COLOR_FOOD)
    display.set_xy((3, 5), COLOR_FOOD)
    display.set_xy((3, 4), COLOR_FOOD)
    display.set_xy((3, 6), COLOR_FOOD)
    display.set_xy((3, 7), COLOR_FOOD)
    display.set_xy((3, 8), COLOR_FOOD)

    display.set_xy((6, 2), COLOR_SNAKE)
    display.set_xy((6, 3), COLOR_SNAKE)
    display.set_xy((6, 4), COLOR_SNAKE)
    display.set_xy((6, 5), COLOR_SNAKE)
    display.set_xy((6, 6), COLOR_SNAKE)
    display.set_xy((6, 7), COLOR_SNAKE)
    display.set_xy((6, 8), COLOR_SNAKE)
    display.set_xy((7, 8), COLOR_SNAKE)
    display.set_xy((8, 8), COLOR_SNAKE)
    display.set_xy((8, 7), COLOR_SNAKE)
    display.set_xy((8, 6), COLOR_SNAKE)
    display.set_xy((8, 5), COLOR_SNAKE)
    display.set_xy((8, 4), COLOR_SNAKE)
    display.set_xy((8, 3), COLOR_SNAKE)
    display.set_xy((8, 2), COLOR_SNAKE)

    display.set_xy((9, 2), COLOR_FOOD)
    display.set_xy((9, 3), COLOR_FOOD)
    display.set_xy((9, 4), COLOR_FOOD)
    display.set_xy((9, 5), COLOR_FOOD)
    display.set_xy((10, 5), COLOR_FOOD)
    display.set_xy((11, 5), COLOR_FOOD)
    display.set_xy((11, 6), COLOR_FOOD)
    display.set_xy((11, 7), COLOR_FOOD)
    display.set_xy((11, 8), COLOR_FOOD)
    display.set_xy((10, 8), COLOR_FOOD)
    display.set_xy((9, 8), COLOR_FOOD)
    display.set_xy((10, 2), COLOR_FOOD)
    display.set_xy((10, 3), COLOR_FOOD)

    display.set_xy((12, 2), COLOR_SNAKE)
    display.set_xy((12, 3), COLOR_SNAKE)
    display.set_xy((12, 4), COLOR_SNAKE)
    display.set_xy((12, 5), COLOR_SNAKE)
    display.set_xy((12, 6), COLOR_SNAKE)
    display.set_xy((12, 7), COLOR_SNAKE)
    display.set_xy((12, 8), COLOR_SNAKE)
    display.set_xy((13, 5), COLOR_SNAKE)
    display.set_xy((14, 2), COLOR_SNAKE)
    display.set_xy((14, 3), COLOR_SNAKE)
    display.set_xy((14, 4), COLOR_SNAKE)
    display.set_xy((14, 5), COLOR_SNAKE)
    display.set_xy((14, 6), COLOR_SNAKE)
    display.set_xy((14, 7), COLOR_SNAKE)
    display.set_xy((14, 8), COLOR_SNAKE)

    display.set_xy((6, 11), COLOR_Q)
    display.set_xy((6, 12), COLOR_Q)
    display.set_xy((6, 13), COLOR_Q)
    display.set_xy((6, 14), COLOR_Q)
    display.set_xy((7, 15), COLOR_Q)
    display.set_xy((8, 15), COLOR_Q)
    display.set_xy((9, 15), COLOR_Q)
    display.set_xy((9, 13), COLOR_Q)
    display.set_xy((10, 14), COLOR_Q)
    display.set_xy((11, 15), COLOR_Q)
    display.set_xy((11, 13), COLOR_Q)
    display.set_xy((11, 12), COLOR_Q)
    display.set_xy((11, 11), COLOR_Q)
    display.set_xy((11, 10), COLOR_Q)
    display.set_xy((10, 10), COLOR_Q)
    display.set_xy((9, 10), COLOR_Q)
    display.set_xy((8, 10), COLOR_Q)
    display.set_xy((7, 10), COLOR_Q)

    display.show() # Update matrix
    time.sleep(2) # Short pause for the title screen

def place_food():
    """Places the apple at a random, unoccupied spot."""
    global food_position
    while True:
        x = random.randint(0, MATRIX_WIDTH - 1)
        y = random.randint(0, MATRIX_HEIGHT - 1)
        if (x, y) not in snake: # Spot must not be occupied by the snake
            food_position = (x, y)
            break

def draw_game_state():
    """Draws the current game state on the LED matrix."""
    # First, clear everything
    for x_clear in range(MATRIX_WIDTH):
        for y_clear in range(MATRIX_HEIGHT):
            display.set_xy((x_clear, y_clear), COLOR_EMPTY)

    # Draw snake
    for segment in snake:
        display.set_xy(segment, COLOR_SNAKE)

    # Draw apple
    if food_position:
        display.set_xy(food_position, COLOR_FOOD)

    display.show() # Update matrix

def update_game_logic():
    """Updates the game logic for one frame."""
    global snake, snake_direction, food_position, game_over, score, last_input_direction

    if game_over:
        return

    # Adjust direction based on the last key input
    # Prevents an immediate 180-degree turn into itself
    if last_input_direction == "W" and snake_direction != (0, 1):
        snake_direction = (0, -1) # Up
    elif last_input_direction == "S" and snake_direction != (0, -1):
        snake_direction = (0, 1)  # Down
    elif last_input_direction == "A" and snake_direction != (1, 0):
        snake_direction = (-1, 0) # Left
    elif last_input_direction == "D" and snake_direction != (-1, 0):
        snake_direction = (1, 0)  # Right
    last_input_direction = None # Input has been processed

    # Calculate the next head position
    head_x, head_y = snake[0]
    next_head_x = head_x + snake_direction[0]
    next_head_y = head_y + snake_direction[1]
    next_head = (next_head_x, next_head_y)

    # Collision detection
    # 1. With walls
    if not (0 <= next_head_x < MATRIX_WIDTH and 0 <= next_head_y < MATRIX_HEIGHT):
        game_over = True
        return
    # 2. With itself
    if next_head in snake and next_head != snake[-1]:
        game_over = True
        return

    # Move snake: Add a new head
    snake.insert(0, next_head)

    # Was the apple eaten?
    if next_head == food_position:
        score += 1
        place_food() # Place a new apple
    else:
        snake.pop() # Remove the last segment (the snake moves)

# --- Remote control functions (called by ulib) ---
# These functions only set the desired direction
def remote_left(c):
    global last_input_direction
    last_input_direction = "A"

def remote_right(c):
    global last_input_direction
    last_input_direction = "D"

def remote_up(c):
    global last_input_direction
    last_input_direction = "W"

def remote_down(c):
    global last_input_direction
    last_input_direction = "S"

def remote_q_pressed(c):
    global start_game
    start_game = True

# --- Key bindings and listener start ---
remote.bind_key("A", remote_left)
remote.bind_key("D", remote_right)
remote.bind_key("W", remote_up)
remote.bind_key("S", remote_down)
remote.bind_key("LEFT", remote_left)
remote.bind_key("RIGHT", remote_right)
remote.bind_key("UP", remote_up)
remote.bind_key("DOWN", remote_down)
remote.bind_key("Q", remote_q_pressed) # Starts the game
remote.listen() # Starts the UDP server to listen for your PC inputs

# --- Main game loop ---
if __name__ == "__main__":
    initialize_game() # Initialize the game at start

    while not start_game:
        time.sleep(0.1)

    while True:
        if not game_over:
            update_game_logic()   # Update game logic
            draw_game_state()     # Draw game on matrix
            time.sleep(GAME_SPEED) # Wait time for game speed
        else:
            # Game over display (blinking)
            for x_go in range(MATRIX_WIDTH):
                for y_go in range(MATRIX_HEIGHT):
                    display.set_xy((x_go, y_go), COLOR_GAME_OVER if int(time.time() * 2) % 2 == 0 else COLOR_EMPTY)
            display.show()
            time.sleep(0.5) # Slower blinking
            # The script must be manually restarted after a Game Over
            # to start a new game.
