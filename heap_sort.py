from timer import myTimer
from sorting_helpers import draw, generate_numbers, swap_two_columns
import tkinter as tk
import threading


class HeapSort(tk.Frame):

    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.main()

    def main(self):
        self.timer = myTimer(self.master)
        self.numbers_to_sort = generate_numbers()
        self.canvas, self.columns = draw(self.numbers_to_sort)
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.t = threading.Thread(target=self.heap_sort)
        self.t.start()

    def heap_sort(self):
        n = len(self.numbers_to_sort)
        for i in range(n//2 - 1, -1, -1):
            self.heapify(n, i)

        for i in range(n-1, 0, -1):
            self.numbers_to_sort[i], self.numbers_to_sort[0] = self.numbers_to_sort[0], self.numbers_to_sort[i]
            swap_two_columns(self.columns[i], self.columns[0], self.canvas)
            self.columns[i], self.columns[0] = self.columns[0], self.columns[i]
            self.heapify(i, 0)
        self.timer.stop()

    def heapify(self, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and self.numbers_to_sort[largest] < self.numbers_to_sort[l]:
            largest = l
        if r < n and self.numbers_to_sort[largest] < self.numbers_to_sort[r]:
            largest = r
        if largest != i:
            self.numbers_to_sort[i], self.numbers_to_sort[largest] = self.numbers_to_sort[largest], self.numbers_to_sort[i]
            swap_two_columns(self.columns[i], self.columns[largest], self.canvas)
            self.columns[i], self.columns[largest] = self.columns[largest], self.columns[i]
            self.heapify(n, largest)
