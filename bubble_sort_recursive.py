from timer import myTimer
from sorting_helpers import draw, generate_numbers, swap_two_columns
import tkinter as tk
import threading


class BubbleSortRecursive(tk.Frame):

    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.main()

    def main(self):
        self.timer = myTimer(self.master)
        self.numbers_to_sort = generate_numbers()
        self.length = len(self.numbers_to_sort)
        self.canvas, self.columns = draw(self.numbers_to_sort)
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.t = threading.Thread(target=self.bubble_sort_recursive)
        self.t.start()

    def bubble_sort_recursive(self, n=None):
        if n is None:
            n = self.length
        if n == 1:
            self.timer.stop()
            return
        for i in range(n - 1):
            if self.numbers_to_sort[i] > self.numbers_to_sort[i + 1]:
                self.numbers_to_sort[i], self.numbers_to_sort[i + 1] = self.numbers_to_sort[i + 1], self.numbers_to_sort[i]
                swap_two_columns(self.columns[i], self.columns[i + 1], self.canvas)
                self.columns[i], self.columns[i+1] = self.columns[i+1], self.columns[i]
        self.bubble_sort_recursive(n - 1)
