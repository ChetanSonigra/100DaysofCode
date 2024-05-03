from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=200,height=200)
window.config(padx=20,pady=20)

input = Entry(width=10)
input.grid(column=1,row=0)

my_label = Label(text='Miles',font=('Arial',12,'normal'))
my_label.grid(column=2,row=0)

my_label1 = Label(text='is equal to',font=('Arial',12,'normal'))
my_label1.grid(column=0,row=1)

my_label2 = Label(text='0',font=('Arial',12,'normal'))
my_label2.grid(column=1,row=1)

my_label3 = Label(text='Km',font=('Arial',12,'normal'))
my_label3.grid(column=2,row=1)

def calculate():
    my_label2['text']=round(float(input.get())*1.609,2)

button = Button(text='Calculate',command=calculate)
button.grid(column=1,row=2)


window.mainloop()