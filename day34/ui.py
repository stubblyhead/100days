import tkinter
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
Q_FONT = ('Arial', 20, 'italic')

class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = tkinter.Tk()
        self.window.title('Quizzler')
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.score_lbl = tkinter.Label(text="Score: 0", background=THEME_COLOR, foreground='white')
        self.score_lbl.grid(row=0, column = 1)

        self.question = tkinter.Canvas(height=250, width=300)
        self.question_text = self.question.create_text(150, 125, text='This is some example text', font= Q_FONT, width=280)
        self.question.grid(row=1, column = 0, columnspan = 2, pady=20)

        def true_cmd():
            correct = self.quiz.check_answer('True')
            if correct:
                self.score_lbl.config(text=f'Score: {(self.quiz.score)}')
            if self.quiz.still_has_questions():
                self.get_next_question()

        def false_cmd():
            correct = self.quiz.check_answer('False')
            if correct:
                self.score_lbl.config(text=f'Score: {(self.quiz.score)}')
            if self.quiz.still_has_questions():
                self.get_next_question()

        true_img = tkinter.PhotoImage(file='images/true.png')
        self.true_btn = tkinter.Button(image=true_img, highlightthickness=0, command=true_cmd)
        self.true_btn.grid(row=2, column=0)

        false_img = tkinter.PhotoImage(file='images/false.png')
        self.false_btn = tkinter.Button(image=false_img, highlightthickness=0, command=false_cmd)
        self.false_btn.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        next_q = self.quiz.next_question()
        self.question.itemconfig(self.question_text, text=next_q)

    