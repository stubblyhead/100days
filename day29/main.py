import tkinter






# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

bg_image = tkinter.PhotoImage(file='logo.png')

canvas = tkinter.Canvas(height=200,width=200,highlightthickness=0)
canvas.create_image(100,100,image=bg_image)
canvas.grid(row=0,column=1)

website_lbl = tkinter.Label(text='Website:')
website_lbl.grid(row=1,column=0)
website_entry = tkinter.Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)

username_lbl = tkinter.Label(text='Email/username:')
username_lbl.grid(row=2,column=0)
username_entry = tkinter.Entry(width=35)
username_entry.grid(row=2,column=1,columnspan=2)

password_lbl = tkinter.Label(text='Password:')
password_lbl.grid(row=3,column=0)
password_entry = tkinter.Entry(width=18)
password_entry.grid(row=3,column=1)
password_btn = tkinter.Button(text='Generate Password')
password_btn.grid(row=3,column=2)

add_btn = tkinter.Button(text='Add',width=36)
add_btn.grid(row=4,column=1,columnspan=2)


window.mainloop()