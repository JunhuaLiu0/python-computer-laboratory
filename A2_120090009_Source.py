# Use module turtle to make a snake game
import random
import turtle
import time
from turtle import Screen

global g_game_over, g_state_running, g_switch, g_start_time
global g_foods, g_switch, g_time_passed, g_contact
g_game_over = False  # Sign the completeness of game
g_state_running = True  # Judge whether the game is paused
g_contact = 0  # Count the contact between snake and monster
snake = [(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0, 0)]  # the coordinate of body and head.
turtle.shape("square")
g_monster = (-120, -120)  # the coordinate of monster.
head = snake[-1]
turtle.penup
g_switch = True  # The sign determines the direction of monster.

"""Place the monster on a random position
Keep a fair distance from the snake
"""


def random_monster():
    while True:
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        if (x > 150 or x < -150) and (y > 150 or y < -150):
            return (x, y)
            break


g_monster = random_monster()

# initalize the wide,height and title of screen.
def install_screen(w=660, h=740):
    screen = Screen()
    screen.setup(w, h)
    screen.title("Joshua's Gluttonous Snake with a purple monster")
    screen.tracer(0)
    return screen


# Pause the snake, but the monster continues.
def pause():
    global g_state_running
    g_state_running = not g_state_running


# Print the instruction for beginners.
def instruction():
    turtle.penup()
    turtle.goto(-240, 120)
    turtle.write(
        """Welcome to Joshua's version of snake game...

You are going to use the 4 arrow keys to move the snake
around the screen, trying to consume all the food items 
before the monster catches you...

Click anywhere on the screen to start the game.
Have fun and relax!""",
        font="black 11 normal",
    )


# Draw the frame of the screen
def frame():
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-250, -250)  # Draw the margin of screen
    turtle.pendown()
    turtle.pencolor("black")
    for i in range(4):
        turtle.forward(500)
        turtle.left(90)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-250, 250)  # Draw the margin of upper area
    turtle.pendown()
    turtle.pencolor("black")
    for i in range(1, 5):
        if i % 2 == 1:
            n = 500
        elif i % 2 == 0:
            n = 80
        turtle.forward(n)
        turtle.left(90)


# Build the content of upper status area
def board():
    global g_state_running, g_time_passed, g_contact
    hint.clear()
    hint.hideturtle()
    hint.penup()
    hint.goto(-200, 280)
    hint.write(  # Sign the passed time
        f"Time: {g_time_passed}", align="left", font="Arial 16 bold"
    )
    hint.goto(-70, 280)
    hint.write(  # Sign the number of contact
        f"Contact: {g_contact}", align="left", font="Arial 16 bold"
    )
    hint.goto(60, 280)
    if g_state_running == True:  # Sign the moving state of snake
        if aim == [0, 0]:
            hint.write(f"Motion: Paused", align="left", font="Arial 16 bold")
        if aim == [0, 20]:
            hint.write(f"Motion: Up", align="left", font="Arial 16 bold")
        if aim == [0, -20]:
            hint.write(f"Motion: Down", align="left", font="Arial 16 bold")
        if aim == [20, 0]:
            hint.write(f"Motion: Right", align="left", font="Arial 16 bold")
        if aim == [-20, 0]:
            hint.write(f"Motion: Left", align="left", font="Arial 16 bold")
    if g_state_running == False:
        hint.write(f"Motion: Paused", align="left", font="Arial 16 bold")


aim = [0, 0]  # Snake moves upward initially.

# Change the moving direction of snake
def direction(x, y):
    global g_state_running
    aim[0] = x
    aim[1] = y
    if g_state_running == False:
        g_state_running = True


# Generate and return a list with the value and random coordinate of food.
def set_food():
    global g_foods
    coordinate = []
    Foods = []
    i = 1
    value = 0
    while i <= 9:
        while True:
            x = (
                random.randint(-11, 11)  # Make sure the snake can eat all food items.
            ) * 20
            y = random.randint(-11, 11) * 20
            if (x, y) not in coordinate:  # Make sure the foods are not the same
                break
        coordinate.append((x, y))
        value += 1
        food = (x, y, value)
        Foods.append(food)
        i += 1
    return Foods


g_foods = set_food()

