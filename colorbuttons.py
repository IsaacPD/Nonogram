import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        master.title("Test") #Controls the window title.
        self.pack()
        self.createWidgets()


    def createWidgets(self):
        floors = [i for i in range(41)]
        self.buttons = {}

        xPos = 0
        yPos = 0
        for floor in floors:
            if(yPos == 5):
                xPos = xPos + 1
                yPos = 0
            if(xPos == 8):
                yPos = 2

            self.buttons[floor] = tk.Button(self, width=3, text=floor, command = lambda f=floor: self.pressed(f))
            self.buttons[floor].grid(row=xPos, column =yPos)
            yPos = yPos +1

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                    command=root.destroy).grid(row = xPos, column = yPos)

    def pressed(self, index):
        print("number pressed", index)
        self.buttons[index].configure(bg="red")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
