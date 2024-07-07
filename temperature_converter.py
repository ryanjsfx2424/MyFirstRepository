import tkinter as tk
"""
# going over inheritance
class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

class ConstructionWorker(Person):
    def __init__(self, name, birthday, income):
        super().__init__(name, birthday)
        self.income = income
"""
class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        #print(r"$^1$C to $^o$F")

        buttonCtoF = tk.Button(master, text="C to F", command=self.convertCtoF)
        buttonCtoF.pack()    

        buttonFtoC = tk.Button(master, text="F to C", command=self.convertFtoC)
        buttonFtoC.pack()    

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()

        # Set it to some value.
        self.contents.set("Enter a Number to Convert (default F to C)")

        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        #self.entrythingy.bind('<Key-Return>',
        #                     self.convertFtoC)

    def convertCtoF(self):
        C = self.contents.get()

        if not C.isdigit():
            print("Error, not a number!")
            return
        C = float(C)

        F = (9.0/5.0)*C + 32
        print("F: ", F)

    def convertFtoC(self):
        F = self.contents.get()

        if not F.isdigit():
            print("Error, not a number!")
            return
        F = float(F)
        
        C = (5.0/9.0)*(F-32)
        print("C: ", C)

if __name__ == "__main__":
    root = tk.Tk()
    myapp = App(root)
    myapp.mainloop()