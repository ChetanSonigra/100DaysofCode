import tkinter

window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)  # padding for overall window.


# Label:
my_label = tkinter.Label(text='I am a Label',font=('Arial',24,'italic'))
my_label.pack(expand=False)          # side = left,right,bottom,top
# my_label.place(x=0,y=0)
# changing text of label
my_label['text']='New Text'
# or my_label.config(text='New Text')
my_label.config(padx=50,pady=50)


# Button

def button_clicked():
    my_label['text']=input.get()
button = tkinter.Button(text='Click Me',command=button_clicked)
# button.grid(column=0,row=0)


# Entry
input = tkinter.Entry(width=10)
input.pack()
print(input.get())
# input.grid(column=1,row=1)


# Text
text = tkinter.Text(height=5,width=30)
text.focus()
text.insert(tkinter.END,'Example of multiline text entry.')
# get current value in textbox at line 1 char 0
print(text.get('1.0',tkinter.END))
text.pack()


# Spinbox
def spinbox_used():
    print(spinbox.get())
spinbox = tkinter.Spinbox(from_=0,to=10,width=5,command=spinbox_used)


# Scale
def scale_used(value):
    print(value)

scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()


# checkbutton

def checkbutton_used():
    print(checked_state.get())

checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text='Is On?',variable=checked_state,command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# radio button used
def radiobutton_used():
    print(radiostate.get())
    
radiostate = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text='Option1', value=1,variable=radiostate,command=radiobutton_used)
radiobutton2 = tkinter.Radiobutton(text='Option2',value=2,variable=radiostate,command=radiobutton_used)
radiobutton1.pack()
radiobutton2.pack()


# listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4)
fruits = ['Apple','Pear','Orange','Banana']
for item in fruits:
    listbox.insert(fruits.index(item),item)
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()
    
# Layout Managers:
# 1. pack 2. place 3. grid
# 1. pack - packs items one by one. but position can't be precise.
# 2. place - can put anywhere using x,y coordinates.
# 3. grid - can put items in any part of grid.
# like button.grid(column=0,row=0), input.grid(column=1,row=1)
# can't mix pack and grid in same program.


window.mainloop()


# arguments with default values
def my_function(a=1,b=2,c=4):
    print(a+b+c)
    
my_function(b=5)

# Unlimited positional arguments *args
def add(*args):
    print(args)          # tuple
    sum=0
    for n in args:
        sum+=n
    return sum
add(2,5,7,3)

# Unlimited  keyword arguments **kwargs

def calculate(**kwargs):
    print(kwargs)         # dictionary
    
calculate(add=4,multiply=6)