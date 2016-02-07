#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import Tkinter as tk
import tkMessageBox as tkm
#Usar column configure
class HomeFrame(tk.Frame):
      
         def __init__(self,parent):
             #Create elements
             tk.Frame.__init__(self,parent, bd=5, height = 12, width = 12, relief="groove")
            
             self.__rows = []

             self.__i = 2
             

             #self.__add_column()
                       
             #self.__button1 = tk.Button(self, text="Add")
