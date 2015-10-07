#! /usr/bin/python

class Hola:
   
      def __init__(self,hola):
          self.hola = hola


      def imprime(self):
          print "Jaja: " + str(self.hola)


"""El error que tenia de que se imprimia None viene de imprimir un metodo, aun cuando el cuerpo del metodo ya estuviera imprimiendo algo."""
hola = Hola(2)
print hola.imprime()


#Para ordenar elementos con base en funciones con parametros.
#def sort_individuals(self,method,position,is_descendent=True):
#    self.__population.sort(key=operador.methodcaller(method,position),reverse=is_descendent)
