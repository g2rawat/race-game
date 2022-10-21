from multiprocessing.resource_sharer import stop
from turtle import Turtle,Screen
import random
wn=Screen()
wn.screensize(500,500)

race=True
colour=["yellow","black","orange","blue","purple"]
turtle_name1=[]


def box():
    box=Turtle()
    box.hideturtle()

    box.speed("fastest")
    box.penup()
    box.goto(-290,-240)
    box.pendown()
    box.speed("fast")

    for i in range(4):
        box.forward(500)
        box.setheading(box.heading()+90)

box()
for i in range (5):
    turtle_name=Turtle(shape="turtle")
    turtle_name.penup()
    turtle_name.color(colour[i])
    turtle_name.goto(-235,-210+(i*100))
    turtle_name1.append(turtle_name)
pop_qn=wn.textinput("Turtle Race","Bet on which Turtle?")
while race is True:
    for turtle in turtle_name1:
        turtle.pendown()
        turtle.speed("fastest")
        turtle.forward(random.randint(0,50))
        if turtle.xcor()>200:
            race=False
            
            wining_tur_col=turtle.pencolor()
            
            if wining_tur_col==pop_qn:
                print("you win")
                print(f"you lose, winner is {wining_tur_col}")
                jim=Turtle()
                jim.penup()
                jim.speed("slow")
                jim.goto(253,-120)
                jim.write("W\nI\nN\nN\nE\nR",move=False, align="center", font=("Arial", 25, "normal"))
                jim.hideturtle()
                
            else:
                print(f"you lose, winner is {wining_tur_col}")
                jim=Turtle()
                jim.penup()
                jim.speed("slow")
                jim.goto(253,-120)
                jim.write("G\nA\nM\nE\n\nO\nV\nE\nR",move=False, align="center", font=("Arial", 25, "normal"))
                jim.hideturtle()
            break

wn.exitonclick()