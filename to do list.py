import tkinter
import random

root=tkinter.Tk()
root.configure(bg="white")
root.title("My Super To Do List")
root.geometry("325x275")

tasks=[]

def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end",task)

def clear_listbox():
    lb_tasks.delete(0,"end")

def add_task():
    task=txt_input.get()
    if task !="":
        tasks.append(task)
        update_listbox()
    else:
        lbl_display["text"]="Please enter a task."
    txt_input.delete(0,"end")

def del_all():
    global tasks
    tasks=[]
    update_listbox()

def del_one():
    task=lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
    update_listbox()

def mark():
    pos=lb_tasks.curselection()
    if pos:
        index=pos[0]
        text=lb_tasks.get(index)
        lb_tasks.delete(index)
        lb_tasks.insert(tkinter.END,f"{text} \u2713")
    else:
        print("No task selected")

def show_number_of_tasks():
    number_of_tasks=len(tasks)
    msg=f"Number of tasks: {number_of_tasks}"
    lbl_display["text"]=msg

lbl_title=tkinter.Label(root,text="To-Do-List",bg="white")
lbl_title.grid(row=0,column=0)

lbl_display=tkinter.Label(root,text="",bg="white")
lbl_display.grid(row=0,column=1)

txt_input=tkinter.Entry(root,width=15)
txt_input.grid(row=1,column=1)

btn_add_task=tkinter.Button(root,text="Add task",fg="black",bg="pink",command=add_task)
btn_add_task.grid(row=1,column=0)

btn_del_all=tkinter.Button(root,text="Delete All",fg="black",bg="pink",command=del_all)
btn_del_all.grid(row=2,column=0)

btn_del_one=tkinter.Button(root,text="Delete",fg="black",bg="pink",command=del_one)
btn_del_one.grid(row=5,column=0)

btn_mark=tkinter.Button(root,text="Mark",fg="black",bg="pink",command=mark) 
btn_mark.grid(row=6,column=0)

btn_number_of_tasks=tkinter.Button(root,text="Number of tasks",fg="black",bg="pink",command=show_number_of_tasks)
btn_number_of_tasks.grid(row=7,column=0)

btn_exit=tkinter.Button(root,text="Exit",fg="black",bg="pink",command=exit)
btn_exit.grid(row=8,column=0)

lb_tasks=tkinter.Listbox(root)
lb_tasks.grid(row=2,column=1,rowspan=7)

root.mainloop()