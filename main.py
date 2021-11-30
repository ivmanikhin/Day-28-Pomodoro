from tkinter import *
from winsound import *
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
is_on = True
checkmarks = ""

# ---------------------------- SOUNDS ------------------------------- #


def zoomer():
    return PlaySound("click_one.wav", SND_ASYNC | SND_ALIAS)

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global reps, is_on, checkmarks
    reps = 0
    is_on = False
    count_down(0)
    timer_label.config(text="Timer", font=(FONT_NAME, 36, "bold"), fg=GREEN)
    checkmarks = ""
    checkmark.config(text=checkmarks)

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps, is_on, checkmarks
    is_on = True
    reps += 1
    button_start.config(state=DISABLED)
    if reps == 8:
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
        checkmarks += "✔ "
        checkmark.config(text=checkmarks)
        window.attributes('-topmost', True)
        return
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
        checkmarks += "✔ "
        checkmark.config(text=checkmarks)
        window.attributes('-topmost', True)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)
        window.attributes('-topmost', False)

    if reps == 9:
        reset()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global is_on

    mins = str(int(count / 60)).rjust(2, "0")
    secs = str(count % 60).rjust(2, "0")
    tomato.itemconfig(timer_text, text=f"{mins}:{secs}")
    if count > 0 and is_on:
        window.after(1, count_down, count-1)
    elif count == 0 and is_on:
        start_timer()
        zoomer()
    else:
        button_start.config(state=NORMAL)
        tomato.itemconfig(timer_text, text=f"00:00")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.minsize()
window.config(padx=60, pady=15, bg=YELLOW)


timer_label = Label(text="Timer", font=(FONT_NAME, 36, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

tomato = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
tomato.create_image(100, 112, image=tomato_pic)
timer_text = tomato.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill='white')
tomato.grid(row=1, column=1)


button_start = Button(text="Start", font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=reset)
button_reset.grid(row=2, column=2)

checkmark = Label(text=checkmarks, font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
checkmark.grid(row=3, column=1)

window.mainloop()