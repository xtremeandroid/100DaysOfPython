from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_bank.append(Question(item['question'], item['correct_answer']))

q1 = QuizBrain(question_bank)

while q1.still_has_questions():
    q1.next_question()

print("You've completed the quiz.")
print(f"Your final score was {q1.score}/{len(question_bank)}")

