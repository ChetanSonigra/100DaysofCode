BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random


def change_card():
    global new_image,word
    canvas.itemconfig(canvas_image,image=new_image)
    canvas.itemconfig(canvas_title,text='English',fill='white')
    canvas.itemconfig(canvas_text,text=word['English'],fill='white')
    

def change_word():
    global word,timer
    window.after_cancel(timer)
    another_word = word
    while another_word==word:
        another_word =random.choice(data_dict)
    word=another_word
    canvas.itemconfig(canvas_text,text=word['French'],fill='black')
    canvas.itemconfig(canvas_image,image=old_image)
    canvas.itemconfig(canvas_title,text='French',fill='black')
    timer = window.after(3000,change_card)

def is_known():
    data_dict.remove(word)
    df =  pd.DataFrame(data_dict)
    df.to_csv('Day31/data/words_to_learn.csv',index=False)
    change_word()

try:
    data_df=pd.read_csv('Day31/data/words_to_learn.csv')
except:
    data_df = pd.read_csv('Day31/data/french_words.csv')
data_dict = data_df.to_dict(orient='records')

word = random.choice(data_dict)

window = Tk()
window.title('Flashy')
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)


canvas = Canvas(width=800,height=450,highlightthickness=0,bg=BACKGROUND_COLOR)
old_image = PhotoImage(file='Day31/images/card_front.png')
new_image = PhotoImage(file='Day31/images/card_back.png')
canvas_image =canvas.create_image(400,200,image=old_image)
canvas_title =canvas.create_text(400,150,text='French',font=('Arial',40,'italic'))
canvas_text = canvas.create_text(400,263,text=f"{word['French']}",font=('Arial',60,'bold'))
canvas.grid(column=0,row=0,columnspan=2)


wrong_image = PhotoImage(file='Day31/images/wrong.png')
wrong_button = Button(image=wrong_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=change_word)
wrong_button.grid(column=0,row=1)

right_image = PhotoImage(file='Day31/images/right.png')
right_button = Button(image=right_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=is_known)
right_button.grid(column=1,row=1)


timer = window.after(3000,change_card)




window.mainloop()