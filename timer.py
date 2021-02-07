import tkinter as tk
from timeit import Timer, default_timer as timer
from datetime import timedelta


class myTimer(tk.Frame):
    def __init__(self, master):
        self.create_timer()
        self.set_timer(master)

    def create_timer(self):
        self.timer = tk.Label(text="")
        self.timer.pack()
        self.start = timer()
        self.timer_runnig = True

    def set_timer(self, master):
        end = timer()
        self.timer.config(text=timedelta(seconds=end-self.start))
        if(self.timer_runnig):
            master.after(1, lambda: self.set_timer(master))

    def stop(self):
        self.timer_runnig = False
