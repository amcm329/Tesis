import Tkinter as tk
import tkMessageBox as tkm
#Usar column configure
class ObjectiveFunctionFrame(tk.Frame):
      
         def __init__(self,parent,options = None):
             #Create elements
             tk.Frame.__init__(self,parent, bd=5, height = 12, width = 12, relief="groove")
            
             self.__rows = []

             self.__i = 2

             self.__add_column()

             self.__button1 = tk.Button(self, text="Add")
             self.__button1.bind('<ButtonRelease-1>',self.__onPress)
             self.__button1.grid(row = 0, column = 1)

             self.__name_label = tk.Label(self, text="Name")
             self.__name_label.grid(row = 1, column = 0)
             

         def __add_column(self):  
             columns = []

             e = tk.Entry(self,relief="ridge")
             e.grid(row=self.__i, column=0, sticky="nsew")
             e.insert(tk.END, '%d' % (self.__i))
             columns.append(e)

             b = tk.Button(self,text="X")
             b.bind('<ButtonRelease-1>',self.__delete_column)
             b.grid(row=self.__i, column=1, sticky="nsew")
             columns.append(b)       
             self.__rows.append(columns)
             self.__i += 1

         def __onPress(self,event):
             self.__add_column()              

         #Falta reasignar elementos en el grid para que concuerden con la nueva numeracion
         def __delete_column(self,event):
             if len(self.__rows) > 1:
                my_i = 2
                information = event.widget.grid_info()
               # print "jajajaja: ",information
                location = int(information['row']) -2

               # print "Hola 2: ",self.__rows
                for element in self.__rows[location]:
                    element.destroy()
             
                del self.__rows[location]
              #  print "-------------------------"

             #   print "Hola: ", self.__rows

              
                for element in self.__rows:
                     for y in range (2):
                         element[y].grid(row=my_i, column=y, sticky="nsew")

                         #Solo para reescrir elementos
                         if y in range(0,1):
                            element[y].delete(0,tk.END)
                            element[y].insert(tk.END, '%d.%d' % (my_i, y))
                     my_i+=1  

                self.__i = my_i
                 
   
             else:
                  tkm.showinfo("Warning", "At least one objective function must be available.")


         def get_information(self):
             vector_functions = []
             for row in self.__rows:
                 vector_functions.append(row[0].get())
              
             return {'vector_functions': vector_functions}


