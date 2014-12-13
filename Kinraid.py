#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""KinraiD
Author : Tanawat Kusungnoen
         Phakphum Charatphan
Language : Python 2.7.8
         : SQL
Last update : 13/12/2557
"""
from Tkinter import *
from db import db
import random
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
        gobut = Button(self.root, bg = "white", image = go_button,
                       command = self.randomnow)
        backbut.place(x=280, y=420)
        gobut.place(x=280, y=170)

        #---Input box---#
        self.entrymoney = IntVar()
        Entry(self.root, textvariable = self.entrymoney, bg = "pink"
              ).place(x=170, y=50)
        self.result_m = StringVar()
        Entry(self.root, textvariable = self.result_m, bg = "white"
              ).place(x=260, y=280)
        self.result_p = StringVar()
        Entry(self.root, textvariable = self.result_p, bg = "white"
              ).place(x=260, y=320)
        self.result_n = StringVar()
        Entry(self.root, textvariable = self.result_n, bg = "white"
              ).place(x=260, y=360)

        #---Option Menu---#
        cur.execute("SELECT * FROM shop")
        name_list = cur.fetchall()
        
        self.alist = ['Random']
        self.dic = {}
        
        for shop in name_list:
            self.alist.append(shop[1])
            self.dic[shop[1]] = shop[0]
            
        self.variable_name = StringVar()
        self.option_name = OptionMenu(self.root, self.variable_name, *self.alist).place(x=170, y=75)
        self.variable_name.set(self.alist[0])

        #---Label text---#
        money_text = Label(self.root, text = "Money :", bg = "white"
                           ).place(x=120, y=50)
        name_text = Label(self.root, text = "Restaurant Name :", bg = "white"
                          ).place(x=66, y=80)
        baht_text = Label(self.root, text = "Baht", bg = "white"
                          ).place(x=300, y=50)
        resultt = Label(self.root, text = "Result", bg = "#fdd1d5",
                        font = ("Courier", 14, "bold")).place(x=315, y=235)
        resultm = Label(self.root, text = "Menu", bg = "#fdd1d5"
                        ).place(x=260, y=257)
        resultp = Label(self.root, text = "Price", bg = "#fdd1d5"
                        ).place(x=260, y=299)
        resultn = Label(self.root, text = "Restuarant name", bg = "#fdd1d5"
                        ).place(x=260, y=339)

        self.root.mainloop()

    def back(self):
        """ back to main page """
        self.root.destroy()
        Main()

    def randomnow(self):
        """ random result """
        word = self.variable_name.get()
        moneyuser = self.entrymoney.get()
        if word == 'Random':
            shopid = random.choice(self.dic.values())
        else:
            shopid = self.dic.get(word)
        cur.execute("SELECT id FROM menu WHERE price <= '{}' AND shop_id = '{}'".format(moneyuser, shopid))
        id_all = cur.fetchall()
        id_list = []
        for m_id in id_all:
            id_list.append(m_id[0])
        rand_id = random.choice(id_list)
        cur.execute("SELECT name,price FROM menu WHERE id = {}".format(rand_id))
        res = cur.fetchall()
        for resn in self.dic:
            if self.dic[resn] == shopid:
                self.result_n.set(resn)
        self.result_m.set(res[0][0])
        self.result_p.set(res[0][1])
        
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
        Entry(self.root, textvariable = self.addname, bg = "white"
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
        select_add = Label(self.root, text = "Add new", bg = "#ffd87e"
                           ).place(x=35, y=225)
        select = Label(self.root, text = "or Select", bg = "#ffd87e"
                       ).place(x=35, y=255)
        
        self.root.mainloop()

    def back(self):
        """ back to main page """
        self.root.destroy()
        Main()

    def confirm(self):
        """ method to confirm add menu to Database """
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
        self.root.geometry("1305x505+30+100")
        self.root.title("KinraiD")

        #---Back button---#
        backbar = Menu(self.root)
        backbar.add_cascade(label="Back", command = self.back)
        self.root.config(menu=backbar)

        #---Background Image---#
        bg_help = PhotoImage(file = "help_pic.gif")
        bg_h = Label(self.root, image = bg_help)
        bg_h.place(x=0, y=0)

        self.root.mainloop()

    def back(self):
        """ back to main page """
        self.root.destroy()
        Main()

class About(object):
    """ class to input user's money and say what do you eat """
    def __init__(self):
        """ main method """
        self.root = Tk()
        self.root.geometry("405x305+400+100")
        self.root.title("KinraiD")

        #---Background Image---#
        bg_about = PhotoImage(file = "about_bg.gif")
        b_about = Label(self.root, image = bg_about)
        b_about.place(x=0, y=0)

        #---Label Text---#
        ver_text = Label(self.root, text = "Version", font = (
            "Courier", 14), bg = "#abff9b").place(x=165, y=25)
        vers = Label(self.root, text = "KinraiD V.1.0.1", font =(
            "Courier", 11), bg = "#abff9b").place(x=134, y=50)
        aut_text = Label(self.root, text = "Author", font = (
            "Courier", 14), bg = "#abff9b").place(x=172, y=90)
        aut1 = Label(self.root, text = "Mr.Tanawat Kusungnoen  57070025",
                     font = ("Courier", 11), bg = "#abff9b").place(x=70, y=115)
        aut2 = Label(self.root, text = "Mr.Phakphum Charatphan  57070088",
                     font = ("Courier", 11), bg = "#abff9b").place(x=66, y=137)
        cre_text = Label(self.root, text = "Credit Database", font = (
            "Courier", 14), bg = "#abff9b").place(x=128, y=175)
        credit = Label(self.root, text = "Mr.Nonpawit Teerachetmongkol",
                       font = ("Courier", 11), bg="#abff9b").place(x=85, y=200)

        #---Button---#
        back_button = PhotoImage(file = "back_but.gif")
        backbut = Button(self.root, bg = "white", image = back_button,
                         command = self.back)
        backbut.place(x=300, y=240)

        self.root.mainloop()

    def back(self):
        """ back to main page """
        self.root.destroy()
        Main()
        
Interface()
