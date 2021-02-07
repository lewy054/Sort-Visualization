from timer import myTimer
from sorting_helpers import draw, generate_numbers, swap_two_columns
import tkinter as tk
import threading


class SelectionSort(tk.Frame):

    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.main()

    def main(self):
        self.timer = myTimer(self.master)
        self.numbers_to_sort = generate_numbers()
        self.canvas, self.columns = draw(self.numbers_to_sort)
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.t = threading.Thread(target=self.selection_sort)
        self.t.start()

    def selection_sort(self):
        for i in range(len(self.numbers_to_sort)):
            lowest_value_index = i
            for j in range(i + 1, len(self.numbers_to_sort)):
                if self.numbers_to_sort[j] < self.numbers_to_sort[lowest_value_index]:
                    lowest_value_index = j
            self.numbers_to_sort[i], self.numbers_to_sort[lowest_value_index] = self.numbers_to_sort[lowest_value_index], self.numbers_to_sort[i]
            swap_two_columns(self.columns[i], self.columns[lowest_value_index], self.canvas)
            self.columns[i], self.columns[lowest_value_index] = self.columns[lowest_value_index], self.columns[i]
        self.timer.stop()