# Displayed foods within the motion area in random locations.
def get_food():
    for (x, y, value) in g_foods:
        food.hideturtle()
        food.color("blue")
        food.penup()
        food.goto(
            x, y - 9  # Place the number on the same level as the center of square.
        )
        food.write(value)


# Draw the snake
def get_snake(snake):
    i = 0
    turtle.shape("square")
    turtle.penup()
    turtle.color("blue", "black")
    while i <= len(snake) - 1:
        turtle.goto(snake[i][0], snake[i][1])
        turtle.stamp()
        i += 1
        if i == len(snake) - 1:  # The head of snake is distinguished from body
            turtle.color("red")


# Draw the monster
def get_monster(g_monster):
    turtle.color("purple")
    turtle.shape("square")
    turtle.penup()
    turtle.goto(g_monster)
    turtle.stamp()


# Monitor the contact between snake and monster
def monitor_contacted():
    for i in snake:
        if -20 <= g_monster[0] - i[0] <= 20 and -20 <= g_monster[1] - i[1] <= 20:
            return True


speed_monster = 200
speed_snake = 200

"""Monster moves toward the head of snake.
Change the moving direction according to the snake
The speed of monster is random.
"""


def move_monster():
    global g_switch, speed_monster, g_game_over, g_monster
    aim_monster = (20, 20)  # The vertical and horizontal speed of monster
    if g_game_over == False:
        if (-40 < g_monster[0] - snake[-1][0] < 40) and (
            -40 < g_monster[1] - snake[-1][1] < 40
        ):  # Do alternate horizontal and vertical motion when the monster is close
            if g_switch == True:
                if g_monster[0] < snake[-1][0]:
                    g_monster = (g_monster[0] + aim_monster[0], g_monster[1])
                elif g_monster[0] > snake[-1][0]:
                    g_monster = (g_monster[0] - aim_monster[0], g_monster[1])
            if g_switch == False:
                if g_monster[1] < snake[-1][1]:
                    g_monster = (g_monster[0], g_monster[1] + aim_monster[1])
                elif g_monster[1] > snake[-1][1]:
                    g_monster = (g_monster[0], g_monster[1] - aim_monster[1])
            g_switch = not g_switch  # Switch the direction next time
        elif (
            -40 < g_monster[0] - snake[-1][0] < 40
        ):  # move vertically when the horizontal distance is short
            if g_monster[1] < snake[-1][1]:
                g_monster = (g_monster[0], g_monster[1] + aim_monster[1])
            elif g_monster[1] > snake[-1][1]:
                g_monster = (g_monster[0], g_monster[1] - aim_monster[1])
        elif (  # move horizontally when the vertical distance is short
            -40 < g_monster[1] - snake[-1][1] < 40
        ):
            if g_monster[0] < snake[-1][0]:
                g_monster = (g_monster[0] + aim_monster[0], g_monster[1])
            elif g_monster[0] > snake[-1][0]:
                g_monster = (g_monster[0] - aim_monster[0], g_monster[1])
        else:  # Do alternate horizontal and vertical motion when the monster is far
            if g_switch == True:
                if g_monster[0] < snake[-1][0]:
                    g_monster = (g_monster[0] + aim_monster[0], g_monster[1])
                elif g_monster[0] > snake[-1][0]:
                    g_monster = (g_monster[0] - aim_monster[0], g_monster[1])
            if g_switch == False:
                if g_monster[1] < snake[-1][1]:
                    g_monster = (g_monster[0], g_monster[1] + aim_monster[1])
                elif g_monster[1] > snake[-1][1]:
                    g_monster = (g_monster[0], g_monster[1] - aim_monster[1])
            g_switch = not g_switch
        turtle.clearstamps()
        get_snake(snake)
        get_monster(g_monster)
        speed_monster = random.randint(
            400, 600
        )  # Move in a random speed faster or slower
        turtle.update()
        g_screen.tracer(0)
    turtle.ontimer(
        move_monster, speed_monster
    )  # A timer to update the monster regularly


"""Snake moves in the set direction.
The body of snake expends after eating the food.
Snake slows down when the body is expending.
"""


