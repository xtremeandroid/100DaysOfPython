from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.result: bool
        self.game_is_on : bool = True
        self.score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        right = PhotoImage(file="images/true.png")
        wrong = PhotoImage(file="images/false.png")
        self.question = self.canvas.create_text(150, 125, width=280, text="Question Text", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.wrong_button = Button(image=wrong, highlightthickness=0, command=self.wrong_button)
        self.wrong_button.grid(row=2, column=0)
        self.right_button = Button(image=right, highlightthickness=0, command=self.right_button)
        self.right_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):

        try:
            q_text = self.quiz.next_question()
        except IndexError:
            self.canvas.config(bg="white")
            self.game_is_on  = False
            self.score_label.config(text="")
            self.canvas.itemconfig(self.question, text=f"Congrats You Have Completed the Quiz Your Total Score was {self.score}/10")
        else:
            self.canvas.itemconfig(self.question, text=q_text)
            self.canvas.config(bg="white")
        finally:
            self.score_label.config(text=f"Score: {self.score}")

    def give_feedback(self, result):
        if result:
            self.score += 1
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)

    def right_button(self):
        if self.game_is_on:
            result = self.quiz.check_answer("True")
            self.give_feedback(result)

    def wrong_button(self):
        if self.game_is_on:
            result = self.quiz.check_answer("False")
            self.give_feedback(result)



