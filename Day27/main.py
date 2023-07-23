from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
# window.minsize(300, 200)
window.config(padx=20, pady=20)


def calc():
    userinput = int(input_box.get())
    value = userinput * 1.609
    label3.config(text=value)


input_box = Entry(width=7)
input_box.grid(column=2, row=1)

label1 = Label(text="Miles")
label1.grid(column=3, row=1)

label2 = Label(text="is equal to")
label2.grid(column=1, row=2)

label3 = Label(text=0)
label3.grid(column=2, row=2)

label4 = Label(text="KM")
label4.grid(column=3, row=2)

calc_button = Button(text="Calculate", command=calc)
calc_button.grid(column=2, row=3)

window.mainloop()
