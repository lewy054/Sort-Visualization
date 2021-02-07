from timer import myTimer
import tkinter as tk
import threading
from sorting_helpers import draw, generate_numbers, swap_two_columns


class QuickSort(tk.Frame):

    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.main()

    def main(self):
        self.timer = myTimer(self.master)
        self.numbers_to_sort = generate_numbers()
        self.canvas, self.columns = draw(self.numbers_to_sort)
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.t = threading.Thread(target=self.quick_sort, args=(0, len(self.numbers_to_sort)-1))
        self.t.start()

    def partition(self, start, end):
        pivot = self.numbers_to_sort[start]
        low = start + 1
        high = end

        while True:
            while low <= high and self.numbers_to_sort[high] >= pivot:
                high = high - 1
            while low <= high and self.numbers_to_sort[low] <= pivot:
                low = low + 1
            if low <= high:
                self.canvas.itemconfig(self.columns[low], fill='red')
                self.canvas.itemconfig(self.columns[high], fill='red')
                self.numbers_to_sort[low], self.numbers_to_sort[high] = self.numbers_to_sort[high], self.numbers_to_sort[low]
                swap_two_columns(self.columns[low], self.columns[high], self.canvas)
                self.columns[low], self.columns[high] = self.columns[high], self.columns[low]
                self.canvas.itemconfig(self.columns[low], fill='orange')
                self.canvas.itemconfig(self.columns[high], fill='orange')
            else:
                break

        self.numbers_to_sort[start], self.numbers_to_sort[high] = self.numbers_to_sort[high], self.numbers_to_sort[start]
        swap_two_columns(self.columns[start], self.columns[high], self.canvas)
        self.columns[start], self.columns[high] = self.columns[high], self.columns[start]
        return high

    def quick_sort(self, start, end):
        if start >= end:
            if(end == len(self.numbers_to_sort) - 1):
                self.timer.stop()
            return

        p = self.partition(start, end)
        self.quick_sort(start, p-1)
        self.quick_sort(p+1, end)
