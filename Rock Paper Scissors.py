# Rock Paper Scissors

#import the random library 
import random 

#create a list of play options
options = ["rock", "paper", "scissors"]

#assign a random play to the computer
computer = random.choice(options)

#set player to False
player = False

#while player is False, keep looping
while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?: ")
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = random.choice(options)