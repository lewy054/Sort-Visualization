from coctail_shaker_sort import CoctailShakerSort
from heap_sort import HeapSort
from selection_sort import SelectionSort
import tkinter as tk
from tkinter import ttk
from quick_sort import QuickSort
from bubble_sort import BubbleSort
from bubble_sort_recursive import BubbleSortRecursive


class Menu(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.create_title()
        self.create_combobox()
        self.create_buttons()

    def create_title(self):
        title = tk.Label(self, text="Sort Visualization", fg='blue')
        title.config(font=("Helvetica", 44))
        title.pack(pady=30)

    def create_combobox(self):
        combo_label = tk.Label(self, text="Select type of sorting :", font=24)
        combo_label.config(font=("Helvetica", 24))
        combo_label.pack(pady=30)
        self.box_value = tk.StringVar()
        self.sort_type = ttk.Combobox(self, width=27, textvariable=self.box_value, state="readonly")
        self.sort_type['values'] = ('QuickSort',
                                    'BubbleSort',
                                    'BubbleSortRecursive',
                                    'SelectionSort',
                                    'HeapSort',
                                    'CoctailShakerSort')
        self.sort_type.current(0)
        self.sort_type.pack()

    def create_buttons(self):
        start_button = tk.Button(self, text="Start", bg='green', fg='white', command=self.start)
        start_button.config(font=("Helvetica", 24))
        start_button.pack(pady=30)

    def start(self):
        selected_sort = self.sort_type.get()
        if(selected_sort == 'BubbleSort'):
            self.master.change(BubbleSort)
        elif(selected_sort == 'QuickSort'):
            self.master.change(QuickSort)
        elif(selected_sort == 'SelectionSort'):
            self.master.change(SelectionSort)
        elif(selected_sort == 'HeapSort'):
            self.master.change(HeapSort)
        elif(selected_sort == 'BubbleSortRecursive'):
            self.master.change(BubbleSortRecursive)
        elif(selected_sort == 'CoctailShakerSort'):
            self.master.change(CoctailShakerSort)


def main():
    root = Menu()
    root.mainloop()


if __name__ == '__main__':
    main()
