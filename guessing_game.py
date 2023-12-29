import random

point = 0

for round in range (5):
    c_guess = random.randint(1,3) 
    u_guess = int(input("Guess a number between 1 to 3: "))
    if (c_guess == u_guess):
        print ("Conrgats")
        point = point+1
    else:
        print ("Better luck next time. Computers number was " + str (c_guess))    

print ("You got " + str (point) +" points")
