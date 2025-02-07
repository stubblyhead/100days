import tkinter

window = tkinter.Tk()
window.minsize(500,500)
window.config(padx=2, pady=2)
def button_clicked():
    new_text = my_input.get()
    label_one.config(text=new_text)
label_one = tkinter.Label(text='this is a label text')
label_one.grid(column=0, row=0)


button_one = tkinter.Button(text="Click me", command=button_clicked)
button_one.config(padx=20,pady=20)
button_one.grid(column=1, row=1)

button_two = tkinter.Button(text="Click me as well", command=button_clicked)
button_two.grid(column=2, row=0)

my_input=tkinter.Entry()
my_input.grid(column=3,row=10)

window.mainloop()