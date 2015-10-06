import os
import xml.etree.ElementTree as et
import operator
from random import shuffle


class perro:
     
      def __init__(self,hola,mundo):
          self.hola = hola
          self.mundo = mundo

      def get_mundo(self):
          return self.mundo

      def get_hola(self,x):
          return self.hola[x]

      def printear(self):
          print "Hola: " + str(self.hola) + ", Mundo: " + str(self.mundo)

   
perro1 = perro([9,1],7)
perro2 = perro([1,9],-1)
perro3 = perro([0,6],3)

#a = [perro3,perro1,perro2]
a = [1,2,3,4,5,6,7,8,9]

print "Inicial: ",a

#for p in a:
#    p.printear() 


#a.sort(compare(1))
#a.sort(key=operator.methodcaller("get_hola",2),reverse=True)
#a.sort(key=operator.methodcaller("get_hola",1),reverse=True)

shuffle(a)

print "Resultado: ",a
 
  
#for p in a:
    #p.printear() 




z = ["a",3,2,"aa","a","ab",34,-1,"ba"]

print "Z: ", z

k =  range(len(z))

for x in z:
    perro = x
    if type(perro) == str:
       #print "Entro: " + str(perro) + " Position: " + str(x)
       if "a" in perro:
           print "Encontre: ", perro
           z.remove(perro)
       
       print "El z: ", z       

print "Z: ", z
 








