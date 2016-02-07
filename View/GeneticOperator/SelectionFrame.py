#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import ttk
import Tkinter as tk
from Template.TemplateFrame import * 

class SelectionFrame(TemplateFrame):

      def __init__(self, parent, name, options):
          TemplateFrame.__init__(self,parent,name,options)
          self.title_label.grid(row = self.row_position,column = 1,columnspan = 3, padx = 5, pady = 5)
          self.row_position += 1

          self.grid_general_widgets()


      def get_information(self):
          return TemplateFrame.get_information(self)
