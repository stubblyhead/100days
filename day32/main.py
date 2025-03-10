import tkinter
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
HEADING_FONT = ('Arial',40,'italic')
WORD_FONT = ('Arial',60,'bold')

right_count = 0
wrong_count = 0

with open('data/french_words.csv') as data:
    words = [ l.strip().split(',') for l in data.readlines() ]
    (front_hdg, back_hdg) = words.pop(0)

def new_word():
    right_btn['state'] = 'disabled'
    wrong_btn['state'] = 'disabled'
    (q_word, a_word) = random.choice(words)
    flashcard.itemconfig(heading_txt, text=front_hdg)
    flashcard.itemconfig(word_txt, text=q_word)
    window.after(3000,flip_word,back_hdg,a_word)

def flip_word(hdg,txt):
    flashcard.itemconfig(heading_txt, text=hdg)
    flashcard.itemconfig(word_txt, text=txt)
    right_btn['state'] = 'normal'
    wrong_btn['state'] = 'normal'

def right_click():
    global right_count
    right_count += 1
    new_word()

def wrong_click():
    global wrong_count
    wrong_count += 1
    new_word()

window = tkinter.Tk()
window.title('Flashy')
window.config(padx=50,pady=50)


flashcard = tkinter.Canvas(height=526,width=800,highlightthickness=0)
bg_front = tkinter.PhotoImage(file='images/card_front.png')
bg_back = tkinter.PhotoImage(file='images/card_back.png')
flashcard.create_image(400,263,image=bg_front)
heading_txt = flashcard.create_text(400,150,text='Heading text',font=HEADING_FONT)
word_txt = flashcard.create_text(400,263,text='Word text', font=WORD_FONT)

flashcard.grid(row=0,column=0,columnspan=2)

wrong_img = tkinter.PhotoImage(file='images/wrong.png')
wrong_btn = tkinter.Button(image=wrong_img, highlightthickness=0, command=wrong_click)

right_img = tkinter.PhotoImage(file='images/right.png')
right_btn = tkinter.Button(image=right_img, highlightthickness=0, command=right_click)

wrong_btn.grid(row=1,column=0)
right_btn.grid(row=1,column=1)
new_word()




window.mainloop()