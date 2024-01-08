import random

while True:
    user_choice = input("Enter your choice (rock/paper/scissors): ")
    computer_choice = random.choice (["rock","paper","scissors"])

    if user_choice == computer_choice:
        print ("It's a tie")
    elif user_choice == "rock":
        if computer_choice == "paper":
            print ("Computer wins!! Computers choice was " + (computer_choice))
        else:
            print ("You win!! GG Computers choice was " + (computer_choice))
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print ("Computer wins!! Computers choice was " + (computer_choice))
        else:
            print ("You win!! Computers choice was " + (computer_choice))
    elif user_choice == "scissors":
        computer_choice == "rock"
        print (" Computer wins! Computers choice was " + (computer_choice))
    else:
        print (" You win!! Computers choice was " + (computer_choice)) 
    
    play_again = input(" Do you wanna play again (y/n): ")
    
    if play_again.lower() != "y":
        break
