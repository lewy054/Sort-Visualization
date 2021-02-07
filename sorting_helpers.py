
from secrets import randbelow
import tkinter as tk

def generate_numbers():
    numbers_to_sort = []
    how_many_numbers = 750
    for _ in range(how_many_numbers):
        numbers_to_sort.append(randbelow(500))
    return numbers_to_sort

def draw(numbers_to_sort):
    xoff = 0
    canvas = tk.Canvas()
    columns = []
    column_width = 2
    for i in numbers_to_sort:
        column = canvas.create_rectangle(xoff, 720, xoff+column_width, 600-i, outline="", fill="orange")
        columns.append(column)
        xoff += column_width
    return (canvas, columns)

def swap_two_columns(col1, col2, canvas):
    x_00, _, x_01, _ = canvas.coords(col1)
    x_10, _, x_11, _ = canvas.coords(col2)
    canvas.move(col1, x_10-x_00, 0)
    canvas.move(col2, x_01-x_11, 0)

def change_two_columns_color_red(col1, col2, canvas, columns):
    canvas.itemconfig(columns[col1], fill='red')
    canvas.itemconfig(columns[col2], fill='red')

def change_two_columns_color_orange(col1, col2, canvas, columns):
    canvas.itemconfig(columns[col1], fill='orange')
    canvas.itemconfig(columns[col2], fill='orange')