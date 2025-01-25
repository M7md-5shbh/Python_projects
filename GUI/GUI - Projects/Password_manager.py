from tkinter import *
from tkinter import messagebox
from random import randint, sample
import string

# ------------------ Generate a Password ------------------ #
def generate_password():
    password = sample(string.ascii_letters, randint(8,10)) + sample(string.punctuation, randint(2,4)) + sample(string.digits, randint(2,4))
    password_entry.delete(0, END)
    password_entry.insert(END, "".join(password))

# ------------------ Save to File ------------------ #
def save_data():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Error", message="Please fill all the fields")
        return
    user_confirm = messagebox.askokcancel(title=website, message=f"These are the details you entered: \n{email}\n{password}, is this correct or do you want to go back to edit? ")

    if user_confirm:
        website_entry.delete(0, END)
        password_entry.delete(0, END)

        with open("save_file.txt", 'a+') as save_file:
            save_file.write(f"{website} | {email} | {password}\n")





window = Tk()
window.config(padx=20, pady=20)
window.minsize(400, 400)
window.title("Password Manager")


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="pass-logo.png")
canvas.create_image(100, 100 , image=logo_img)
canvas.grid(row=0, column=1, columnspan=2)


# Labels
# Website label
website_label = Label(window, text="Website:")
website_label.grid(row=1, column=0)

# Email/Username Label
email_username_label= Label(window, text="Email/Username:")
email_username_label.grid(row=2, column=0)

# Password Label
password_label = Label(window, text="Password:")
password_label.grid(row=3, column=0)

# Entries
# Website Entry
website_entry = Entry(window, width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky=EW)
website_entry.focus()

# Email/Username Entry
email_username_entry = Entry(window, width=35)
email_username_entry.grid(row=2, column=1, columnspan=2, sticky=EW)
email_username_entry.insert(0, "") # insert your email here if you have one you use for many websites

# Password Entry
password_entry = Entry(window, width=17)
password_entry.grid(row=3, column=1, sticky=EW)


# Buttons
# Generate Password Button
generate_password_button = Button(window, text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky=EW)

# Save button
save_button = Button(window, text="Save Password/Add password", command=save_data)
save_button.grid(row=4, column=1, columnspan=2, sticky=NSEW)

window.mainloop()
