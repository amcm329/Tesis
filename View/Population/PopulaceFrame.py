#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

"""
Elementos:
Generations
Population_size
Decimal_precision
Tipo de representacion
opciones de representacion para binario
"""
import Tkinter as tk
import ttk

class PopulaceFrame(tk.Frame):

      def __init__(self, parent, name, options):
          #Create elements
          tk.Frame.__init__(self,parent, bd=5, height = 12, width = 12, relief="groove")
          self.__title = name
          self.__class_name = name.lower()
          self.__path = options[0]
          self.__options = options[1]
          self.__options_list = self.__options.keys()
       
          self.__current_variable = tk.StringVar(self) 
          self.__current_variable.set(self.__options_list[0])
          self.__old_variable = self.__current_variable.get()     

          self.__title_label = tk.Label(self, text = self.__title)
          self.__number_of_generations_label = tk.Label(self, text="Number of generations:")
          self.__number_of_generations_entry = tk.Entry(self, width=18)
          self.__population_size_label = tk.Label(self, text="Population size:")
          self.__population_size_entry = tk.Entry(self, width=18)
          self.__decimal_precision_label = tk.Label(self, text="Decimal precision:")
          self.__decimal_precision_entry = tk.Entry(self, width=18)

          
          self.__option_menu_label = tk.Label(self, text = "Chromosomal Representation: ")
          self.__option_menu = tk.OptionMenu(self, self.__current_variable, *self.__options_list, command = self.__update_widgets)
          self.__separator = ttk.Separator(self,orient = tk.HORIZONTAL)
          self.__parameters_label = tk.Label(self, text = "Additional options for {0}:".format(self.__current_variable.get()))
                    
          self.row_position = 0

          self.__widgets = {}

          for technique_name in self.__options_list: 
              technique_parameters = self.__options[technique_name]['parameter']
              provisional_widgets = []
              for element in technique_parameters:
                  provisional_label = tk.Label(self,text = element['name'] + ":")
                  #print "Hola: ", provisional_label.winfo_class()
                  provisional_entry = tk.Entry(self,relief="ridge") 
                  provisional_widgets.append([provisional_label,provisional_entry])
                   
              if provisional_widgets == []:
                 provisional_label = tk.Label(self,text = "NONE")
                 provisional_widgets.append([provisional_label])
                 

              self.__widgets[technique_name] = provisional_widgets

          self.__grid_general_widgets()
   
      def __update_widgets(self,dummy_variable):   
          #Eliminar las viejas          
          for old_widget in self.__widgets[self.__old_variable]:
              for element in old_widget:
                  element.grid_forget()
             
          #Poner las nuevas
          counter = self.row_position
          for current_widget in self.__widgets[self.__current_variable.get()]:
              for position in range (len(current_widget)): 
                  current_widget[position].grid(row = counter, column = position, padx = 5, pady = 5,)
              counter += 1   
            
          self.__old_variable = self.__current_variable.get()
          self.__parameters_label.config(text = "Additional parameters for {0}:".format(self.__current_variable.get()))
      

      def __grid_general_widgets(self):      
          self.__title_label.grid(row = self.row_position, column = 0, padx = 5, pady = 5)
          self.row_position += 1
          
          self.__number_of_generations_label.grid(row = self.row_position, column = 0, padx = 5, pady = 5)
          self.__number_of_generations_entry.grid(row = self.row_position, column = 1, padx = 5, pady = 5)
          self.row_position += 1
          
          self.__population_size_label.grid(row = self.row_position, column = 0, padx = 5, pady = 5)
          self.__population_size_entry.grid(row = self.row_position, column = 1, padx = 5, pady = 5)
          self.row_position += 1
          
          self.__decimal_precision_label.grid(row = self.row_position, column = 0, padx = 5, pady = 5)
          self.__decimal_precision_entry.grid(row = self.row_position, column = 1, padx = 5, pady = 5)
          self.row_position += 1
          
          self.__option_menu_label.grid(row = self.row_position, column = 0, padx = 5, pady = 5)
          self.__option_menu.grid(row = self.row_position, column = 1, padx = 5, pady = 5)
          self.row_position += 1

          self.__parameters_label.grid(row = self.row_position, column = 1, padx = 5, pady = 5)
          #self.__separator.grid(row =2,column = 0,columnspan = 12, padx = 5, pady = 5, sticky="ew")
          self.row_position += 1
          self.__update_widgets(None)        
         
          
          #Falta el checkbutton para la opcion de la codificacion de gray
  

      def get_information(self):
          populace_information = {
                                  'number_of_generations': self.__number_of_generations_entry.get(),
                                  'population_size': self.__population_size_entry.get(),
                                  'decimal_precision_query': self.__decimal_precision_entry.get()  
                                 }

          selected_technique = self.__current_variable.get()
          selected_class = self.__path + self.__options[selected_technique]["class"]
          selected_options = {}
          technique_parameters = self.__options[selected_technique]["parameter"]
          technique_widgets = self.__widgets[selected_technique]             
          
          for x in range (len(technique_parameters)):
              current_parameter = technique_parameters[x]["value"]
              current_value =  technique_widgets[x][1].get()
              selected_options[current_parameter] = current_value
        
          populace_information[self.__class_name + "_class"] = selected_class
          populace_information[self.__class_name + "_options"] = selected_options

          return populace_information          


