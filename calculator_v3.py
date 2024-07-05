## goal: develop a working GUI calculator app.

import tkinter as tk

class Calculator:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def add(self):
        print(self.x + self.y)
        return self.x + self.y

MyCalculator = Calculator(1,2)
#print("the sum is: ", MyCalculator.add())

root = tk.Tk()
frm = tk.Frame(root)
frm.grid()
tk.Label(frm, text="Hello World!").grid(column=0, row=0)
text_input = tk.Entry(root).grid(column=0, row=1)
print("text_input: ", text_input)
tk.Button(frm, text="Add", command=MyCalculator.add).grid(column=1, row=0)
root.mainloop()
