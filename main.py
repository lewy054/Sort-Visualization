from tkinter import *
from time import sleep
from secrets import randbelow
import threading
from sorts import *

class SortingVisualization:
    def __init__(self, root):
        self.root = root

    def main(self):
        self.generateNumbers()
        self.t = threading.Thread(target=self.draw)
        self.t.start()

    def generateNumbers(self):
        self.numbersToSort = []
        for _ in range(150):
            self.numbersToSort.append(randbelow(500))

    def draw(self):
        xoff = 0
        self.canvas = Canvas()
        self.columns = []
        for i in self.numbersToSort:
            column = self.canvas.create_rectangle(xoff, 720, xoff+10, 600-i,
                outline="black", fill="orange")
            self.columns.append(column)
            xoff+=10
        self.canvas.pack(fill=BOTH, expand=1)
        bubbleSort(self)
    
    def swap_two_pos(self, pos_0, pos_1):
        x_00, _, x_01, _ = self.canvas.coords(pos_0)
        x_10, _, x_11, _ = self.canvas.coords(pos_1)
        # moves each rectangle to the x position of the other; y remains unchanged
        self.canvas.move(pos_0, x_10-x_00, 0)
        self.canvas.move(pos_1, x_01-x_11, 0)

if __name__ == '__main__':
    root = Tk()
    root.geometry('1500x720')
    root.bind("<F11>", lambda event: root.attributes("-fullscreen",
                                    not root.attributes("-fullscreen")))
    root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False), root.geometry('1500x720'))
    root.title('Sorting visualization')
    sort = SortingVisualization(root)
    sort.main()
    root.mainloop()