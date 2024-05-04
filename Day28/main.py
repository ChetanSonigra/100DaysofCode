
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    mins= count//60
    secs=count%60
    if secs < 10:
        if secs==0:
            secs='00'
        else:
            secs=f'0{secs}'
    canvas.itemconfig(time_text,text=f'{mins}:{secs}')
    if count>0:
        timer = window.after(1000,count_down,count-1)
    elif REPS<8:
        start_pomodoro()
        checkmarks['text']='✔'*(REPS//2)
        
        
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_pomodoro():
    global REPS
    REPS=0
    window.after_cancel(timer)
    canvas.itemconfig(time_text,text='00:00')
    checkmarks['text']=''
    timer_label.config(text='Timer',fg=GREEN)
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_pomodoro():
    global REPS
    REPS += 1
    work_secs = int(WORK_MIN*60)
    short_break_secs = int(SHORT_BREAK_MIN*60)
    long_break_secs = int(LONG_BREAK_MIN*60)
    if REPS %8==0:
        timer_label.config(text='Break',fg=RED)
        count_down(long_break_secs)
    elif REPS %2==0:
        timer_label.config(text='Break',fg=PINK)
        count_down(short_break_secs)
    else:
        timer_label.config(text='Work',fg=GREEN)
        count_down(work_secs)


            

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.title('Pomodoro')
# window.minsize(400,400)
window.config(padx=100,pady=50,bg=YELLOW)


timer_label = Label(text='Timer',fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,'bold'))
timer_label.grid(column=1,row=0)
# print(timer_label,timer_label.grid_info())

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file='Day28/tomato.png')
canvas.create_image(100,112,image=tomato_img)
time_text=canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(column=1,row=1)
# print(canvas,canvas.grid_info())

start_button = Button(text='Start',command=start_pomodoro)
start_button.grid(column=0,row=2)
# print(start_button,start_button.grid_info())

reset_button = Button(text='Reset',command=reset_pomodoro)
reset_button.grid(column=2,row=2)
# print(reset_button,reset_button.grid_info())

checkmarks = Label(text='',fg=GREEN,bg=YELLOW,font=(FONT_NAME,28,'bold'))
checkmarks.grid(column=1,row=3)
# print(checkmarks,checkmarks.grid_info())

# print(window.grid_size())
window.mainloop()


# Dynamically typed langauge:
# you can assign different type of data to same variable. which is not possible in other langauges.