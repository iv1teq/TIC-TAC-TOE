from turtle import *



bob = Turtle()
screen = Screen()
bob.setheading(0)
bob.speed(100000)
bob.hideturtle()
gamestart = False



#Menu
def menu():
    bob.clear()
    bob.penup()
    bob.goto(-200,0)
    bob.write("Wanna play Tic Tac Toe?",font = ("Arial",30,"normal"))
    bob.pendown()
    for i in range(2):
        bob.forward(450)
        bob.right(90)
        bob.forward(100)
        bob.right(90)
    bob.penup()
    bob.goto(-20,-70)
    bob.pendown()
    bob.write("Yes!", font = ("Arial",30,"normal"))
    bob.hideturtle()
    screen.onclick(button) 
def button(x,y):
    global gamestart
    if -200 <= x <=250 and 0 >= y >= -70:
        gamestart = True
        print("Hi!")
        game()


menu()

battleground = [0,0,0,0,0,0,0,0,0]
playerzerolist = [0,0,0,0,0,0,0,0,0]
playercrosslist = [0,0,0,0,0,0,0,0,0]
player_zero = False
player_cross = True
def game():
    global gamestart
    bob.clear()
    if gamestart == True:
        # Function for squares
        def square():
            for i in range(4):
                bob.forward(100)
                bob.right(90)

        y_axe = 150

        #Playground
        for count in range(3):
            bob.penup()
            bob.goto(-150, y_axe)
            bob.pendown()
            for m in range (3):
                square()
                bob.forward(100)
                
            y_axe -= 100
        #Cross
        def cross(x , y):
            bob.setheading(0)
            bob.penup()
            bob.goto(x,y)
            bob.pendown()
            bob.pencolor("red")
            bob.pensize(3)
            bob.right(45)
            bob.forward(140)
            bob.back(70)
            bob.left(90)
            bob.forward(70)
            bob.back(140)
            bob.pencolor("black")
            bob.pensize(1)
        #Zero
        def zero(x , y):
            bob.setheading(0)
            bob.penup()
            bob.goto(x,y)
            bob.pendown()
            bob.pencolor("green")
            bob.pensize(3)
            bob.circle(49)
            bob.pencolor("black")
            bob.pensize(1)


        #Steps   
        def step (x,y):
            win()

            global battleground,player_zero,player_cross
            if -150 <= x <= -50 and 50 <= y <= 150:
                if battleground[0] == 0:
                    if player_zero == True:
                        zero(-100,50)
                        battleground[0] = 1
                        playerzerolist[0] = 1
                        player_zero = False
                        player_cross = True
                        print(battleground)
                        win()
                    elif player_zero == False :
                        cross(-150,150)
                        player_cross = False
                        player_zero = True
                        battleground[0] = 1
                        playercrosslist[0] = 1
                        print(battleground)
                        win()

            elif -50 <= x <= 50 and 50 <= y <= 150:
                if battleground[1] == 0:
                    if player_zero == True:
                        zero(0,50)
                        battleground[1] = 1
                        playerzerolist[1] = 1
                        player_zero = False
                        player_cross = True
                        print(battleground)
                        win()
                    elif player_zero == False :
                        cross(-50,150)
                        player_cross = False
                        player_zero = True
                        battleground[1] = 1
                        playercrosslist[1] = 1
                        print(battleground)
                        win()

            elif 50 <= x <= 150 and 50 <= y <= 150:
                if battleground[2] == 0:
                    if player_zero == True:
                        zero(100,50)
                        battleground[2] = 1
                        playerzerolist[2] = 1
                        player_zero = False
                        player_cross = True
                        print(battleground)
                        win()
                    elif player_zero == False :
                        cross(50,150)
                        player_cross = False
                        player_zero = True
                        battleground[2] = 1
                        playercrosslist[2] = 1
                        print(battleground)
                        win()
                
            
            elif -150 <= x <= -50 and -50 <= y <= 50:
                if battleground[3] == 0:
                    if player_zero == True:
                        zero(-100,-50)
                        battleground[3] = 1
                        playerzerolist[3] = 1
                        player_zero = False
                        player_cross = True
                        print(battleground)
                        win()
                    elif player_zero == False :
                        cross(-150,50)
                        player_cross = False
                        player_zero = True
                        battleground[3] = 1
                        playercrosslist[3] = 1
                        print(battleground)
                        win()

            elif -50 <= x <= 50 and -50 <= y <= 50:
                if battleground[4] == 0:
                    if player_zero == True:
                        zero(0,-50)
                        battleground[4] = 1
                        playerzerolist[4] = 1
                        player_zero = False
                        player_cross = True
                        print(battleground)
                        win()
                    elif player_zero == False :
                        cross(-50,50)
                        player_cross = False
                        player_zero = True
                        battleground[4] = 1
                        playercrosslist[4] = 1
                        print(battleground)
                        win()
                
            
        
            elif 50 <= x <= 150 and -50 <= y <= 50:
                if battleground[5] == 0:
                    if player_zero == True:
                        zero(100,-50)
                        battleground[5] = 1
                        playerzerolist[5] = 1
                        player_zero = False
                        player_cross = True
                        print(battleground)
                        win()
                    elif player_zero == False :
                        cross(50,50)
                        player_cross = False
                        player_zero = True
                        battleground[5] = 1
                        playercrosslist[5] = 1
                        print(battleground)
                        win()
            elif -150 <= x <= -50 and -150 <= y <= -50:
                if battleground[6] == 0:
                    if player_zero == True:
                        zero(-100,-150)
                        battleground[6] = 1
                        playerzerolist[6] = 1
                        player_zero = False
                        player_cross = True
                        print(battleground)
                        win()
                    elif player_zero == False :
                        cross(-150,-50)
                        player_cross = False
                        player_zero = True
                        battleground[6] = 1
                        playercrosslist[6] =1
                        print(battleground)
                        win()
            elif -50 <= x <= 50 and -150 <= y <= -50:
                if battleground[7] == 0:
                    if player_zero == True:
                        zero(0,-150)
                        battleground[7] = 1
                        playerzerolist[7] = 1
                        player_zero = False
                        player_cross = True
                        print(battleground)
                        win()
                    elif player_zero == False :
                        cross(-50,-50)
                        player_cross = False
                        player_zero = True
                        battleground[7] = 1
                        playercrosslist[7] = 1
                        print(battleground)
                        win()

            elif 50 <= x <= 150 and -150 <= y <= -50:
                if battleground[8] == 0:
                    if player_zero == True:
                        zero(100,-150)
                        battleground[8] = 1
                        playerzerolist[8] = 1
                        player_zero = False
                        player_cross = True
                        print(battleground)
                        win()
                    elif player_cross == True :
                        cross(50,-50)
                        player_cross = False
                        player_zero = True
                        battleground[8] = 1
                        playercrosslist[8] = 1
                        print(battleground)
                        win()
            

        screen.onclick(step)

