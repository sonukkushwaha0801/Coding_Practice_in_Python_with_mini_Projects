#how to crack password using brute force method in python
#lets gets started

import random
from tkinter import *

root = Tk()
def submit():
    pass_real = pass_value.get()
    pass_characters = "0123456789abcdefghijklmnopqrstuvwxyz"
    pass_characters_list = list(pass_characters)
    pass_guess = ""

    while(pass_guess !=pass_real):
        pass_guess = random.choices(pass_characters_list,k=len(pass_real))
        print(pass_guess)
        if (pass_guess == list(pass_real)):
            print(pass_guess)
            break
    Label(root,text="Your Password is: "+''.join(map(str,pass_guess)),fg='red',font='arial 17').place(x=80,y=200)


root.geometry('500x350')
root.title("Password Cracker")
bg_img = PhotoImage(file='pass_bg.png')
img = Label(root,image=bg_img)
img.pack()
pass_value = StringVar()
Label(root,text="Enter Your Password",fg="green",font="arial 17").place(x=25,y=120)
pass_entry = Entry(root,textvariable=pass_value,width=15,bd=2,show="*",font="arial 17").place(x=280,y=120)
btn = Button(root,text="Submit",font=15,width=10,height=2,command=submit)
btn.place(x=180,y=270)
root.mainloop()
