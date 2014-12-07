"""KinraiD
Author : Tanawat Kusungnoen
         Phakphum Charuspan
Last update : 19/11/2557
"""
print 'Test'
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
        self.root.destroy()
        Eating()

    def call_addmenu(self):
        """ call Main class to create mainpage """
        self.root.destroy()
        Addmenu()

    def call_helpus(self):
        """ call Main class to create mainpage """
        self.root.destroy()
        Helpus()

    def call_about(self):
        """ call Main class to create mainpage """
        self.root.destroy()
        About()

class Eating(object):
    """ class to input user's money and say what do you eat """
    def __init__(self):
        """ main method """
        self.root = Tk()
        self.root.geometry("405x505+400+100")
        self.root.title("KinraiD")

        #---Background Image---#
        bg_eat = PhotoImage(file = "testbg_main.gif")
        b_eat = Label(self.root, image = bg_eat)
        b_eat.place(x=0, y=0)

        #---Button---#
        back_button = PhotoImage(file = "back_but.gif")
        go_button = PhotoImage(file = "go_but.gif")
        backbut = Button(self.root, bg = "white", image = back_button,
                         command = self.back)
        gobut = Button(self.root, bg = "white", image = go_button)
        backbut.place(x=280, y=420)
        gobut.place(x=280, y=170)

        #---Input box---#
        self.entrymoney = IntVar()
        Entry(self.root, textvariable = self.entrymoney, bg = "pink"
              ).place(x=170, y=50)
        self.name = StringVar()
        Entry(self.root, textvariable = self.name, bg = "pink"
              ).place(x=170, y=80)

        #---Label text---#
        money_text = Label(self.root, text = "Money :", bg = "white"
                           ).place(x=120, y=50)
        name_text = Label(self.root, text = "Restaurant Name :", bg = "white"
                          ).place(x=66, y=80)
        baht_text = Label(self.root, text = "Baht", bg = "white"
                          ).place(x=300, y=50)
        

        self.root.mainloop()

    def back(self):
        """ back to main page """
        self.root.destroy()
        Main()
        
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
