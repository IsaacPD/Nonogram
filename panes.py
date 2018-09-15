from tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E, PanedWindow, BOTH, VERTICAL

class MyFirstGUI:
    def __init__(self, master):
        self.master = PanedWindow()
        master.title("Nonogram")
        m1 = PanedWindow()
        m1.pack(fill=BOTH, expand=1)

        left = Label(m1, text="left pane")


        m1.add(left)

        m2 = PanedWindow(m1, orient=VERTICAL)
        m1.add(m2)

        self.new_button = Button(m2, text="New puzzle", command=self.new_puzzle)
        self.new_button.pack()
        self.save_button = Button(m2, text="Save puzzle", command=self.save_puzzle)
        self.save_button.pack()

        

        bottom = Label(m2, text="bottom pane")
        m2.add(bottom)

    def new_puzzle(self):
        print("Try to solve this")

    def save_puzzle(self):
        print("Saving your progress...")
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
