import tkinter
THEME_COLOR = "#375362"
Q_FONT = ('Arial', 20, 'italic')

class QuizInterface:

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('Quizzler')
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.score_lbl = tkinter.Label(text="Score: 0", background=THEME_COLOR)
        self.score_lbl.grid(row=0, column = 1)

        self.question = tkinter.Canvas(height=250, width=300)
        self.question.create_text(125, 150, text='This is some example text', font= Q_FONT, width=280)
        self.question.grid(row=1, column = 0, columnspan = 2, pady=20)

        true_img = tkinter.PhotoImage(file='images/true.png')
        self.true_btn = tkinter.Button(image=true_img, highlightthickness=0)
        self.true_btn.grid(row=2, column=0)

        false_img = tkinter.PhotoImage(file='images/false.png')
        self.false_btn = tkinter.Button(image=false_img, highlightthickness=0)
        self.false_btn.grid(row=2, column=1)

        self.window.mainloop()