from tkinter import Tk, Label, Button, W
from tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = PanedWindow()
        master.title("Nonogram")


        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.new_button = Button(master, text="New puzzle", command=self.new_puzzle)
        self.new_button.pack()

        self.save_button = Button(master, text="Save puzzle", command=self.save_puzzle)
        self.save_button.pack()

        self.load_button = Button(master, text="Load puzzle", command=self.load_puzzle)
        self.load_button.pack()

        self.create_button = Button(master, text="Create puzzle", command=self.create_puzzle)
        self.create_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()



  

    def new_puzzle(self):
        print("Try to solve this")

    def save_puzzle(self):
        print("Saving your progress...")

    def load_puzzle(self):
        print("Loading game...")

    def create_puzzle(self):
        print("Take a picture!")


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()