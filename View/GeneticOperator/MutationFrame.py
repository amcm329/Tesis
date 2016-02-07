#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import ttk
import Tkinter as tk
from Template.TemplateFrame import * 

class MutationFrame(TemplateFrame):

      def __init__(self, parent, name, options):
          TemplateFrame.__init__(self,parent,name,options)
          self.__probability_label = tk.Label(self, text = "Probability: ")
          self.__probability_entry = tk.Entry(self,relief="ridge")            
          self.title_label.grid(row = self.row_position,column = 1,columnspan = 3, padx = 5, pady = 5)
          self.row_position += 1
          self.__probability_label.grid(row = self.row_position,column = 0, padx = 5, pady = 5)
          self.__probability_entry.grid(row = self.row_position,column = 1, padx = 5, pady = 5)           
          self.row_position += 1

          self.grid_general_widgets()
          
          
      def get_information(self):
          mutation_information = TemplateFrame.get_information(self)
          mutation_information["probability_{0}_general".format(self.class_name)] = self.__probability_entry.get()
          return mutation_information
