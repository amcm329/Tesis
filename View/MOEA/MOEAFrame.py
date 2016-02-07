import Tkinter as tk
import tkMessageBox as tkm
#Usar column configure


from AlgorithmFrame import *
from SharingFunctionFrame import *

class MOEAFrame(tk.Frame):
       
      def __init__(self, parent, options = None):
          tk.Frame.__init__(self,parent, bd=5, relief="groove")
          self.__general_options = options     
          self.__frames_instances = [("MOEA",AlgorithmFrame),("SharingFunction",SharingFunctionFrame)]
          self.__frames = []
          for frame in self.__frames_instances:
              initial_frame = frame[1](self,frame[0],self.__general_options[frame[0]])
              initial_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True)
              self.__frames.append(initial_frame)

     
      def delete_content(self):
          pass
     
      def get_information(self):
          #concatenar diccionarios
          moea_information = {}
          for current_frame in self.__frames:
              moea_information.update(current_frame.get_information())
       
          return moea_information
       
