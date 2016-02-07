#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import Tkinter as tk
import matplotlib.pyplot as mp
import math

from Home.HomeFrame import *
from DecisionVariable.DecisionVariableFrame import *
from ObjectiveFunction.ObjectiveFunctionFrame import *
from Population.PopulationFrame import *
from GeneticOperator.GeneticOperatorFrame import *
from MOEA.MOEAFrame import *

import Controller.Controller as controlador

TITLE_FONT = ("Helvetica", 18, "bold")

#No olvidar poner estos valores para mutacion                         
#"decimal_precision_floatpoint_mutation":decimal_precision,
#"vector_variables_floatpoint_mutation":vector_variables}

#Poner un diccionario para entradas principales
class MainWindow():
      
      def __init__(self):
          self.__root = tk.Tk()   
          self.__root.title('MOEA Grapher')
          self.__root.geometry('800x800')
          self.__root.config(bg="#3366ff")

          self.__initial_data = [("Home",HomeFrame),("Decision Variables",DecisionVariableFrame),("Objective Functions",ObjectiveFunctionFrame),("Population Settings",PopulationFrame),("Genetic Operators Settings",GeneticOperatorFrame),("MOEAs Settings",MOEAFrame)]
          self.__frames = {}        

          #MARCO PARA LOS BOTONES DE EJECUCION  
          self.marcobot = tk.Frame(self.__root, bd=5, height = 50, width = 5, relief="groove")
          self.borrar = tk.Button(self.marcobot, text="Borrar ")
          self.ejecutar = tk.Button(self.marcobot,name = "hola<<<<<<<<<<<<<<<<<<",text="Ejecutar ")
          self.ejecutar.bind('<ButtonRelease-1>',self.get_information)
          self.borrar.pack()
          self.ejecutar.pack()
          self.marcobot.pack(side = tk.BOTTOM, fill = tk.X)
          
          
          #MARCO PARA PONER LAS OPCIONES PRINCIPALES DEL PROGRAMA
          self.marco = tk.Frame(self.__root, bd=5, height = 50, width = 5, relief="groove")
          self.__listbox = tk.Listbox(self.marco)
          #self.__listbox.pack(fill=tk.BOTH, expand=1)
          for element in self.__initial_data:       
              self.__listbox.insert(tk.END,element[0]) 
 
          self.__listbox.bind('<ButtonRelease-1>',self.evento)
          self.__listbox.itemconfig(0, background='green')
          self.__listbox.itemconfig(0, selectbackground='green')
          self.__listbox.pack(side = tk.LEFT)  
          self.marco.pack(side = tk.LEFT,fill = tk.Y)
          self.__old_selection = 0
          self.__old_frame_selection = self.__initial_data[0][0]
          
          
          main_features = controlador.load_features("Features.xml")
          print main_features        
 
          for element in self.__initial_data:
              sub_frame = element[1]
              name = element[0]
             
              if main_features.has_key(name):
                 self.__frames[name] = sub_frame(self.__root,main_features[name])
              
              else:
                 self.__frames[name] = sub_frame(self.__root)
              

          self.__frames['Home'].pack(expand = True,fill = tk.BOTH)
          
       
 
      def get_information(self,event):
          for frame in self.__frames.keys():
              current_frame = self.__frames[frame]
              invert_op = getattr(current_frame, "get_information", None) 
              if callable(invert_op):
                 print "Frame: ", frame
                 print current_frame.get_information()
                
      def run(self):
          self.__root.mainloop() 


      def graph(self,event):
         """
         self.x1 = [1,2,3,4,5,6]
         self.y1 = [1,4,6,8,10]

         #for i in range(len(self.entry_x)):
         #    self.x1.append(float(self.entry_x[i].get())) 

         #for i in range(len(self.entry_y)):
         #    self.y1.append(float(self.entry_y[i].get()))

         mp.ion()
         mp.plot(self.x1, self.y1)  
         mp.title('Wykres')
         mp.xlabel('x')
         mp.ylabel('y')
         mp.draw()
         """
         self.__frames["Genetic Operators Settings"].get_information()


      def evento(self,event):
          widget = event.widget
          selection=widget.curselection()
          print "Selection: ", selection
          value = widget.get(selection[0])

#          print "La cosa valiosa: ",value 

          widget.itemconfig(self.__old_selection,selectbackground = 'white')
          widget.itemconfig(self.__old_selection, background='white')
         
          widget.itemconfig(int(selection[0]), selectbackground='green')
          widget.itemconfig(int(selection[0]), background='green')
          
  #        print "Tipo: ",type(self.__old_selection)
          self.__frames[self.__old_frame_selection].pack_forget()	
          self.__frames[value].pack(expand = True, fill = tk.BOTH) 

                     
          self.__old_selection = int(selection[0])
          self.__old_frame_selection = value 
 #         print "Selection 2:", selection, ": '%s'" % value             
           

         
          #Verificar si es necesario
          #self.__root.update()

main_window = MainWindow()
main_window.run()

