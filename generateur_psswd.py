from tkinter import *
import string
import random

def generate_password():
    mixed= string.ascii_letters + string.digits
    psswd="".join(random.choice(mixed) for i in range(9))
    password_entry.delete(0, END)
    password_entry.insert(0, psswd)

window=Tk()
window.title("password")
window.minsize(480,360)
window.maxsize(600, 600)
window.config(background='gray')

#creation d;image 

#crreation de la frame principale
frame = Frame(window, bg='gray')

#afficher la frame
frame.pack(expand=YES)

#creer un champ 
password_entry= Entry(frame, font=("Helvetica", 20), bg='white', fg='black')
password_entry.pack()

#creer un bouton
password_entry_button= Button(frame, text="generer", font=("Helvetica", 20), bg='white', fg='black', command=generate_password)
password_entry_button.pack(fill=X)


window.mainloop()