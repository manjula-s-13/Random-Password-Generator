import tkinter
from tkinter import *
import random
import string
def fun():
    
    n=length_entry.get()
    caps_list=string.ascii_uppercase
    small_list=string.ascii_lowercase
    numbers=string.digits
    special_char=string.punctuation
    final=caps_list+small_list+numbers+special_char
    list=(random.sample(final,int(n)))
    password=''.join(list)
    print(password)
    Generated_Password_output=Label(window,text=password, font=("Algerian",18), bg="sky blue" , relief=RAISED ,  borderwidth=5) 
    Generated_Password_output.place(x=100 ,y=500, height=50 , width=500)
    
    

window=tkinter.Tk()
window.geometry('661x670+500+10')
window.title("RANDOM PASSWORD GENERATOR")
window.resizable(0,0)
window.configure(bg='gold')
name=Label(window,text=" RANDOM PASSWORD GENERATOR " , font=("Algerian",18),bg="light grey", relief=RAISED, borderwidth=5)
name.place(x=150 ,y=50)
heading=Label(window,text=" Enter the length of password " , font=("Algerian",18),bg="light grey", relief=RAISED, borderwidth=5) 
heading.place(x=50 ,y=170)
length_entry=Entry(window,font=('Times New Roman',20),bg="sky blue",fg="black")
length_entry.place(x=100 ,y=240, height=50 , width=500)
connect=Button(window,text=" CLICK" , font=("Algerian",18),bg="light grey", relief=RAISED, borderwidth=5,command=fun)
connect.place(x=250 , y=330 )
Generated_Password=Label(window,text="  Generated Password  " , font=("Algerian",18), bg="light grey" , relief=RAISED ,  borderwidth=5) 
Generated_Password.place(x=50,y=430)






























