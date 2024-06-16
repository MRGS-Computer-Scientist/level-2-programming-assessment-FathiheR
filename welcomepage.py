from tkinter import *
from app_settings import * 


def open_second_frame():
    global window
    window.withdraw()  # Hide the main window

    second_window = Toplevel(window)
    second_window.geometry("800x800")
    second_window.title("Students Tracker App")

    second_frame = Frame(second_window)  # No need to specify height and width here
    second_frame.pack(fill=BOTH, expand=True)  # Use pack instead of grid for filling the frame

    student_list = Listbox(second_frame)
    student_list.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Add padding and sticky

    away_list = Listbox(second_frame)
    away_list.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")  # Add padding and sticky

    student_list.insert(END, "Tom")  # Use END to insert at the end of the list
    away_list.insert(END, "10")
    student_list.insert(END, "Alex")
    away_list.insert(END, "5")

    
    def close_first_frame():
       close_first_frame.destroy()
        
    first_frame.protocol("WM_DELETE_WINDOW", second_window)


window = Tk()
window.geometry("800x800")
window.title("Students Tracker App")

first_frame = Frame(window, height=800, width=800)
first_frame.grid(row=0, column=0)

question_label = Label(first_frame, text="Student Tracker")
question_label.grid(row=0, column=0, columnspan=2)

btn_continue = Button(first_frame, text='Continue!', command=open_second_frame)
btn_continue.grid(row=2, column=0, columnspan=2)

btn_exit = Button(first_frame, text='EXIT!', command=close_first_frame)
btn_exit.grid(row=1, column=0, columnspan=2)



window.mainloop()
