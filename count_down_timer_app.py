import time
import tkinter as tk
from tkinter import messagebox

class CountdownTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Countdown Timer")
        self.label = tk.Label(self.root, text="Enter time in seconds:", font=('Helvetica', 24))
        self.label.pack()
        self.entry = tk.Entry(self.root, font=('Helvetica', 24))
        self.entry.pack()
        self.button = tk.Button(self.root, text="Start", command=self.start_timer, font=('Helvetica', 24))
        self.button.pack()
        self.time_label = tk.Label(self.root, text="", font=('Helvetica', 48))
        self.time_label.pack()

    def start_timer(self):
        self.time = int(self.entry.get())
        self.button.config(state="disabled")
        self.countdown()

    def countdown(self):
        if self.time > 0:
            self.time_label.config(text=str(self.time))
            self.time -= 1
            self.root.after(1000, self.countdown)
        else:
            self.time_label.config(text="Time's up!")
            messagebox.showinfo("Timer", "Time's up!")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    timer = CountdownTimer()
    timer.run()
