from app_settings import *
from tkinter import *

window = Tk()
window.geometry("800x800")
window.configure(bg=bg_color)
window.title("Students tracker App")

question_label = Label(text="Student Tracker")
question_label.grid(row=0, column=0, columnspan=2)

btn = Button(window, text = 'Continue !', command = window.destroy)
btn.grid(row=2, column=0, columnspan=2)

btn = Button(window, text = 'EXIT !', command = window.destroy) 
btn.grid(row=1, column=0, columnspan=2)  

newwindow = Tk()
newwindow.geometry("800x800")




student_list = Listbox(newwindow)
student_list.grid(row=3, column = 0)

away_list = Listbox(newwindow)
away_list.grid(row=3, column = 1)

student_list.insert(0, "Tom")
away_list.insert(0, "10")
student_list.insert(0, "Alex")
away_list.insert(0, "5")

window.mainloop()