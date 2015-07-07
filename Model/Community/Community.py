#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import math as m
import random as r
import Population.Population as p


class Community:

      def __init__(self,representation_class,fitness_class,fitness_method,fitness_options):
          self.__representation = representation
          

      #------------------------------------------------
      def init_population():  
         #def create_population(representation,chromosome_set,length_subchromosomes,decimal_precision,vector_functions,vector_ranges,fitness_mode,fitness_options_extra):
    #return p.Population(representation,chromosome_set,length_subchromosomes,decimal_precision,vector_functions,vector_ranges,fitness_mode,fitness_options_extra)
             """Método que inicializa una Población con base en el tamaño (número de Individuos)
      el vector de funciones y el vector de rangos."""
      def __initialize(self,chromosome_set):
          for chromosome in chromosome_set:
              self.__population.append(i.Individual(self.__representation,chromosome,self.__decimal_precision,self.__length_subchromosomes,self.__vector_functions,self.__vector_ranges))
          


      #------------------------------------------------
      
      This evaluates and sorts population
      def evaluate_population():

      def __assign_fitness(self,fitness_method,fitness_options):
          getattr(st,selection_method)(population,fitness_options)
                
          #Proportional fitness
          if fitness_mode == 0:
             self.__assign_proportional_fitness()                      

          #Escalamiento fitness.
          elif fitness_mode == 1:
               alpha = fitness_options_extra[0]
               beta = fitness_options_extra[1]
               self.__assign_scaling_fitness(alpha,beta)        
                         
          #Ranking normal
          elif fitness_mode == 2:
               self.__assign_normal_ranking_fitness()
 
          #Ranking con sp (un poco pendiente)
          elif fitness_mode == 3:
               sp = fitness_options_extra[0]
               self.__assign_sp_ranking_fitness(sp)

          else:
               return "ERROR. Class: Population. Method: assign_fitness. Message: Fitness not implemented yet." 

          pass


      #-----------------------------------------------------------------------------------------------

      def elitism(self,parent_population,children_population,elitism_amount):
           #calcular la posicion del peor individuo en el fitness mode  
      def get_position_worst_individual(self,fitness_position):
          pivot = self.__population[0]
          position = 0
          for x in range (1,self.__population_size):
              provisional = self.__population[x]
              if pivot.get_fitness(fitness_position) > provisional.get_fitness(fitness_position):
                 pivot = provisional
                 position = x

          return position


      #poner el mejor individuo en el fitness mode
      def get_best_individual(self,fitness_position):
          pivot = self.__population[0]
          position = 0
          for x in range (1,self.__population_size):
              provisional = self.__population[x]
              if pivot.get_fitness(fitness_position) < provisional.get_fitness(fitness_position):
                 pivot = provisional
                 position = x

          return pivot
             
          pass


      #-----------------------------------------------------------------------------------------------











def create_chromosomes(representation,population_size,decimal_precision,vector_functions,vector_ranges):
    my_chromosome_set = []
    length_subchromosomes = []

    #Create chromosomes 
    """Se crea un cromosoma para cada Individuo."""
    if representation == 0 or representation == 1:
         length_my_complete_chromosome = 0

         length_subchromosomes = __calculate_length_subchromosomes(vector_ranges,decimal_precision)

         for value in length_subchromosomes:
             length_my_complete_chromosome += value
                  
         for x in range (population_size):
             my_chromosome_set.append(__create_binary_chromosome(length_my_complete_chromosome))

    elif representation == 2:   
         length_subchromosomes = [1]*len(vector_ranges)
         for x in range (population_size): 
             my_chromosome_set.append(__create_float_point_chromosome(vector_ranges,decimal_precision))

    else:
         return "ERROR. Class: BlackboardResponsible. Method: create_chromosomes. Message: Representation not implemented yet." 
          
    
    return [my_chromosome_set,length_subchromosomes]


     
"""
[chromosomes,length_subchromosomes] = create_chromosomes(0,8,3,["10*x+y","x*y","34*x-y"],[[-3,3],[-2,2]])
#representation,chromosome_set,length_subchromosomes,decimal_precision,vector_functions,vector_ranges,fitness_mode,fitness_options_extra   
poblacion = create_population(0,chromosomes,length_subchromosomes,3,["10*x+y","x*y","34*x-y"],[[-3,3],[-2,2]],2,[])
print type(poblacion)
poblacion.print_population()
#my_pob = st.stochastic,universal(poblacion,0)

#print my_pob
""" 
