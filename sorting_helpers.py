
from secrets import randbelow
import tkinter as tk
import time

def generate_numbers():
    numbers_to_sort = []
    how_many_numbers = 10
    for _ in range(how_many_numbers):
        numbers_to_sort.append(randbelow(500))
    return numbers_to_sort

def draw(numbers_to_sort):
    xoff = 0
    canvas = tk.Canvas()
    columns = []
    column_width = 16
    for i in numbers_to_sort:
        column = canvas.create_rectangle(xoff, 720, xoff+column_width, 600-i, outline="black", fill="orange")
        columns.append(column)
        xoff += column_width
    return (canvas, columns)

def swap_two_columns(col1, col2, canvas):
    x_00, _, x_01, _ = canvas.coords(col1)
    x_10, _, x_11, _ = canvas.coords(col2)
    canvas.itemconfig(col1, fill='red')
    canvas.itemconfig(col2, fill='pink')
    canvas.move(col1, x_10-x_00, 0)
    canvas.move(col2, x_01-x_11, 0)
    canvas.itemconfig(col1, fill='orange')
    canvas.itemconfig(col2, fill='orange')

def replace_column(col1, col2, canvas, columns):
    # x_00, _, x_01, _ = canvas.coords(col1)
    x1, y1, x2, y2 = canvas.coords(col1)
    x11, y11, x21, y22 = canvas.coords(col2)
    canvas.itemconfig(col1, fill='red')
    canvas.itemconfig(col2, fill='pink')
    canvas.coords(col1, x1, y11, x2, y22)
    canvas.itemconfig(col1, fill='blue')
    canvas.itemconfig(col2, fill='green')
    # canvas.delete(col1)
    # canvas.move(col2, x_01-x_11, 0)
    canvas.itemconfig(col1, fill='orange')
    canvas.itemconfig(col2, fill='orange')

def draw_column(column, where, canvas, columns):
    x1, y1, x2, y2 = canvas.coords(column)
    column = canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="orange")
    columns.insert(where, column)
