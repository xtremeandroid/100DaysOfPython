from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    pass_list = password_letters + password_symbols + password_numbers
    random.shuffle(pass_list)
    password = "".join(pass_list)
    input3.delete(0, END)
    input3.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_to_file():
    website = input1.get()
    email = input2.get()
    password = input3.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="OOPS", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details you entered : \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", 'a') as file:
                file.write(f"{website} | {email} | {password}\n")
            input1.delete(0, END)
            input3.delete(0, END)
            input1.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)
image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

label1 = Label(text="Website:")
label1.grid(row=1, column=0)
input1 = Entry(width=50)
input1.grid(row=1, column=1, columnspan=2)
input1.focus()

label2 = Label(text="Email/Username:")
label2.grid(row=2, column=0)
input2 = Entry(width=50)
input2.insert(0, "snapit4ayush@gmail.com")
input2.grid(row=2, column=1, columnspan=2)

label3 = Label(text="Password:")
label3.grid(row=3, column=0)
input3 = Entry(width=25)
input3.grid(row=3, column=1)

button1 = Button(text="Generate Password", command=generate_password)
button1.grid(row=3, column=2)

button2 = Button(text="Add", width=50, command=save_to_file)
button2.grid(row=4, column=1, columnspan=2)





window.mainloop()
