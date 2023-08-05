userInput = input("Enter Scores : \n").split()
scores = []
for inp in userInput:
    scores.append(int(inp))
highestScore = 0
for score in scores:
    if score > highestScore:
        highestScore = score
print(f"Highest Score is {highestScore}")