from menu import Menu
import tkinter as tk


class Mainframe(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Sorting visualization')
        self.geometry('1500x720')
        self.frame = Menu(self)
        self.frame.pack()

    def change(self, frame):
        self.frame.pack_forget()
        self.frame = frame(self)
        self.frame.pack()


def main():
    root = Mainframe()
    root.mainloop()


if __name__ == '__main__':
    main()
