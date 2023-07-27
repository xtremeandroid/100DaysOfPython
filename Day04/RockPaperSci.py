import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

userInput = int(input("Enter a Number 1.Rock 2.Paper 3.Scissor\n")) -1
handArt = [rock,paper,scissors]
randomChoice = random.randint(0,2)

if userInput < 2 and userInput > 0:
    print("You Chose\n")
    print(handArt[userInput])
    print("Computer Chose\n")
    print(handArt[randomChoice])
    if userInput == randomChoice:
        print("Its A Tie")

    if userInput == 0:
        if randomChoice == 1:
            print("You Lose")
        if randomChoice == 2:
            print("You Won")

    if userInput == 1:
        if randomChoice == 0:
             print("You Won")
        if randomChoice == 2:
             print("You Lose")

    if userInput == 2:
        if randomChoice == 0:
            print("You Lose")
        if randomChoice == 1:
            print("You Won")
else:
    print("Enter a valid number, You Lose")




