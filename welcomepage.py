from tkinter import *
from app_settings import * 



def open_second_frame():

    global window
    window.withdraw()  # Hide the main window

    second_window = Toplevel(window)
    second_window.geometry("800x800")
    second_window.title("Students Tracker App")

    second_frame = Frame(second_window, bg=bg_color)  # No need to specify height and width here
    second_frame.pack(fill=BOTH, expand=True)  # Use pack instead of grid for filling the frame
  
    Student_list = Listbox(second_frame)
    Student_list.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Add padding and sticky

    Toilet_list = Listbox(second_frame)
    Toilet_list.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")  # Add padding and sticky

    Deans_list = Listbox(second_frame)
    Deans_list.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")  # Add padding and sticky

    Stundentservice_list = Listbox(second_frame)
    Stundentservice_list.grid(row=0, column=4, padx=10, pady=10, sticky="nsew")


    Other_list = Listbox(second_frame)
    Other_list.grid(row=0, column=5, padx=10, pady=10, sticky="nsew")


    Student_list.insert(0, "Tom")  
    Student_list.insert(0, "Jack")
    Student_list.insert(0, "Alex")
    Student_list.insert(0, "Jarry")
    Student_list.insert(0, "Luke")
    Student_list.insert(0, "Emma")
    Student_list.insert(0, "Cole")
    Student_list.insert(0, "Nico")


    Toilet_list.insert(0, "4") 
    Toilet_list.insert(0, "2")
    Toilet_list.insert(0, "2")
    Toilet_list.insert(0, "1")
    Toilet_list.insert(0, "0")
    Toilet_list.insert(0, "1")
    Toilet_list.insert(0, "3")
    Toilet_list.insert(0, "2")

    Deans_list.insert(0, "2")  
    Deans_list.insert(0, "0")
    Deans_list.insert(0, "0")
    Deans_list.insert(0, "0")
    Deans_list.insert(0, "0")
    Deans_list.insert(0, "0")
    Deans_list.insert(0, "1")
    Deans_list.insert(0, "0")
    
    Stundentservice_list.insert(0, "0")  
    Stundentservice_list.insert(0, "1")
    Stundentservice_list.insert(0, "0")
    Stundentservice_list.insert(0, "0")
    Stundentservice_list.insert(0, "0")
    Stundentservice_list.insert(0, "1")
    Stundentservice_list.insert(0, "0")
    Stundentservice_list.insert(0, "0")

    Other_list.insert(0, "3")  
    Other_list.insert(0, "0")
    Other_list.insert(0, "3")
    Other_list.insert(0, "0")
    Other_list.insert(0, "0")
    Other_list.insert(0, "0")
    Other_list.insert(0, "4")
    Other_list.insert(0, "1")



window = Tk()
window.geometry("800x800")
window.title("Students Tracker App")
first_frame = Frame(window,  bg=bg_color, width=800, height=800)
first_frame.pack(fill=BOTH, expand=True)

question_label = Label(first_frame, text="Student Tracker")
question_label.grid(row=0, column=0, columnspan=2)





def close_second_frame():
    global window
    window.withdraw()  # Hide the main window

    second_window = Toplevel(window)
    second_window.geometry("800x800")
    second_window.title("Students Tracker App")

    second_frame = Frame(second_window)  # No need to specify height and width here
    second_frame.pack(fill=BOTH, expand=True)  # Use pack instead of grid for filling the frame


def close_first_frame():
    global window
    window.withdraw()  # Hide the main window

    first_window = Tk()
    first_window.geometry("800x800")
    first_window.title("Students Tracker App")

    first_frame = Frame( first_window,  bg=bg_color)  # No need to specify height and width here
    first_frame.pack(fill=BOTH, expand=True)  # Use pack instead of grid for filling the frame

question_label = Label(first_frame, text="Student Tracker")
question_label.grid(row=0, column=0, columnspan=2)

btn_continue = Button(first_frame, text='Continue!', command=open_second_frame)
btn_continue.grid(row=2, column=0, columnspan=2)

btn_exit = Button(first_frame, text='EXIT!', command=close_first_frame)
btn_exit.grid(row=1, column=0, columnspan=2)



def close_second_frame():
    global window
    window.withdraw()  # Hide the main window

    first_window = Tk()
    first_window.geometry("800x800")
    first_window.title("Students Tracker App")

    first_frame = Frame( first_window,  bg=bg_color)  # No need to specify height and width here
    first_frame.pack(fill=BOTH, expand=True)  # Use pack instead of grid for filling the frame

question_label = Label(first_frame, text="Student Tracker")
question_label.grid(row=0, column=0, columnspan=2)

btn_continue = Button(first_frame, text='Continue!', command=open_second_frame)
btn_continue.grid(row=2, column=0, columnspan=2)

btn_exit = Button(first_frame, text='EXIT!', command=close_second_frame)
btn_exit.grid(row=1, column=0, columnspan=2)



window.mainloop()
