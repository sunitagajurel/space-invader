import turtle
import os
import math
import random



screen =turtle.Screen()
screen.bgcolor('black')
screen.title('space invader')

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-200,-200)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(450)
    border_pen.lt(90)
border_pen.hideturtle()

#set score
score =0

#Draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-180,180)
scorestring = "score : %s " %score
score_pen.write(scorestring,False,align="left",font =("Arial",14,"normal"))
score_pen.hideturtle()               


#Create the player turtle

player =turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-180)
player.setheading(90)

playerspeed =15

#choose no of enemies
no_of_enemies =5
enemies =[]

for i in range (no_of_enemies):
     enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x= random.randint(-200,200)
    y= random.randint(-150,150)
    enemy.setposition(x,y)
    
enemyspeed =2

  

# create the players bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
# bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bulletspeed =20

#define bulletstate

bulletstate ="ready"



#move player
def move_left():
    x= player.xcor()
    x-=playerspeed
    if x<-280:
        x=-280
    player.setx(x)
    


def move_right():
    x= player.xcor()
    x+=playerspeed
    if x> 280:
        x=280
    player.setx(x)



def fire_bullet():
    global bulletstate
    if bulletstate =="ready":
        bulletstate = "fire"

        #move the bullet to the just above the player
        x = player.xcor()
        y=player.ycor() +10
        bullet.setposition(x,y)
        bullet.showturtle()


def isCollision(t1,t2):
    distance =math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance <15:
        return True

#keyword bindings
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")

#main game loop

while True:
    for enemy in enemies:
        
        #Move the enemy
        x=enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)

        #move the enemy back and down
        if enemy.xcor()> 200 :
            for e in enemies:
                 y= e.ycor()
                 y-=40
                 e.sety(y)
            #change enemy direction
            enemyspeed*= -1

        if enemy.xcor()< -200:
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
            enemyspeed *= -1

        #Move the bullet
            if bulletstate =="fire":
                 y= bullet.ycor()
                 y+= bulletspeed
                 bullet.sety(y)

             #check to see if bullet has gone to the top
                 if(bullet.ycor()> 200):
                    bullet.hidetutle()
                    bulletstate ="ready"

            # check for collision

            if(isCollision (bullet,enemy)):
               bullet.hideturtle()
               bulletstate = "ready"
               bullet.setposition(0,-400)
               x= random.randint(-200,200)
               y= random.randint(-150,150)
               enemy.setposition (x,y)

               #update the score
               score+=10
               score_pen.clear()
               scorestring = "score : %s " %score
               score_pen.write(scorestring,False,align="left",font =("Arial",14,"normal"))
                               

                

            if (isCollision (player,enemy)):
                enemy.hideturtle()
                player.hideturtle()
                print("Game Over")
                break
                   
                   
                   
                    

