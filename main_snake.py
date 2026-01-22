
from turtle import Turtle, Screen
import time
import random

# Proměnné
score = 0
highest_score = 0

screen = Screen()
screen.bgcolor("green")
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.tracer(False)

# Nastavení hadí hlavy
head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0,0)
head.direction = "stop"

# Nastavení jablek
apple = Turtle("circle")
apple.color("red")
apple.speed(0)
apple.penup()
apple.goto(100,100)

# Nastavení počítadla scóre
score_counter = Turtle("square")
score_counter.speed(0)
score_counter.color("white")
score_counter.penup()
score_counter.hideturtle()
score_counter.goto(-270,270)
score_counter.write("Scóre: 0  Nejvyšší scóre: 0 " , font=("Arial", 14))


body_parts = []

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Funkce nastavení pohybů
def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_right():
    if head.direction != "left":
        head.direction = "right"

def move_left():
    if head.direction != "right":
        head.direction = "left"

# Ovládání klávesnicí
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

# Hlavní cyklus
while True:
    screen.update()

    # Kontrola kolize s hranou obrazovky
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(2)
        head.goto(0, 0)
        head.direction = "stop"
        for one_body_part in body_parts:
            one_body_part.goto(1000, 1000)
        body_parts.clear()
        score = 0
        score_counter.clear()
        score_counter.write(f"Scóre: {score}  Nejvyšší scóre: {highest_score} ", font=("Arial", 14))

    # Vygenerování nového jablka po snězení jídla
    if head.distance(apple) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        apple.goto(x, y)
        score += 1
        if score > highest_score:
            highest_score = score
        score_counter.clear()
        score_counter.write(f"Scóre: {score}  Nejvyšší scóre: {highest_score} " , font=("Arial", 14))

    # Přidání do těla
        new_body_part = Turtle("circle")
        new_body_part.speed(0)
        new_body_part.color("grey")
        new_body_part.penup()
        body_parts.append(new_body_part)

    for i in range(len(body_parts) - 1, 0, -1):
        x = body_parts[i - 1].xcor()
        y = body_parts[i - 1].ycor()
        body_parts[i].goto(x, y)

    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x, y)

    move()

    # Kolize hlavy s tělem
    for one_body_part in body_parts:
        if one_body_part.distance(head) < 20:
            time.sleep(2)
            head.goto(0, 0)
            head.direction = "stop"
            one_body_part.goto(0, 0)
            for one_body_part in body_parts:
                one_body_part.goto(1000, 1000)
            body_parts.clear()
            score = 0
            score_counter.clear()
            score_counter.write(f"Scóre: {score}  Nejvyšší scóre: {highest_score} ", font=("Arial", 14))

    time.sleep(0.1)
    screen.update()


screen.exitonclick()