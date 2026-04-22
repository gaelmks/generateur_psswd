from tkinter import *
import string
import random

window=Tk()
window.title("password")
window.minsize(480,360)
window.maxsize(600, 600)
window.config(background='#4065A4')

#creation d;image 
mixed= string.ascii_letters + string.digits
psswd="".join(random.choice(mixed) for i in range(9))
print(f'mot de passe: {psswd}')

window.mainloop()