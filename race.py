import turtle
import os
import math 
import random
import pygame
import time

# set up screen
window = turtle.Screen()
window.bgcolor("black")
window.title("Dont Crash")

#Register Shapes
turtle.register_shape("player.gif")
turtle.register_shape("car.gif")

#Draw Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("White")
border_pen.penup()
border_pen.setposition(-120,-300)
border_pen.pendown()
border_pen.pensize(5)
for side in range(4):
	if (side%2) == 0:
		border_pen.fd(240)
	else:
		border_pen.fd(600)
	border_pen.lt(90)
border_pen.setposition(-40,-300)
border_pen.pendown()
border_pen.pensize(2)
for side in range(4):
	if (side%2) == 0:
		border_pen.fd(80)
	else:
		border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()

#set the score to zero
score = 0
flag = False

#draw pen
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("White")
score_pen.penup()
score_pen.setposition(-290,240)
scorestring = "Score %s" %score
score_pen.write(scorestring, False, align = "left", font =("Arial", 14, "normal"))
score_pen.hideturtle()

#create the player turtle
player = turtle.Turtle()
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-200)
player.setheading(90)

playerspeed = 15

#list of enemy
enemies = []
no_of_enemy = 0

def generate_enemy():
	global enemies 
	global no_of_enemy 
	old_no_of_enemy = no_of_enemy
	no_of_enemy = random.randint(1, 2)

	#create enemy
	for i in range(no_of_enemy):
		enemies.append({"car" : turtle.Turtle(), "x_position" : random.choice([-80, 0, 80]), "y_position": 350 , "no" : no_of_enemy})

	#enemy charecters
	for enemy in enemies:
		enemy["car"].shape("car.gif")
		enemy["car"].penup()
		enemy["car"].speed(0)
		x = enemy["x_position"]
		y = enemy["y_position"]
		enemy["car"].setposition(x,y)

#Move player left and right
def move_left():
	x = player.xcor()
	if x > -100:
		x -= playerspeed
	player.setx(x)

def move_right():
	x = player.xcor()
	if x < 100:
		x += playerspeed
	player.setx(x)

def isCollision(t1,t2):
	dist = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2) + math.pow(t1.ycor() - t2.ycor(), 2))
	if dist < 50:
		return True
	else:
		return False

#keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")

generate_enemy()
if no_of_enemy == 1:
	enemyspeed = 2
else:
	enemyspeed = 4
while True:
	if enemies[-1]["y_position"] < 100:
		generate_enemy()
		enemyspeed = len(enemies) * 2
	for enemy in enemies:
		#Move enemy
		if enemy["y_position"] > -300:
			enemy["y_position"] -= enemyspeed
			enemy["car"].sety(enemy["y_position"])
		else:
			score += enemy["no"]
			scorestring = "Score %s" %score
			score_pen.clear()
			score_pen.write(scorestring, False, align = "left", font =("Arial", 14, "normal"))
			for i in range(enemy["no"]):
				enemies[0]["car"].hideturtle()
				del enemies[0]
			enemyspeed = 4

		#check for player collision
		if(isCollision(player, enemy["car"])):
			#Reset bullet
			print("Game over")
			player.hideturtle()
			enemy["car"].hideturtle()
			flag = True
			break

	if flag:
			break