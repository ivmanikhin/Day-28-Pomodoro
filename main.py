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

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    if reps == 6:
        count_down(20 * 60)
    elif reps % 2 == 1:
        count_down(5 * 60)
    else:
        count_down(25 * 60)
    reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    mins = str(int(count / 60)).rjust(2, "0")
    secs = str(count % 60).rjust(2, "0")
    tomato.itemconfig(timer_text, text=f"{mins}:{secs}")
    if count > 0:
        window.after(1000, count_down, count-1)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.minsize()
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer", font=(FONT_NAME, 36, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

tomato = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
tomato.create_image(100, 112, image=tomato_pic)
timer_text = tomato.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill='white')
tomato.grid(row=1, column=1)


button_start = Button(text="Start", font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", font=(FONT_NAME, 12, "bold"), highlightthickness=0)
button_reset.grid(row=2, column=2)

checkmark = Label(text="✔", font=(FONT_NAME, 20), fg=GREEN)
checkmark.grid(row=3, column=1)

window.mainloop()