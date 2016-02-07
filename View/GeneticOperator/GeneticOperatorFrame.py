#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import Tkinter as tk
import tkMessageBox as tkm

from SelectionFrame import *
from CrossoverFrame import *
from MutationFrame import *

#Usar column configure
#Separar elementos por una línea para darle más presentación
#Ver si el porcentaje se queda como entero o decimal

class GeneticOperatorFrame(tk.Frame):
      
      def __init__(self, parent, options = None):
          tk.Frame.__init__(self,parent, bd=5, relief="groove")
          self.__general_options = options     
          self.__frames_instances = [("Selection",SelectionFrame),("Crossover",CrossoverFrame),("Mutation",MutationFrame)]
          self.__frames = []
          for frame in self.__frames_instances:
              initial_frame = frame[1](self,frame[0],self.__general_options[frame[0]])
              initial_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True)
              self.__frames.append(initial_frame)

     
      def delete_content(self):
          pass
     

      def get_information(self):
          #concatenar diccionarios
          genetic_operator_information = {}
          for current_frame in self.__frames:
              genetic_operator_information.update(current_frame.get_information())
       
          return genetic_operator_information
