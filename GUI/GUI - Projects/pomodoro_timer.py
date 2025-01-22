# written by M7md-5shbh
# Pomodoro Timer which is a timer that works like this 
# a 3-time loop consisting of (25 mins of work then 5 mins short break)
# then a 20 minutes long break then repeats
#--------------------------------------------

from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    tick_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    work_sec = WORK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count = int(count)
    count_minutes = count // 60
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        global reps
        start_timer()
        marks = ""
        work_sessions = reps//2
        for _ in range(work_sessions):
            marks += "✔️"
        tick_label.config(text=marks)
    # else:
    #     window.after(1000, countdown, count - 1)
    #     count_in_seconds = 59
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(bg=YELLOW, fg=GREEN, text="Timer", font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_photo)
timer_text = canvas.create_text(103, 130, fill="black", text="00:00", font=(FONT_NAME, 20, "bold"))
canvas.grid(column=1, row=1, rowspan=2)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=3, ipadx=10, pady=10)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=3, ipadx=10, pady=10)


tick_label = Label(fg=GREEN, bg=YELLOW)
tick_label.grid(column=1, row=4)
window.mainloop()
