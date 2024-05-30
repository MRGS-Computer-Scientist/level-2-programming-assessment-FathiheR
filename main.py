bg_color="#4895c2"

# "Red", "Blue", "Greem"


from tkinter import *
window = Tk()
window.geometry("300x600")
window.configure(bg=bg_color)
window.title("Students tracker App")
question_label = Label(text="student tracker")
question_label.pack()



btn = Button(window, text = 'EXIT !', command = window.destroy) 
btn.pack(side = 'top')  

btn = Button(window, text = 'continue !', command = window.destroy)
btn.pack(side = 'top')  

from tkinter import *
newwindow = Tk()
window.geometry("300x600")


window.mainloop()