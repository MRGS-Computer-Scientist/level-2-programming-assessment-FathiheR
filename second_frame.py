from app_settings import *
from welcomepage import *

class SecondPage():
    second_frame = Frame(window, height=800, width=800)

    student_list = Listbox(second_frame)
    student_list.grid(row=3, column = 0)

    away_list = Listbox(second_frame)
    away_list.grid(row=3, column = 1)

    student_list.insert(0, "Tom")
    away_list.insert(0, "10")
    student_list.insert(0, "Alex")
    away_list.insert(0, "5")