import tkinter






# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Password Manager')
window.minsize(240,240)
window.config(padx=20, pady=20)

bg_image = tkinter.PhotoImage(file='logo.png')

canvas = tkinter.Canvas(height=200,width=200,highlightthickness=0)
canvas.create_image(100,100,image=bg_image)

canvas.grid(row=0,column=0)



window.mainloop()