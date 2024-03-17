# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import ttk
import random
import csv

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = inp1.get()
    email = inp2.get()
    password = inp3.get()

    with open(file="data.csv", mode='a', newline='') as f:
        csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([website, email, password])


def generate_password():
    char1 = '+-/*!&$#?=@<>'
    char2 = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    char3='1234567890'
    password =''
    for i in range(6,13):
        password += random.choice(char2)
    for i in range(2,6):
        password+= random.choice(char1)
    for i in range(2,5):
        password+= random.choice(char3)
    inp3.set(password)

def find_word():
    website_to_find = inp1.get()
    
    with open(file="data.csv", mode='r') as f:
        csv_reader = csv.reader(f, delimiter=',', quotechar='"')
        
        for row in csv_reader:
            if row and row[0] == website_to_find:
                found_password = row[2]
                inp3.set(found_password)
                break




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.configure(padx=50,bg='#DCFFB7')
window.minsize(500, 500)
canvas = Canvas()
img = PhotoImage(file='logo.png')
canvas.create_image(220,125,image=img)
canvas.grid(column=2, row=1)
inp1= StringVar()
inp2= StringVar()
inp3= StringVar()
input_web= Entry(textvariable = inp1).grid(column=2, row=2)
input_email = Entry(textvariable = inp2).grid(column=2, row=3)
input_passw = Entry(textvariable = inp3).grid(column=2, row=4)
label_web = Label(window, text='Website:', bg='#DCFFB7', font=('Helvetica', 16)).grid(column=1, row=2)
label_email = Label(window, text='Email/Username:', bg='#DCFFB7',font=('Helvetica', 16)).grid(column=1, row=3)
label_passw = Label(window, text='Password:', bg='#DCFFB7',font=('Helvetica', 16)).grid(column=1, row=4)
add= Button(window, text='ADD', command=save, height=1, width=17, bg="#FFEAA7").grid(column=2,row=5)
generate=Button(window, text='Generate password', command=generate_password, height=1, bg="#FFEAA7").grid(column=3,row=4)
find=Button(window, text='Find password', command=find_word, height=1, bg="#FFEAA7").grid(column=3,row=2)
window.mainloop()


# TODO Fix erros 
# TODO If password already is csv don't add it to csv
# TODO If password not found show messagebox
# TODO In your code there should be at least 1 try/catch block handling errors
# TODO If fileds are empty notify user 
# TODO If user wrote existing login and wrote new password update password data with button 
# TODO When password generated save it to the clipboard with pyperclip