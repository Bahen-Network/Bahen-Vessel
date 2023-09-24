import tkinter as tk
from .frames import MainFrame


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Worker App")
        self.root.geometry("600x600")
        self.main_frame = MainFrame(self.root)

    def run(self):
        self.root.mainloop()
