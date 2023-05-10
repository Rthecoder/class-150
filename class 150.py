# -*- coding: utf-8 -*-
"""
Created on Fri May  5 14:37:35 2023

@author: hp
"""

from tkinter import *
root=Tk()
root.geometry("500x500")
country=Entry(root)
country.place(relx=0.5,rely=0.2,anchor=CENTER)

capital=Entry(root)
country.place(relx=0.5,rely=0.3,anchor=CENTER)

display_country_list=Label(root)
display_capital_list=Label(root)
display_random_country_list=Label(root)
display_random_capital_list=Label(root)

country_list=[]
capital_list=[]

def country_city_list():
    countryname=country.get()
    country_list.append(countryname)
    display_country_list["text"]="countryname :" + str(country_list)
    capitalname=capital.get()
    capital_list.append(capitalname)
    display_capital_list["text"]="capitalname :" + str(capital_list)