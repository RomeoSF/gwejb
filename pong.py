from turtle import Turtle, Screen
import time
import itertools
import math

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)

player_1 = Turtle()
player_1.color("Black")
player_1.shape("square")
player_1.shapesize(stretch_wid=5, stretch_len=1)

player_1.penup()
player_1.goto(-350, 0)  
player_1.color("White")

player_2 = Turtle()
player_2.color("Black")
player_2.shape("square")
player_2.shapesize(stretch_wid=5, stretch_len=1)

player_2.penup()
player_2.goto(350, 0)
player_2.color("White")

ball = Turtle()
ball.shape("circle")
ball.color("White")
ball.penup()


score = Turtle()
score.color("White")
score.penup()
score.hideturtle()
left_score = 0
right_score = 0

rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
winner = Turtle()
winner.penup()
winner.hideturtle()


def get_rgb_color(t, offset=0):
    """Generate RGB colors that cycle smoothly"""
    r = int(127 * (1 + math.sin(t + offset)))
    g = int(127 * (1 + math.sin(t + offset + 2)))
    b = int(127 * (1 + math.sin(t + offset + 4)))
    return f"#{r:02x}{g:02x}{b:02x}"

def winner_show(text):
    """Show winner text with animated RGB colors"""
    winner.clear()
    start_time = time.time()
    
    
    while time.time() - start_time < 5:
        winner.clear()
        current_time = time.time() * 4  
        
        
        total_width = len(text) * 30
        start_x = -total_width // 2
        
        for i, char in enumerate(text):
            
            color_offset = i * 0.5
            color = get_rgb_color(current_time, color_offset)
            winner.color(color)
            winner.goto(start_x + i * 30, 0)
            winner.write(char, align="center", font=("Courier", 40, "bold"))
        
        screen.update()
        time.sleep(1.5)  
    
    
    winner.clear()
    rainbow_colors = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#9400D3"]
    color_cycle = itertools.cycle(rainbow_colors)
    total_width = len(text) * 30
    start_x = -total_width // 2
    
    for i, char in enumerate(text):
        winner.color(next(color_cycle))
        winner.goto(start_x + i * 30, 0)
        winner.write(char, align="center", font=("Courier", 40, "bold"))

def move_up():
    y = player_1.ycor() + 20
    player_1.goto(player_1.xcor(), y)

def move_down():
    y = player_1.ycor() - 20
    player_1.goto(player_1.xcor(), y)

def move_up_2():
    y = player_2.ycor() + 20
    player_2.goto(player_2.xcor(), y)

def move_down_2():
    y = player_2.ycor() - 20
    player_2.goto(player_2.xcor(), y)

    
def update_score():
    global left_score, right_score
    score.clear()
    score.goto(-100, 200)
    score.write(left_score, align="center", font=("Courier", 80, "normal"))
    score.goto(100, 200)
    score.write(right_score, align="center", font=("Courier", 80, "normal"))
    ball.goto(0, 0)
  
    

ball_ax = 10
ball_ay = 10

def move_ball():
    ball_x = ball.xcor() + ball_ax
    ball_y = ball.ycor() + ball_ay
    ball.goto(ball_x, ball_y)

screen.listen()


screen.onkey(move_up, "w")
screen.onkey(move_down, "s")

screen.onkey(move_up_2, "Up")
screen.onkey(move_down_2, "Down")

update_score()

game_on = True

while game_on == True:
    screen.update(  )
    move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball_ay *= -1
    if ball.xcor() > 370:
        left_score += 1
        screen.update()
        update_score()
        ball.hideturtle()
        ball.penup()
        ball.goto(0,0)
        ball.showturtle()
        time.sleep(0.5)
    elif ball.xcor() < -370:
        right_score += 1
        update_score()
        ball.hideturtle()
        ball.penup()
        ball.goto(0,0)
        ball.showturtle()
        time.sleep(0.5)
    if (ball.xcor() < -320 and ball.xcor() > -360 and 
        ball.ycor() < player_1.ycor() + 50 and ball.ycor() > player_1.ycor() - 50):
        ball_ax *= -1
    if (ball.xcor() > 320 and ball.xcor() < 360 and 
        ball.ycor() < player_2.ycor() + 50 and ball.ycor() > player_2.ycor() - 50):
        ball_ax *= -1
    if left_score == 3:
        winner_show("Player 1 Wins!")
        screen.update()
        game_on = False
    elif right_score == 3:
        winner_show("Player 2 Wins!")
        screen.update()
        game_on = False

screen.exitonclick()