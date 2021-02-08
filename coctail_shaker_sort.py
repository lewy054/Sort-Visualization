from timer import myTimer
from sorting_helpers import change_two_columns_color_orange, change_two_columns_color_red, draw, generate_numbers, swap_two_columns
import tkinter as tk
import threading


class CoctailShakerSort(tk.Frame):

    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.main()

    def main(self):
        self.timer = myTimer(self.master)
        self.numbers_to_sort = generate_numbers()
        self.canvas, self.columns = draw(self.numbers_to_sort)
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.t = threading.Thread(target=self.cocktail_shaker_sort)
        self.t.start()

    def cocktail_shaker_sort(self):
        def swap(i, j):
            self.numbers_to_sort[i],  self.numbers_to_sort[j] = self.numbers_to_sort[j],  self.numbers_to_sort[i]
            swap_two_columns(self.columns[i], self.columns[j], self.canvas)
            self.columns[i], self.columns[j] = self.columns[j], self.columns[i]

        upper = len(self.numbers_to_sort) - 1
        lower = 0

        no_swap = False
        while (not no_swap and upper - lower > 1):
            no_swap = True
            for j in range(lower, upper):
                change_two_columns_color_red(j+1, j, self.canvas, self.columns)
                change_two_columns_color_orange(j+1, j, self.canvas, self.columns)
                if self.numbers_to_sort[j + 1] < self.numbers_to_sort[j]:
                    swap(j + 1, j)
                    no_swap = False
            upper = upper - 1

            for j in range(upper, lower, -1):
                change_two_columns_color_red(j-1, j, self.canvas, self.columns)
                change_two_columns_color_orange(j-1, j, self.canvas, self.columns)
                if self.numbers_to_sort[j - 1] > self.numbers_to_sort[j]:
                    swap(j - 1, j)
                    no_swap = False
            lower = lower + 1
        self.timer.stop()
