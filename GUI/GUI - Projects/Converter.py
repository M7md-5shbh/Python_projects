from tkinter import *

# Creating a new window and configurations
window = Tk()
window.config(padx=20, pady=20)
window.title("Converter")

miles_entry = Entry(width=20)
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles", padx=20)
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", padx=20)
equal_label.grid(column=0, row=1)

kilo_result_label = Label(text="0", padx=20)
kilo_result_label.grid(column=1, row=1)

kilo_label = Label(text="Km", padx=20)
kilo_label.grid(column=2, row=1)


def miles_to_km():
    miles = int(miles_entry.get())
    km = round(miles * 1.609, 1)
    kilo_result_label.config(text=f"{km}")


calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
