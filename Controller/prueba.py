import os
import xml.etree.ElementTree as et
from operator import itemgetter

class perro:
     
      def __init__(self,hola,mundo):
          self.hola = hola
          self.mundo = mundo


      def get_hola(self,x):
          return self.hola[x]


      def load_xml_features(self,features_filename):
          category_id = 1
          options = []
          #path = os.path.dirname(__file__)
          #tree = et.parse(path + "/" + features_filename)
          tree = et.parse(features_filename)
          root = tree.getroot()


      #reverse es en orden descendiente
      def make_comparation(x):
          if n[x] > m[x]:
             return 1

          elif n[x] == m[x]:
                   return 0

          else: 
               return -1


perro1 = perro([9,8],7)
perro2 = perro([1,2],-1)
perro3 = perro([0,-1],3)

a = [perro1,perro2]

print "Inicial: ", a 

#a = [3,2,4,5,6,-1,-2,0]
#a.sort(compare(1))
a.sort()

print "Resultado: ", a 
   









