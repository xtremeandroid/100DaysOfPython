class QuizBrain:

    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is : {self.score}/{self.question_no}")
        print("\n")

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_no].question
        current_answer = self.question_list[self.question_no].answer
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no}: {current_question}. (True/False)?: ")
        self.check_answer(user_answer, current_answer)
