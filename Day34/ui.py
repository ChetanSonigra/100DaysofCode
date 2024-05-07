THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain
import time

class QuizInterface:
    def __init__(self,quizbrain:QuizBrain) -> None:
        self.quiz = quizbrain
        self.timer = None
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        
        self.score = Label(text=f'Score: {self.quiz.score}',bg=THEME_COLOR,fg='white')
        self.score.grid(row=0,column=1,padx=20,pady=20)
        
        self.canvas = Canvas(width=300, height=250,bg='white')
        self.question_text = self.canvas.create_text(150,125
                                                     ,text='Question Here'
                                                     ,fill=THEME_COLOR
                                                     ,width=280
                                                     ,font=('Arial',20,'italic'))
        self.canvas.grid(row=1,column=0,columnspan=2,padx=20,pady=20)
        
        self.right_image = PhotoImage(file='Day34/images/true.png')
        self.right = Button(image=self.right_image,highlightthickness=0,command=self.check_right_answer)
        self.right.grid(row=2,column=0,padx=20,pady=20)
        
        self.wrong_image = PhotoImage(file='Day34/images/false.png')
        self.wrong = Button(image=self.wrong_image,highlightthickness=0,command=self.check_wrong_answer)
        self.wrong.grid(row=2,column=1,padx=20,pady=20)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.score['text']=f'Score: {self.quiz.score}'
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text= self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text='You have reached end of game.')
            self.right.config(state='disabled')
            self.wrong.config(state='disabled')
        
    def check_right_answer(self):
        result = self.quiz.check_answer('True')
        if result:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.timer = self.window.after(1000,self.get_next_question)
        
        
    def check_wrong_answer(self):
        result = self.quiz.check_answer('False')
        if result:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.timer = self.window.after(1000,self.get_next_question)
    