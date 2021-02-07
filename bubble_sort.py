from timer import myTimer
from sorting_helpers import draw, generate_numbers, swap_two_columns
import tkinter as tk
import threading


class BubbleSort(tk.Frame):

    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.main()

    def main(self):
        self.timer = myTimer(self.master)
        self.numbers_to_sort = generate_numbers()
        self.canvas, self.columns = draw(self.numbers_to_sort)
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.t = threading.Thread(target=self.bubble_sort)
        self.t.start()

    def bubble_sort(self):
        n = len(self.numbers_to_sort)
        for i in range(n):
            for j in range(0, n-i-1):
                self.canvas.itemconfig(self.columns[j], fill='red')
                self.canvas.itemconfig(self.columns[j+1], fill='red')
                if (self.numbers_to_sort[j] > self.numbers_to_sort[j+1]):
                    swap_two_columns(self.columns[j], self.columns[j+1], self.canvas)
                    self.columns[j], self.columns[j+1] = self.columns[j+1], self.columns[j]
                    self.numbers_to_sort[j], self.numbers_to_sort[j+1] = self.numbers_to_sort[j+1], self.numbers_to_sort[j]
                if(self.columns[j] != self.columns[i]):
                    self.canvas.itemconfig(self.columns[j], fill='orange')
            self.canvas.itemconfig(self.columns[n-i-1], fill='green')
        self.timer.stop()
