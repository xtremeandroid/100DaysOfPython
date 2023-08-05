def randomNumber():
    from random import randint
    return randint(1,100)

def noOfattempts():
    if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy":
        return 10
    else:
        return 5

print("Welcome to the Number Guessing game!")
print("I M Thinking of a number between 1 and 100")
compNumber = randomNumber()
noOfattemptsRemaining = noOfattempts()
shouldContinue = True

while shouldContinue:

    if noOfattemptsRemaining != 0:
        print(f"You have {noOfattemptsRemaining} attempts remaining to guess the number.")
        userGuess = int(input("Make a guess: "))
        if userGuess > compNumber:
            print("Too High")
            noOfattemptsRemaining -= 1
        elif userGuess < compNumber:
            print("Too Low")
            noOfattemptsRemaining -= 1
        else:
            print("You guessed it right ! You Won. ")
            shouldContinue = False
    else:
        print("You Lose, You ran out of attempts.")
        shouldContinue = False


