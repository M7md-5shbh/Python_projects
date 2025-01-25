import email
from tkinter import *
from tkinter import messagebox
from random import randint, sample
import string
import json

# ------------------ Generate a Password ------------------ #
def generate_password():
    password = sample(string.ascii_letters, randint(8,10)) + sample(string.punctuation, randint(2,4)) + sample(string.digits, randint(2,4))
    password_entry.delete(0, END)
    password_entry.insert(END, "".join(password))

# ------------------ Save to File ------------------ #
def save_data():
    website = website_entry.get().title()
    email = email_username_entry.get().lower()
    password = password_entry.get().lower()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Error", message="Please fill all the fields")
        return
    user_confirm = messagebox.askokcancel(title=website, message=f"These are the details you entered: \n{email}\n{password}\nIs this correct or do you want to go back to edit? ")

    if user_confirm:
        new_data = {
            website: {
            "email": email,
            "password": password
            }
        }
        try: # try block so the code won't throw a FileNotFoundError the first time it is launched
            with open("save_file.json", 'r') as load_file:
                # Reading data from file
                data = json.load(fp=load_file)

        except FileNotFoundError: # if the file is not found, it will create a new file and dump the data in it
            with open("save_file.json", "w") as save_file:
                json.dump(new_data, fp=save_file, indent=4)
        else: # if the file is found, it will update the data loaded from it with the new data then write it all to file again
            data.update(new_data)

            with open("save_file.json", 'w') as save_file:
                # writing the data back to the same file with the updated data
                json.dump(data, fp=save_file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        messagebox.showinfo(title="Success", message="Data saved successfully")


# ------------------ Find Password through File ------------------ #
def find_password():
    search_field = website_entry.get().title()
    try:
        with open("save_file.json", 'r') as load_file:
            data = json.load(load_file)

    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="Data File not found or not created yet")
        return

    if len(search_field) == 0:
        messagebox.showwarning(title="Warning", message="Please enter a website")
        return
    if search_field in data:
        email = data[search_field]["email"]
        password = data[search_field]["password"]
        messagebox.showinfo(title=f"Results for {search_field}", message=f"email: {email}\npassword: {password}")
    else:
        messagebox.showinfo(title="Results", message=f"No details for {search_field} exist.")




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

# Website Entry
website_entry = Entry(window, width=21)
website_entry.grid(row=1, column=1, sticky=EW)
website_entry.focus()

# Search Button
search_button = Button(text="Search" ,command=find_password, width=14)
search_button.grid(column=2, row=1, sticky=E)



# Email/Username Label
email_username_label= Label(window, text="Email/Username:")
email_username_label.grid(row=2, column=0)

# Email/Username Entry
email_username_entry = Entry(window, width=35)
email_username_entry.grid(row=2, column=1, columnspan=2, sticky=EW)
email_username_entry.insert(0, "")



# Password Label
password_label = Label(window, text="Password:")
password_label.grid(row=3, column=0)

# Password Entry
password_entry = Entry(window, width=21)
password_entry.grid(row=3, column=1, sticky=EW)

# Generate Password Button
generate_password_button = Button(window, text="Generate Password" ,command=generate_password)
generate_password_button.grid(row=3, column=2, sticky=E)

# Save button
save_button = Button(window, text="Save Password/Add password",width=36, command=save_data)
save_button.grid(row=4, column=1, columnspan=2, pady=2)

window.mainloop()
