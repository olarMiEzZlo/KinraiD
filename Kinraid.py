#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""KinraiD
Author : Tanawat Kusungnoen
         Phakphum Charuspan
Language : Python 2.7.8
Last update : 9/12/2557
"""
from Tkinter import *
from db import db
con = db()
cur = con.cursor()
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
        self.root.geometry("305x505+600+100")
        self.root.title("KinraiD")

        #---Background Image---#
        bg_add = PhotoImage(file = "testbg_add.gif")
        b_add = Label(self.root, image = bg_add)
        b_add.place(x=0, y=0)

        #---Button---#
        back_button = PhotoImage(file = "back_but.gif")
        backbut = Button(self.root, bg = "white", image = back_button,
                         command = self.back)
        backbut.place(x=180, y=420)
        addmenu_but = PhotoImage(file = "addmenubut.gif")
        addmenubutton = Button(self.root, bg = "white", image = addmenu_but,
                               command = self.confirm).place(x=115, y=300)

        #---Input Box---#
        self.addfood = StringVar()
        Entry(self.root, textvariable = self.addfood, bg = "white"
              ).place(x=95, y=75)
        self.addprice = IntVar()
        Entry(self.root, textvariable = self.addprice, bg = "white"
              ).place(x=95, y=150)
        self.addname = StringVar()
        Entry(self.root, width=24, textvariable = self.addname, bg = "white"
              ).place(x=95, y=225)

        #---Option Menu---#
        cur.execute("SELECT * FROM shop")
        name_list = cur.fetchall()
        
        self.alist = []
        self.dic = {}
        
        for shop in name_list:
            self.alist.append(shop[1])
            self.dic[shop[1]] = shop[0]
            
        self.variable_name = StringVar()
        self.option_name = OptionMenu(self.root, self.variable_name, *self.alist).place(x=95, y=250)
        self.variable_name.set(self.alist[0])

        #---Label Text---#
        food_text = Label(self.root, text = "Menu", bg = "#ffd87e"
                          ).place(x=140, y=50)
        price_text = Label(self.root, text = "Price", bg = "#ffd87e"
                           ).place(x=140, y=125)
        name_text = Label(self.root, text = "Restaurant Name", bg = "#ffd87e"
                          ).place(x=108, y=200)
        
        self.root.mainloop()

    def back(self):
        """ back to main page """
        self.root.destroy()
        Main()

    def confirm(self):
        pp = self.addprice.get()
        food = self.addfood.get()
        rest = self.addname.get()
        if rest == "":
            shopid = self.dic.get(self.variable_name.get())

            cur.execute("INSERT INTO menu(name, price, shop_id) VALUES ('{}', {}, {})".format(food, pp, shopid))
            con.commit()
        else:
            cur.execute("INSERT INTO shop(name) VALUES ('{}')".format(rest))
            con.commit()
            cur.execute("SELECT id FROM shop WHERE name = '{}'".format(rest))
            shopid = cur.fetchone()[0]
            cur.execute("INSERT INTO menu(name, price, shop_id) VALUES ('{}', {}, '{}')".format(food, pp, shopid))
            con.commit()
        self.back()

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
