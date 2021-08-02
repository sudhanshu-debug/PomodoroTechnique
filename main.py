from tkinter import *
import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 40
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(show_countdown, text="00:00")
    label_check.config(text = "")
    global reps, check
    reps = 0
    check = ""
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0 :
        label.config(text="Break", fg =RED)
        countdown(LONG_BREAK_MIN*60)
    elif reps % 2 == 1:
        label.config(text="Work", fg = GREEN)
        countdown(WORK_MIN*60)

    else :
        label.config(text="Break", fg = PINK)
        countdown(SHORT_BREAK_MIN*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    if count >= 0:
        min = int(count/60)
        sec = count%60
        if sec<10:
            sec = "0"+str(sec)
        if len(str(min))<2:
            min = "0"+str(min)
        time = f"{min}:{sec}"
        canvas.itemconfig(show_countdown, text = time)
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        playsound.playsound("alert.wav")
        global check
        for _ in range(int(reps/2)):
            check += "✔"
        label_check.config(text = check)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)
label = Label(text = "Timer", fg = GREEN, bg = YELLOW)
label.config(font = (FONT_NAME, 50, "bold"))
label.grid(column=1, row=0)
tomato_image =  PhotoImage(file = "tomato.png")
canvas = Canvas(width = 200, height = 223, bg = YELLOW, highlightthickness = 0)
canvas.create_image(100, 112, image = tomato_image)
show_countdown = canvas.create_text(103, 130, text = "00:00",fill = "white", font  = (FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row = 1)
label_check = Label(fg = GREEN, bg = YELLOW)
label_check.config(font = (FONT_NAME, 14, "bold"))
label_check.grid(column=1, row=3)
start_button = Button(text = "Start",command = start_timer ,width = 7, highlightthickness = 0)
start_button.grid(column = 0, row = 2)
reset_button = Button(text = "Reset", width = 7, highlightthickness = 0, command = reset)
reset_button.grid(column = 2, row = 2)
window.mainloop()
