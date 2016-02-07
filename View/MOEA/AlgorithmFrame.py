

import Tkinter as tk
import ttk


class AlgorithmFrame(tk.Frame):

      def __init__(self, parent, name, options):
          tk.Frame.__init__(self,parent, bd=5, relief="groove")
          self.__title = name
          self.__class_name = name.lower()
          self.__path = options[0]
          self.__options = options[1]
          self.__options_list = self.__options.keys()
       
          self.__current_variable = tk.StringVar(self) 
          self.__current_variable.set(self.__options_list[0])
          self.__old_variable = self.__current_variable.get()     
          self.__row_position = 0
         
          self.__title_label = tk.Label(self, text = self.__title)
          self.__option_radiobutton_label = tk.Label(self, text = "Technique: ")
          self.__separator = ttk.Separator(self,orient = tk.HORIZONTAL)
          self.__parameters_label = tk.Label(self, text = "Additional options for {0}:".format(self.__current_variable.get()))

          self.__widgets = {}
          
          for technique_name in self.__options_list: 
              technique_parameters = self.__options[technique_name]['parameter']
              provisional_widgets = []                 
              for element in technique_parameters:
                  provisional_label = tk.Label(self,text = element['name'] + ":")
                  provisional_entry = tk.Entry(self,relief="ridge")                                                             
                  provisional_widgets.append([provisional_label,provisional_entry])
     
              if provisional_widgets == []:
                 provisional_label = tk.Label(self,text = "NONE")
                 provisional_widgets.append([provisional_label])
                 
                   
              self.__widgets[technique_name] = provisional_widgets
    
          self.__title_label.grid(row = self.__row_position, column = 0, padx = 5, pady = 5)
          self.__row_position += 1
          self.__option_radiobutton_label.grid(row = self.__row_position, column = 0, padx = 5, pady = 5)
          self.__row_position += 1

          for technique_name in self.__options_list:
              self.__rb = tk.Radiobutton(self, text = technique_name, variable = self.__current_variable, value = technique_name,command = self.__update_widgets)
              self.__rb.grid(row = self.__row_position, column = 0, padx = 5, pady = 5)
              self.__row_position += 1
          
          self.__parameters_label.grid(row = self.__row_position, column = 0, padx = 5, pady = 5)
          self.__row_position += 1

          #self.__separator.grid(row =2,column = 0,columnspan = 12, padx = 5, pady = 5, sticky="ew")

          self.__update_widgets()        
      
    
      def __update_widgets(self):   
          #Eliminar las viejas          
          for old_widget in self.__widgets[self.__old_variable]:
              for element in old_widget:
                  element.grid_forget()
             
          #Poner las nuevas
          counter = self.__row_position
          for current_widget in self.__widgets[self.__current_variable.get()]:
              for position in range (len(current_widget)): 
                  current_widget[position].grid(row = counter, column = position, padx = 5, pady = 5,)
              counter += 1   
            
          self.__old_variable = self.__current_variable.get()
          self.__parameters_label.config(text = "Additional parameters for {0}:".format(self.__current_variable.get()))
       

      def __grid_general_widgets(self):      
          self.__title_label.grid(row = self.row_position, column = 0, padx = 5, pady = 5)
          self.row_position += 1

          self.__option_menu_label.grid(row = self.row_position, column = 0, padx = 5, pady = 5)
          self.__option_menu.grid(row = self.row_position, column = 1, padx = 5, pady = 5)
          self.row_position += 1

          self.__parameters_label.grid(row = self.row_position, column = 1, padx = 5, pady = 5)
          #self.__separator.grid(row =2,column = 0,columnspan = 12, padx = 5, pady = 5, sticky="ew")
          self.row_position += 1
          self.__update_widgets()        


      def get_information(self):
          selected_technique = self.__current_variable.get()
          selected_class = self.__path + self.__options[selected_technique]["class"]
          selected_options = {}
          technique_parameters = self.__options[selected_technique]["parameter"]
          technique_widgets = self.__widgets[selected_technique]             
          
          for x in range (len(technique_parameters)):
              current_parameter = technique_parameters[x]["value"]
              current_value =  technique_widgets[x][1].get()
              selected_options[current_parameter] = current_value
        
          return { self.__class_name + "_class": selected_class,
                   self.__class_name + "_options": selected_options }
