import tkinter

datafile = open('totallynotpasswords.txt','a')




# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    with open('totallynotpasswords.txt','a') as datafile:
        datafile.write(f'{website} | {username} | {password}\n')

    website_entry.delete(0,tkinter.END)
    username_entry.delete(0,tkinter.END)
    password_entry.delete(0,tkinter.END)
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
website_entry.focus()

username_lbl = tkinter.Label(text='Email/username:')
username_lbl.grid(row=2,column=0)
username_entry = tkinter.Entry(width=35)
username_entry.insert(0,'myemail@example.com')
username_entry.grid(row=2,column=1,columnspan=2)

password_lbl = tkinter.Label(text='Password:')
password_lbl.grid(row=3,column=0)
password_entry = tkinter.Entry(width=18)
password_entry.grid(row=3,column=1)
password_btn = tkinter.Button(text='Generate Password')
password_btn.grid(row=3,column=2)

add_btn = tkinter.Button(text='Add',width=36,command=add_password)
add_btn.grid(row=4,column=1,columnspan=2)

window.mainloop()