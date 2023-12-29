import random

point = 0

num_rounds = int(input("How many rounds do want to play?: "))

for round in range (num_rounds):
    c_guess = random.randint(1,3) 
    u_guess = int(input("Guess a number between 1 to 3: "))
    if (c_guess == u_guess):
        print ("Conrgats")
        point = point+1
    else:
        print ("Better luck next time. Computers number was " + str (c_guess))    

print ("You got " + str (point) + " points out of " + str (num_rounds))
