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
TESTING = True
CHECKMARK = "✓"
reps = 0
checklabel = ''
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_cmd():
    global reps
    global checklabel
    global count
    global timer
    window.after_cancel(timer)
    checklabel = ''
    count.config(text=checklabel)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text='')
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_cmd():
    global reps
    
    reps += 1
    if TESTING:
        factor = 1
    else:
        factor = 60
    if reps % 2 == 1:
        title.config(text='Work', fg=GREEN)
        countdown(WORK_MIN * factor)
    elif reps % 8 == 0:
        title.config(text='Break', fg=RED)
        countdown(LONG_BREAK_MIN * factor)
    elif reps % 2 == 0:
        title.config(text='Break', fg=PINK)
        countdown(SHORT_BREAK_MIN * factor)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(sec):
    global timer
    global reps
    #global count
    global checklabel
    count_string = "{0:02d}:{1:02d}".format(sec//60,sec%60)
    canvas.itemconfig(timer_text, text=count_string)
    if sec > 0:
        timer = window.after(1000, countdown, sec-1)
    if sec == 0 and reps % 2 == 0:
        checklabel += CHECKMARK
        count.config(text=checklabel) 
        


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("tomato time")
window.minsize(500,400)
window.config(padx=100,pady=50)
window.config(background=YELLOW)

bg_image = tkinter.PhotoImage(file='tomato.png')

canvas = tkinter.Canvas(width=210,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(106,112, image=bg_image)
timer_text = canvas.create_text(106,140,text='00:00',fill="white",font=(FONT_NAME,24,'bold'))
canvas.grid(row=2,column=2)

title = tkinter.Label(text='',fg=GREEN, bg=YELLOW,font=(FONT_NAME,48,'normal'))
title.grid(row=1,column=2)

start_btn = tkinter.Button(text="Start", command=start_cmd)
reset_btn = tkinter.Button(text="Reset", command=reset_cmd)
start_btn.grid(row=3,column=1)
reset_btn.grid(row=3,column=3)

count = tkinter.Label(text=checklabel,fg=GREEN,bg=YELLOW,font=(FONT_NAME,24,"bold"))
count.grid(row=4,column=2)
window.mainloop()