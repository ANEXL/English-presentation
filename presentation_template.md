<!--
author:   Anton Kalch, Alexander Felber, Tristan Kaestner

email:    anton.kalch@gmail.com

version:  0.0.1

language: en

comment:  english LED-box presentation
-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://raw.githubusercontent.com/ANEXL/english-presentation/main/presentation_template.md)

# Table of contents

1. Object of desire
2. Added value from this presentation
3. Scope of the presentation
4. Inspiration
5. Background Info / Technical Details
6. Code

 * Big picture
  
 * Important code snippets

7. Coding process

 * How did you code? Vibe? GitHub?
    
 * What did you already know (and from where do you know it) and what did you have to learn to complete the project?

8. The show/game. Demo and description
9. Conclusion. What did we get from taking part in this challenge?
10. Final thought/take-home message

## 1. Object of desire

<p align="center">
  <img src="englisch.png" width="850"/>
</p>

## 2. Added value from this presentation

 * basic python knowledge
    
 * how to work with libraries
    
 * insights into game logic and design

## 3. Scope of the presentation

 * brief snake history
    
 * explaining our code and the thoughts behind it
    
 * the problems we had along the way

## 4. Inspiration

 * initial tetris idea was abandoned (after concerns from Bjoern
    
 * inspiration from [onlinespiele-sammlung.de](onlinespiele-sammlung.de)

## 5. Background Knowledge

 * basic programming knowledge
    
 * ability to read (optional)

## 6. Code

                              {{1-2}}
*******************************************************************************

```python
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
```
*******************************************************************************

                              {{2-3}}
*******************************************************************************
```python
def initialize_game():
    global snake, snake_direction, food_position, game_over, score
    snake = [(MATRIX_WIDTH // 2, MATRIX_HEIGHT // 2)] # Start in the middle
    snake_direction = (1, 0) # Start moving to the right
    food_position = None
    game_over = False
    score = 0
    place_food()      # Place the first apple
    title_screen()    # Display the title screen
```
*******************************************************************************

                              {{3-4}}
*******************************************************************************
```python
def place_food():
    """Places the apple at a random, unoccupied spot."""
    global food_position
    while True:
        x = random.randint(0, MATRIX_WIDTH - 1)
        y = random.randint(0, MATRIX_HEIGHT - 1)
        if (x, y) not in snake: # Spot must not be occupied by the snake
            food_position = (x, y)
            break
```
*******************************************************************************

                              {{4-5}}
*******************************************************************************
```python
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
```
*******************************************************************************

                              {{5-6}}
*******************************************************************************
```python
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
```
*******************************************************************************

                              {{6-7}}
*******************************************************************************
```python
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
```
*******************************************************************************

## 7. Coding process
  1. Prototype in C#
  2. First Python prototype with pygame library
  3. Final solution with our own functions

-------------------------------------------------------------------------------
                                {{1-2}}
*******************************************************************************
  1. Prototype in C#

  ```C#
  class Program
  {
    static void Main(string[] args)
    {
        Level myLevel = new Level(); // Level construction
        Player myPlayer = new Player(); // Player construction

        Thread thd1 = new Thread(new ThreadStart(Loop1));//Zwei parallele methoden initilaisieren
        Thread thd2 = new Thread(new ThreadStart(Loop2));
        Thread thd3 = new Thread(new ThreadStart(Loop3));

        thd1.Start(); thd2.Start(); thd3.Start();
        thd1.Join(); thd2.Join(); thd3.Join();

        void Loop1()
        {
            myLevel.RefreshArea(myPlayer.headpos[0], myPlayer.headpos[1], myPlayer.tailpos, myPlayer.length);
            //int s = 0;
            while (true)
            {
                myPlayer.MoveTail();

                switch (myPlayer.headdir)
                {
                    case 'd': myPlayer.headpos[1]++; break;
                    case 'u': myPlayer.headpos[1]--; break;
                    case 'l': myPlayer.headpos[0]--; break;
                    case 'r': myPlayer.headpos[0]++; break;
                }

                    myPlayer.CollDet(myLevel.Area);
               
                myLevel.RefreshArea(myPlayer.headpos[0], myPlayer.headpos[1], myPlayer.tailpos, myPlayer.length);

                Console.Clear();
                myLevel.PrintArea(myLevel.Area);
                System.Threading.Thread.Sleep(250);
            }
        }

        void Loop2()
        {
            while (true)
            {
                switch (Console.ReadKey(true).Key)//checkt tatstatur input
                {
                    case ConsoleKey.UpArrow: myPlayer.headdir = 'u'; break;  //pfeiltatsen setzen richtung
                    case ConsoleKey.DownArrow: myPlayer.headdir = 'd'; break;
                    case ConsoleKey.LeftArrow: myPlayer.headdir = 'l'; break;
                    case ConsoleKey.RightArrow: myPlayer.headdir = 'r'; break;
                    case ConsoleKey.Escape: Environment.Exit(0); break;
                }
            }
        }
        
        void Loop3()
        {
            while (true)
            {
                System.Threading.Thread.Sleep(1000);
                myPlayer.length++;
            }
        }
        
    }
  }
  ```
*******************************************************************************

                                {{2-3}}
*******************************************************************************
  2. First Python prototype with pygame library

  ```python
  def main():
    global richtung
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    snake_position = [(5, 5), (4, 5), (3, 5)]
    richtung = (1, 0)
    apple_position = äpfel_generieren(snake_position, (GRID_WIDTH, GRID_HEIGHT))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            richtung = steuerung_schlange(event, richtung)

        # Bewegung
        new_head = (snake_position[0][0] + richtung[0], snake_position[0][1] + richtung[1])
        snake_position.insert(0, new_head)

        # Apfel gegessen?
        if new_head == apple_position:
            apple_position = äpfel_generieren(snake_position, (GRID_WIDTH, GRID_HEIGHT))
        else:
            snake_position.pop()

        if kollision_pruefung(snake_position, (GRID_WIDTH, GRID_HEIGHT)):
            running = False

        # Zeichnen mit pygame
        screen.fill((0, 0, 0))
        zeichne_schlange(screen, snake_position)
        zeichne_apfel(screen, apple_position)
        pygame.display.flip()
        clock.tick(10)

        # Zeichnen auf der LED-Matrix
        display.fill((0, 0, 0))
        for segment in snake_position:
            display.set_xy(segment[0], segment[1], (0, 255, 0)) 
        display.set_xy(apple_position, (255, 0, 0))
        display.show()

    pygame.quit()
  ```
*******************************************************************************

## 8. The show/game. Demo and description

<p align="center">
  <img src="logo.png" width="600"/>
</p>

## 9. Conclusion. What did we get from taking part in this challenge?

 * training to work as a team
   
 * new Python skills
   
 * learned to work with inputs from remote controllers
   
## 10. Final thought/take-home message

 * It's easier than it looks

 