def close_game(x,y):
    screen.bye()

def win():
    bob.pensize(5)
    if playercrosslist[0] == 1 and playercrosslist[1] == 1 and playercrosslist[2] == 1:
        bob.penup()
        bob.goto(-150,100)
        bob.pendown()
        bob.goto(150,100)
        bob.penup()
        bob.goto(-100,200)
        bob.write("Cross player wins!",font = ("Arial", 15,"normal"))
        screen.onscreenclick(close_game)

    if playerzerolist[0] == 1 and playerzerolist[1] == 1 and playerzerolist[2] == 1:
        bob.penup()
        bob.goto(-150,100)
        bob.pendown()
        bob.goto(150,100)
        bob.penup()
        bob.goto(-100,200)
        bob.write("Zeros player wins!",font = ("Arial",15,"normal"))
        screen.onscreenclick(close_game)
    if playercrosslist[0] == 1 and playercrosslist[3] == 1 and playercrosslist[6] == 1:
        bob.penup()
        bob.goto(-100,150)
        bob.pendown()
        bob.goto(-100,-150)
        bob.penup()
        bob.goto(-100,200)
        bob.write("Cross player wins!",font = ("Arial", 15,"normal"))
        screen.onscreenclick(close_game)
    if playerzerolist[0] == 1 and playerzerolist[3] == 1 and playerzerolist[6] == 1:
        bob.penup()
        bob.goto(-100,150)
        bob.pendown()
        bob.goto(-100,-150)
        bob.penup()
        bob.goto(-100,200)
        bob.write("Zeros player wins!",font = ("Arial",15,"normal"))
        screen.onscreenclick(close_game)
    if playercrosslist[0] == 1 and playercrosslist[4] == 1 and playercrosslist[8] == 1:
        bob.penup()
        bob.goto(-150,150)
        bob.pendown()
        bob.goto(150,-150)
        bob.penup()
        bob.goto(-100,200)
        bob.write("Cross player wins!",font = ("Arial", 15,"normal"))
        screen.onscreenclick(close_game)
    if playerzerolist[0] == 1 and playerzerolist[4] == 1 and playerzerolist[8] == 1:
        bob.penup()
        bob.goto(-150,150)
        bob.pendown()
        bob.goto(150,-150)
        bob.penup()
        bob.goto(-100,200)
        bob.write("Zeros player wins!",font = ("Arial",15,"normal"))
        screen.onscreenclick(close_game)
    if playercrosslist[2] == 1 and playercrosslist[5] == 1 and playercrosslist[8] == 1:
        bob.penup()
        bob.goto(100,150)
        bob.pendown()
        bob.goto(100,-150)
        bob.penup()
        bob.goto(-100,200)
        bob.write("Cross player wins!",font = ("Arial", 15,"normal"))
        screen.onscreenclick(close_game)
    if playerzerolist[2] == 1 and playerzerolist[5] == 1 and playerzerolist[8] == 1:
        bob.penup()
        bob.goto(100,150)
        bob.pendown()
        bob.goto(100,-150)
        bob.penup()
        bob.goto(-100,200)
        bob.write("Zeros player wins!",font = ("Arial",15,"normal"))
        screen.onscreenclick(close_game)
    if playercrosslist[2] == 1 and playercrosslist[4] == 1 and playercrosslist[6] == 1:
        bob.penup()
        bob.goto(150,150)
        bob.pendown()
        bob.goto(-150,-150)
        bob.penup()
        bob.goto(-100,200)
        bob.write("Cross player wins!",font = ("Arial", 15,"normal"))
        screen.onscreenclick(close_game)
    if playerzerolist[2] == 1 and playerzerolist[4] == 1 and playerzerolist[6] == 1:
        bob.penup()
        bob.goto(150,150)
        bob.pendown()
        bob.goto(-150,-150)
        bob.penup()
        bob.goto(-100,200)
        bob.write("Zeros player wins!",font = ("Arial",15,"normal"))
        screen.onscreenclick(close_game)
    if playercrosslist[6] == 1 and playercrosslist[7] == 1 and playercrosslist[8] == 1:
        bob.penup()
        bob.goto(-150,-100)
        bob.pendown()
        bob.goto(150,-100)
        bob.penup()
        bob.goto(-100,200)
        bob.write("Cross player wins!",font = ("Arial", 15,"normal"))
        screen.onscreenclick(close_game)
    if playerzerolist[6] == 1 and playerzerolist[7] == 1 and playerzerolist[8] == 1:
        bob.penup()
        bob.goto(-150,-100)
        bob.pendown()
        bob.goto(150,-100)
        bob.penup()
        bob.goto(-100,200)
        bob.write("Zeros player wins!",font = ("Arial",15,"normal"))
        screen.onscreenclick(close_game)
    if playercrosslist[3] == 1 and playercrosslist[4] == 1 and playercrosslist[5] == 1:
        bob.penup()
        bob.goto(-150,0)
        bob.pendown()
        bob.goto(150,0)
        bob.penup()
        bob.goto(-100,200)
        bob.write("Cross player wins!",font = ("Arial", 15,"normal"))
        screen.onscreenclick(close_game)
    if playerzerolist[3] == 1 and playerzerolist[4] == 1 and playerzerolist[5] == 1:
        bob.penup()
        bob.goto(-150,0)
        bob.pendown()
        bob.goto(150,0)
        bob.penup()
        bob.goto(-100,200)
        bob.write("Zeros player wins!",font = ("Arial",15,"normal"))
        screen.onscreenclick(close_game)
    if playercrosslist[1] == 1 and playercrosslist[4] == 1 and playercrosslist[7] == 1:
        bob.penup()
        bob.goto(0,150)
        bob.pendown()
        bob.goto(0,-150)
        bob.penup()
        bob.goto(-100,200)
        bob.write("Cross player wins!",font = ("Arial", 15,"normal"))
        screen.onscreenclick(close_game)
    if playerzerolist[1] == 1 and playerzerolist[4] == 1 and playerzerolist[7] == 1:
        bob.penup()
        bob.goto(0,150)
        bob.pendown()
        bob.goto(150,0)
        bob.penup()
        bob.goto(0,-150)
        bob.write("Zeros player wins!",font = ("Arial",15,"normal"))
        screen.onscreenclick(close_game)

mainloop()