def move_snake():
    global speed_snake
    if g_game_over == False:
        if (  # Make sure the snake do not move when the screen is paused
            g_state_running == True
        ):
            head = snake[-1]
            head = (head[0] + aim[0], head[1] + aim[1])
            if (  # Make sure the snake is within the border.
                -240 <= head[0] <= 240 and -240 <= head[1] <= 240
            ):
                snake.append(head)
                snake.pop(0)
            turtle.clearstamps()
            get_snake(snake)
            get_monster(g_monster)
            dict_food = {}
            for (x, y, value) in g_foods:
                dict_food[(x, y)] = value
            if head in dict_food.keys():  # Check whether the snake eat the food.
                snake_append = snake[0]
                for i in range(dict_food[head]):
                    snake.insert(
                        0, snake_append
                    )  # Make element inserted from the beginning of list.
                    food.clear()
                for (x,y,z) in g_foods:  # Remove the food item from list after being eaten
                    if (x, y) == head:
                        g_foods.remove((x, y, z))
                get_food()
            if len(snake) != len(set(snake)):  # The speed is lower when snake is expending.
                speed_snake = 280
            else:
                speed_snake = 210
        turtle.update()
        g_screen.tracer(0)
    turtle.ontimer(move_snake, speed_snake)  # A timer to update the snake regularly


"""Check the contact between snake and monster.
Update the data of upper area.
Hint win when all the food is eaten.
Hint game over when monster touches the snake.
"""


def check():
    global current_time, g_monster, g_start_time, g_contact, g_game_over, g_time_passed, g_switch
    current_time = time.time()
    g_time_passed = int(current_time - g_start_time)
    if g_game_over == False:
        board()
        if monitor_contacted() == True:  # Count the number of contact.
            g_contact += 1
        if (  # Check whether monster touches the snake.
            -20 <= g_monster[0] - snake[-1][0] <= 20
            and -20 <= g_monster[1] - snake[-1][1] <= 20
        ):
            g_game_over = True
        if (  # Check whether a losing condition has been reached.
            g_game_over == True and len(g_foods) != 0
        ):
            turtle.penup()
            turtle.goto(snake[-1][0] - 40, snake[-1][1] - 40)
            turtle.write("Game Over!!!", align="left", font="Arial 16 bold")
        if (len(set(snake)) == len(snake)) and (
            len(g_foods) == 0
        ):  # Check whether a victory condition has been reached.
            get_snake(snake)
            get_monster(g_monster)
            turtle.color("cyan")
            turtle.penup()
            turtle.goto(snake[-1][0] - 40, snake[-1][1] - 40)
            turtle.write("Winner!!!", align="left", font="Arial 16 bold")
            g_game_over = True
        turtle.update()
        g_screen.tracer(0)
    turtle.ontimer(check, 200)  # A timer to check the situation regularly


# Create the intro screen.
def begin():
    set_food()
    frame()
    instruction()
    turtle.penup()
    turtle.goto(-200, 280)
    turtle.write(f"Time: 0", align="left", font="Arial 16 bold")
    turtle.goto(-70, 280)
    turtle.write(f"Contact: 0", align="left", font="Arial 16 bold")
    turtle.goto(60, 280)
    turtle.write(f"Motion: Paused", align="left", font="Arial 16 bold")
    get_monster(g_monster)
    get_snake(snake)


"""Listen to the screen.
Generate a random list of food items.
Bind the function to keys. 
Initialize the game.
"""


def main(x, y):
    global g_start_time, g_game_over
    turtle.clear()
    turtle.hideturtle()
    get_food()
    frame()
    turtle.listen()
    turtle.onscreenclick(None)  # Clear the function bound to clicking
    if g_game_over == False:  # Bind the key to function correspondingly
        turtle.onkey(lambda: direction(0, 20), "Up")
        turtle.onkey(lambda: direction(0, -20), "Down")
        turtle.onkey(lambda: direction(-20, 0), "Left")
        turtle.onkey(lambda: direction(20, 0), "Right")
        turtle.onkey(pause, "space")
    g_start_time = time.time()  # Get the start time of game
    move_monster()
    move_snake()
    check()
    turtle.update()
    turtle.done()


if __name__ == "__main__":
    hint = turtle.Turtle()  ##turtle object for hint in upper area.
    food = turtle.Turtle()  ##turtle object for food
    g_screen = install_screen()  ##initialize the windows of program
    g_screen.tracer(0)  ##turn off auto screen refresh
    begin()
    turtle.listen()
    turtle.onscreenclick(main)  ##start the game after clicking the screen.
    turtle.mainloop()  ##turn off auto screen refresh.

