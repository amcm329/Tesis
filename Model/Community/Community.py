#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import Population.Population as p


#Cambiar nombre a length subchromosomes
class Community:
      def __init__(self,population_size,vector_functions,vector_variables,available_expressions,decimal_precision,representation_class,representation_options,fitness_class,fitness_method,fitness_options)):
          self.__population_size = population_size
          self.__vector_functions = vector_functions
          self.__vector_variables = vector_variables
          self.__available_expressions = available_expressions
          self.__decimal_precision = decimal_precision
          self.__representation_class = representation_class
          self.__representation_options = representation_options
          self.__fitness_class = fitness_class
          self.__fitness_method = fitness_method
          self.__fitness_options = fitness_options
          
          
      def init_population(self):
          population = []
          chromosome = []
          try:
             rc = __import__(self.__representation_class, globals(), locals(), ['object'], -1)
             length_subchromosomes = getattr(rc,"calculate_length_subchromosomes")(self.__decimal_precision,self.__vector_ranges)              
             population = p.Population(self.__population_size,length_subchromosomes,self.__vector_functions,self.__vector_variables,self.__available_expressions,self.__decimal_precision)
             for x in range (self.__population_size):
                 complete_chromosome =  getattr(rc,"create_chromosome")(length_subchromosomes,self.__decimal_precision,self.__vector_ranges)
                 population.add_individual(complete_chromosome)
           
          except:
              population =  "ERROR. Class: Community. Method: init_population. Message: Problem found with chromosomal representation"


          return population



      #------------------------------------------------
      
      #This evaluates only functions
      def evaluate_population_functions(self,population):
          code = "OK"
          complete_chromosome = ""
          decision_variables = {}
          length_subchromosomes = population.get_length_subchromosomes() 
          try:
              rc = __import__(self.__representation_class, globals(), locals(), ['object'], -1)
              individuals = population.get_population
              for individual in individuals:
                  complete_chromosome = individual.get_complete_chromosome()          
                  decision_variables = getattr(rc,"evaluate_subchromosomes")(complete_chromosome,length_subchromosomes,self.__vector_variables,self.__decimal_precision,self.__representation_options)
                  individual.evaluate_functions(decision_variables)

          except:
              code = "ERROR. Class: Community. Method: evaluate_population_functions. Message: Problem while evaluating functions"

          return code 


      def assign_population_fitness(self,population):
          code = "OK"
          try: 
             fc = __import__(self.__fitness_class, globals(), locals(), ['object'], -1)
             getattr(fc,fitness_method)(population,fitness_options)
                
          except:
               return "ERROR. Class: Community. Method: assign_population_fitness. Message: Problem while assignating fitness" 

          return code


      #-----------------------------------------------------------------------------------------------


      #children[i] = parents[i]                     
      def elitism(self,parents,children,position,elitism_amount):
          estos metodos mandarlos llamar desde la poblacion, poniendo el metodo y la posicion como variable.
          parents.get_population().sort(key=o.method_caller("get_fitness",position),reverse=True)
          children.
          hacer que el metodo add 

          pass


      #-----------------------------------------------------------------------------------------------


      def disorder_population(self,population):
          r.shuffle(population.get_population)
     
"""
[chromosomes,length_subchromosomes] = create_chromosomes(0,8,3,["10*x+y","x*y","34*x-y"],[[-3,3],[-2,2]])
#representation,chromosome_set,length_subchromosomes,decimal_precision,vector_functions,vector_ranges,fitness_mode,fitness_options_extra   
poblacion = create_population(0,chromosomes,length_subchromosomes,3,["10*x+y","x*y","34*x-y"],[[-3,3],[-2,2]],2,[])
print type(poblacion)
poblacion.print_population()
#my_pob = st.stochastic,universal(poblacion,0)

#print my_pob
""" 
