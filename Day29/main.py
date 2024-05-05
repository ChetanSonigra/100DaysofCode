# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
import pyperclip,json
from tkinter import *
import tkinter.messagebox as tkm
from password_generator import generate_password

window = Tk()
window.title('Password Manager')
# window.minsize(240,240)
window.config(padx=20,pady=20)


def search_website():
    website = application_input.get()
    try:
        with open('Day29/data.json','r') as f:
            data_dict = json.load(f)
            tkm.showinfo(title=website,message=f"Email: {data_dict[website]['email']}\nPassword: {data_dict[website]['password']}")
    except:
        tkm.showinfo(title='Error', message=f"Data for {website} doesn't exist")   

def show_password():
    password= generate_password()
    password_input.insert(0,password)
    pyperclip.copy(password)


def add_to_file():
    website = application_input.get()
    email = username_input.get()
    passwd = password_input.get()
    new_data = {website:{'email': email,'password': passwd}}
    if len(passwd)==0 or len(website)==0:
        tkm.showinfo(title='Oops',message=f"Make sure you haven't left any field empty.")
    else:
        is_ok = tkm.askokcancel(title=f'{website}',message=f"These are the details entered: \nEmail: {email} "
                                                    f"\nPassword: {passwd}\nIs it okay to save?"
                                                    )
        if is_ok:
            try: 
                with open('Day29/data.json','r') as f:
                    data = json.load(f)
                    data.update(new_data)
                    # print(data)
            except:
                data = new_data
            with open('Day29/data.json','w') as f:
                json.dump(data,f,indent=4)
            application_input.delete(0,END)
            password_input.delete(0,END)

img = PhotoImage(file='Day29/logo.png')

canvas = Canvas(width=200,height=200)
canvas.create_image(100,100,image=img)
canvas.grid(column=1,row=0)

application= Label(text='Website: ',font=('Arial',12,'normal'))
application.grid(column=0,row=1)

application_input= Entry(width=34)
application_input.grid(column=1,row=1)
application_input.focus()

search_button = Button(text='Search',command=search_website,width=15)
search_button.grid(column=2,row=1)

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