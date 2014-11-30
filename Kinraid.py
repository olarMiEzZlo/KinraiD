"""KinraiD
Author : Tanawat Kusungnoen
         Phakphum Charuspan
Last update : 19/11/2557
"""
print 'Test'
from Tkinter import *
class App(object):
    """first class an interface"""
    def __init__(self):
        """main method"""
        self.root = Tk()
        self.root.geometry("500x300+600+300")
        self.root.title("Insert your money")

        """Background Image"""
        photo = PhotoImage(file = "bg1.gif")
        label = Label(self.root, image = photo)
        label.image = photo
        label.place(relx=0, rely=0)

        """Input money box"""
        self.entrymoney = StringVar()
        Entry(self.root, textvariable = self.entrymoney
              ).place(x=110, y=75)

        self.root.mainloop()

App()
