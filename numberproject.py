# import random
# secrete_number=random.randint(1,20)
# attempt=10
# while True:
#     guess_number=int(input("enter the number: "))
#     if guess_number>secrete_number:
#         print("secret number is less than guess number")
#     elif guess_number<secrete_number:
#         print("secret number is greater than guess number") 
#     else:
#         print("congutes your guess number is correct...")
   
        
#         play_again=input("do you want to play game agin ? (YES/NO):").lower()
       
#         if play_again=="yes":
#            secrete_number=random.randint(1,20)
#            attempt=0
#            print("new game start:")       
#         else:
#            print("thank you")
#            break
          
          
# garphic appliing for numbers      

import turtle
import random
screen = turtle.Screen()
screen.title("Guess My Number Game")
screen.bgcolor("orange")
blackpen = turtle.Turtle()
blackpen.hideturtle()
blackpen.penup()
blackpen.goto(0,100)
blackpen.write("guess","Welcome to Guess My Number!", align="center", font=("Arial", 16, "bold"))
secrete_number=random.randint(1,20)
attempt=0
while True:
    guess = int(screen.textinput("Guess", "Enter a number between 1 and 20:"))
    attempt += 1
    if guess>secrete_number:
        blackpen.clear()
        blackpen.write(f"secret number is less than guess number",align="center",font=("arial",17,"bold"))
    elif guess<secrete_number:
        blackpen.clear()
        blackpen.write(f"secret number is greater than guess number",align="center",font=("arial",17,"bold"))
    else:
        blackpen.clear()
        blackpen.write(f"🎉congrats! the number was {secrete_number}\nAttempts:{attempt}",
                    align="center",font=("arial",17,"bold"))
  







# import random
# secrete_latter=random.choice("a,z")
# attempt=10
# while True:
#     guess_letter=input("enter the letter:")
#     if guess_letter>secrete_letter:
#         print("the letter is worng")
#     if guess_letter==secrete_letter:
#         print("congrats your guess letter is correct")   
        
#     else:
#         print("the letter is more then letter")
        