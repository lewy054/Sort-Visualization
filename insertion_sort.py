import time
from timer import myTimer
from sorting_helpers import draw, draw_column, generate_numbers, replace_column, swap_two_columns
import tkinter as tk
import threading


class InsertionSort(tk.Frame):

    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.main()

    def main(self):
        self.timer = myTimer(self.master)
        self.numbers_to_sort = generate_numbers()
        self.canvas, self.columns = draw(self.numbers_to_sort)
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.t = threading.Thread(target=self.insertion_sort)
        self.t.start()

    def insertion_sort(self):
        time.sleep(2)
        # Loop from the second element of the array until
        # the last element
        for i in range(1, len(self.numbers_to_sort)):
            # This is the element we want to position in its
            # correct place
            key_item = self.numbers_to_sort[i]
            key_column = self.columns[i]
            print(i)
            # Initialize the variable that will be used to
            # find the correct position of the element referenced
            # by `key_item`
            j = i - 1

            # Run through the list of items (the left
            # portion of the array) and find the correct position
            # of the element referenced by `key_item`. Do this only
            # if `key_item` is smaller than its adjacent values.
            while j >= 0 and self.numbers_to_sort[j] > key_item:
                # Shift the value one position to the left
                # and reposition j to point to the next element
                # (from right to left)
                self.numbers_to_sort[j + 1] = self.numbers_to_sort[j]
                replace_column(self.columns[j], self.columns[j+ 1], self.canvas, self.columns)
                self.columns[j+ 1] = self.columns[j]
                j -= 1
            print(j)
            print(self.columns)
            # When you finish shifting the elements, you can position
            # `key_item` in its correct location
            # swap_two_columns(self.columns[j +1], self.columns[i], self.canvas)
            print(self.canvas.coords(self.columns[j + 1]))
            print(self.canvas.coords(key_column))
            replace_column(self.columns[j + 1], key_column, self.canvas, self.columns)
            self.columns[j + 1] = key_column
            self.numbers_to_sort[j + 1] = key_item
        self.timer.stop()
