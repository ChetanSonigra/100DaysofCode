# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
import pyperclip
from tkinter import *
import tkinter.messagebox as tkm
from password_generator import generate_password

window = Tk()
window.title('Password Manager')
# window.minsize(240,240)
window.config(padx=20,pady=20)

def show_password():
    password= generate_password()
    password_input.insert(0,password)
    pyperclip.copy(password)


def add_to_file():
    website = application_input.get()
    email = username_input.get()
    passwd = password_input.get()
    if len(passwd)==0 or len(website)==0:
        tkm.showinfo(title='Oops',message=f"Make sure you haven't left any field empty.")
    else:
        is_ok = tkm.askokcancel(title=f'{website}',message=f"These are the details entered: \nEmail: {email} "
                                                    f"\nPassword: {passwd}\nIs it okay to save?"
                                                    )
        if is_ok:
            with open('Day29/password_manager.txt','+a') as f:
                f.write(f'{website}    |    {email}    |    {passwd}\n')

            application_input.delete(0,END)
            password_input.delete(0,END)

img = PhotoImage(file='Day29/logo.png')

canvas = Canvas(width=200,height=200)
canvas.create_image(100,100,image=img)
canvas.grid(column=1,row=0)

application= Label(text='Website: ',font=('Arial',12,'normal'))
application.grid(column=0,row=1)

application_input= Entry(width=53)
application_input.grid(column=1,row=1,columnspan=2)
application_input.focus()

username= Label(text='Email/Username: ',font=('Arial',12,'normal'))
username.grid(column=0,row=2)
# print(username.grid_info())

username_input = Entry(width=53)
username_input.grid(column=1,row=2,columnspan=2)
# print(username_input.grid_info())
username_input.insert(0,'chetan@gmail.com')   # starting text

password = Label(text='Password: ',font=('Arial',12,'normal'))
password.grid(column=0,row=3)

password_input = Entry(width=34)
password_input.grid(column=1,row=3)
# print(password_input.grid_info())

generate_pwd = Button(text='Generate Password',command=show_password)
generate_pwd.grid(column=2,row=3)
# print(generate_pwd.grid_info())

add = Button(text='Add',command=add_to_file,width=45)
add.grid(column=1,row=4,columnspan=2)


window.mainloop()