'''
Created on May 3, 2020

@author: ITAUser
'''
from random import random

keepPlaying = True

while keepPlaying == True:
    print("Welcome to Rock Paper Scissors.")
    print("Best 2 out of 3 wins. Press 'q' to quit")
    
    rock = 1
    scissors = 2
    paper = 3

    playerScore = 0
    computerScore = 0

    while(playerScore < 2 and computerScore < 2):
        computerChoice = random.randint(1,3)
        playerChoice = input("Please choose Rock, Paper, or Scissors")
        playerChoice = playerChoice.lower()
    
    if(playerChoice == 'q'):
        keepPlaying = False 
        break

    elif((playerChoice == "rock" and computerChoice == 1) or (playerChoice == "scissors" and computerChoice == 2) or (playerChoice == "paper" and computerChoice == 3)):
        print("DRAW")
        print("Player's Score =" + playerScore._str_() + "Computer's Score =" +  computerScore._str_())
    elif((playerChoice == "rock" and computerChoice == 2) or (playerChoice == "scissors" and computerChoice == 3 ) or (playerChoice == "paper" and computerChoice == 1)):
        playerScore = playerScore + 1
        print("Player's Score =" + playerScore._str_() + "Computer's Score =" +  computerScore._str_())
        print("ROUND WON")
    elif((playerChoice == "rock" and computerChoice == 3) or (playerChoice == "scissors" and computerChoice == 1) or (playerChoice == "paper" and computerChoice == 2)):
        computerScore = computerScore + 1
        print("Player's Score =" + playerScore._str_() + "Computer's Score =" +  computerScore._str_())
        print("ROUND LOST")
    else:
        print("Input is not valid.Try again.")
        print("Thank you for playing!") 
    if(playerScore == 2):
        print("WINNER")
    if(computerScore == 2):
        print("LOSER. COMPUTER WINS.")
    print("Player's Score =" + playerScore._str_() + "Computer's Score =" +  computerScore._str_())
