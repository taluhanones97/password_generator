from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
photo = PhotoImage(file="logo.png")

canvas.create_image(100,100,image=photo)
canvas.grid(row=0,column=1)

label_1=Label(text="Website: ")
label_1.grid(row=1,column=0)

label_2=Label(text="Email/Username: ")
label_2.grid(row=2,column=0)

label_3=Label(text="Password: ")
label_3.grid(row=3,column=0)

website=Entry(width=35)
website.grid(row=1,column=1,columnspan=2,sticky=EW)
website.focus()

e_mail=Entry(width=35)
e_mail.grid(row=2,column=1,columnspan=2,sticky=EW)
e_mail.insert(0,"otaluhan@gmail.com")
passwor=Entry(width=21)
passwor.grid(row=3,column=1,sticky=EW)

def add_info():
    if len(website.get())==0 or len(passwor.get())==0:
        warningtext=messagebox.showinfo(message="Dont leave website/e-mail empty")
    else:
        with open("data.txt",mode="a") as file:
            text= str(website.get())+" | "+ str(e_mail.get())+" | "+ str(passwor.get()+"\n")
            save_text=messagebox.askokcancel(title=website,message=f"Those are the details {text}, is it okey to save")
            if save_text:
                file.write(text)
                website.delete(0,END)
                passwor.delete(0,END)

add=Button(text="Add",width=36,command=add_info)
add.grid(row=4,column=1,columnspan=2,sticky=EW)


#Password Generator Project
import random

def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)





    letter_list=[random.choice(letters) for _ in range(nr_letters)]
    symbol_list=[random.choice(symbols) for _ in range(nr_symbols)]
    number_list=[random.choice(numbers) for _ in range(nr_numbers)]

    password_list=letter_list+symbol_list+number_list

    random.shuffle(password_list)

    password="".join(password_list)
    passwor.insert(0,password)



gen_pass=Button(text="Generate password",command=gen_password)
gen_pass.grid(row=3,column=2)

window.mainloop()



