"""KinraiD
Author : Tanawat Kusungnoen
         Phakphum Charuspan
Last update : 19/11/2557
"""
from Tkinter import *
class Interface(object):
    """ first class an interface """
    def __init__(self):
        """ main method """
        self.root = Tk()
        self.root.geometry("505x305+450+200")
        self.root.title("KinraiD")

        #---Background Image---#
        photo = PhotoImage(file = "bg1.gif")
        b_inter = Button(self.root, command = self.call_mainpage, image = photo)
        b_inter.place(x=0, y=0)

        self.root.mainloop()

    def call_mainpage(self):
        """ call Main class to create mainpage """
        self.root.destroy()
        Main()

class Main(object):
    """ first class an interface """
    def __init__(self):
        """ main method """
        self.root = Tk()
        self.root.geometry("605x505+400+100")
        self.root.title("KinraiD")

        #---Background Image---#
        photo2 = PhotoImage(file = "testbg2.gif")
        b_main = Label(self.root, image = photo2)
        b_main.place(x=0, y=0)

        #---Button Menu---#
        bt1 = PhotoImage(file = "testbut.gif")
        bt2 = PhotoImage(file = "add_but.gif")
        bt3 = PhotoImage(file = "help_but.gif")
        bt4 = PhotoImage(file = "about_but.gif")
        b1_main = Button(self.root, bg = 'white', image = bt1,
                         command = self.call_eating)
        b2_main = Button(self.root, bg = 'white', image = bt2,
                         command = self.call_addmenu)
        b3_main = Button(self.root, bg = 'white', image = bt3,
                         command = self.call_helpus)
        b4_main = Button(self.root, bg = 'white', image = bt4,
                         command = self.call_about)
        b1_main.place(x=60, y=145)
        b2_main.place(x=60, y=215)
        b3_main.place(x=60, y=285)
        b4_main.place(x=60, y=355)

        self.root.mainloop()

    def call_eating(self):
        """ call Main class to create mainpage """
        Eating()

    def call_addmenu(self):
        """ call Main class to create mainpage """
        Addmenu()

    def call_helpus(self):
        """ call Main class to create mainpage """
        Helpus()

    def call_about(self):
        """ call Main class to create mainpage """
        About()

class Eating(object):
    """ class to input user's money and say what do you eat """
    def __init__(self):
        """ main method """
        self.root = Tk()
        self.root.geometry("605x505+400+100")
        self.root.title("KinraiD")


class Addmenu(object):
    """ class to input user's money and say what do you eat """
    def __init__(self):
        """ main method """
        self.root = Tk()
        self.root.geometry("605x505+400+100")
        self.root.title("KinraiD")    

class Helpus(object):
    """ class to input user's money and say what do you eat """
    def __init__(self):
        """ main method """
        self.root = Tk()
        self.root.geometry("605x505+400+100")
        self.root.title("KinraiD")

class About(object):
    """ class to input user's money and say what do you eat """
    def __init__(self):
        """ main method """
        self.root = Tk()
        self.root.geometry("605x505+400+100")
        self.root.title("KinraiD")
        
Interface()
