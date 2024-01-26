
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}/{self.quiz.total_questions}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(
            row=0,
            column=1,
        )

        self.canvas = Canvas(
            width=300,
            height=250,
            bg="white",
         )
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 12, "italic")
        )
        self.canvas.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=20,
        )

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')

        if self.quiz.still_has_questions():
            self.true_button.config(state='active')
            self.false_button.config(state='active')
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.total_questions}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz!\n\nYou scored a {(self.quiz.score / self.quiz.total_questions)*100:.1f}%.")

    def true_pressed(self):
        user_response = self.quiz.check_answer(user_answer='True')
        self.give_feedback(user_response)
        self.true_button.config(state='disabled')
        self.false_button.config(state='disabled')

    def false_pressed(self):
        user_response = self.quiz.check_answer(user_answer='False')
        self.give_feedback(user_response)
        self.true_button.config(state='disabled')
        self.false_button.config(state='disabled')

    def give_feedback(self, user_response):
        if user_response == True:
            self.canvas.config(bg='green')
            self.quiz.score += 1
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)



