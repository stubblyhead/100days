import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("tomato time")
window.minsize(500,400)
window.config(padx=100,pady=50)
window.config(background=YELLOW)

bg_image = tkinter.PhotoImage(file='tomato.png')

canvas = tkinter.Canvas(width=210,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(106,112, image=bg_image)
canvas.create_text(106,140,text='00:00',fill="white",font=(FONT_NAME,24,'bold'))
canvas.pack()



window.mainloop()