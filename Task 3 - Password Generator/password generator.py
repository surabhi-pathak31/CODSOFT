import tkinter 
import random
import string 

main_window=tkinter.Tk()
main_window.title("Password Generator")
main_window.geometry('300x250')
main_window["padx"]=20
main_window["padx"]=20


length_var=tkinter.StringVar()

def generate_password():
    try:
        len_value = int(length_var.get())
        if len_value <= 0:
            raise ValueError("Length must be positive")
        valid_char = string.ascii_letters + string.digits
        password = "".join(random.sample(valid_char, len_value))
        display_result.delete(0, tkinter.END)
        display_result.insert(0, password)
    except ValueError:
        display_result.delete(0, tkinter.END)
        display_result.insert(0, "Enter valid number")

title_text=tkinter.Label(text="Password Generator")
title_text.grid(row=0, column=0,columnspan=2,pady=10)

tkinter.Label(text="Enter length:").grid(row=1,column=0)
length_entry=tkinter.Entry(textvariable=length_var)
length_entry.grid(row=1,column=1,padx=5,pady=5)

display_result=tkinter.Entry()
display_result.grid(row=2,column=0,columnspan=2,pady=10)

pass_generate=tkinter.Button(text="Generate",command=generate_password)
pass_generate.grid(row=5,column=0,columnspan=2,pady=10)

main_window.mainloop()