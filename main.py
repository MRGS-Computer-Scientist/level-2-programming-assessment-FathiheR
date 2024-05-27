from tkinter import *
window = Tk()
window.geometry("300x600")
window.title("Students tracker App")
question_label = Label(text="student tracker")
question_label.pack()

btn = Button(window, text = 'EXIT !', 
                command = window.destroy) 

btn.pack(side = 'top')  

btn = Button(window, text = 'continue !', 
                command = window.destroy)

btn.pack(side = 'top')  


window.mainloop()