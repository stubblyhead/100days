import tkinter

window = tkinter.Tk()
window.minsize(300,200)
window.config(padx=50,pady=100)
miles_input = tkinter.Entry()
miles_input.grid(column=2,row=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=3,row=1)

eq_label = tkinter.Label(text="is equal to")
eq_label.grid(column=1, row=2)

km_output = tkinter.Label()
km_output.grid(column=2,row=2)

km_label = tkinter.Label(text="km")
km_label.grid(column=3,row=2)

def convert():
    miles = float(miles_input.get())
    km_output.config(text=str(miles/0.621371))

calc_button = tkinter.Button(text="Calculate", command=convert)
calc_button.grid(column=2,row=3)









window.mainloop()