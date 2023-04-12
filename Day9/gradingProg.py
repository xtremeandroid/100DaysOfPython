student_scores = {
    "Sadiq": 18,
    "Ayush": 32,
    "Prajwal": 65,
    "Deon": 85,
    "Ishan": 92,
}
student_grades = {}
currentGrade = ""

for key in student_scores:
    currentScore = student_scores[key]
    if  currentScore > 90:
        currentGrade = "Outstanding"
    elif currentScore > 80:
        currentGrade = "Exceeds Expectations"
    elif currentScore > 70:
        currentGrade = "Acceptable"
    else:
        currentGrade = "Fail"
    student_grades[key] = currentGrade

print(student_grades)    