def bubbleSort(self):
    n = len(self.numbersToSort)
    for i in range(n):
        for j in range(0, n-i-1):
            self.canvas.itemconfig(self.columns[j], fill='red')
            self.canvas.itemconfig(self.columns[j+1], fill='red')
            if (self.numbersToSort[j] > self.numbersToSort[j+1]):
                self.swap_two_pos(self.columns[j], self.columns[j+1])
                self.columns[j], self.columns[j+1] = self.columns[j+1], self.columns[j]
                self.numbersToSort[j], self.numbersToSort[j+1] = self.numbersToSort[j+1], self.numbersToSort[j]
            if(self.columns[j] != self.columns[i]):
                self.canvas.itemconfig(self.columns[j], fill='orange')
        self.canvas.itemconfig(self.columns[n-i-1], fill='green')
