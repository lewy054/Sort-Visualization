from insertion_sort import InsertionSort
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from quick_sort import QuickSort
from bubble_sort import BubbleSort


class Menu(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.create_title()
        self.create_combobox()
        self.create_buttons()

    def create_title(self):
        title = tk.Label(self, text="Sort Visualization", fg='blue')
        myFont = Font(family="Roboto", size=44)
        title.config(font=myFont)
        title.pack(pady=30)

    def create_combobox(self):
        combo_label = tk.Label(self, text="Select type of sorting :")
        myFont = Font(family="Roboto", size=24)
        combo_label.config(font=myFont)
        combo_label.pack(pady=30)
        self.box_value = tk.StringVar()
        self.sort_type = ttk.Combobox(self, width=27, textvariable=self.box_value, state="readonly")
        self.sort_type['values'] = ('QuickSort',
                                    'BubbleSort',
                                    'InsertionSort')
        self.sort_type.current(0)
        self.sort_type.pack()

    def create_buttons(self):
        start_button = tk.Button(self, text="Start", bg='green', fg='white', command=self.start)
        myFont = Font(family="Roboto", size=24)
        start_button.config(font=myFont)
        start_button.pack(pady=30)

    def start(self):
        selected_sort = self.sort_type.get()
        if(selected_sort == 'BubbleSort'):
            self.master.change(BubbleSort)
        elif(selected_sort == 'QuickSort'):
            self.master.change(QuickSort)
        elif(selected_sort == 'InsertionSort'):
            self.master.change(InsertionSort)


def main():
    root = Menu()
    root.mainloop()
