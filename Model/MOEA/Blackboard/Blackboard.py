#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import math as m
import random as r
import Population.Population as p

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
          
"""Método que crea un cromosoma binario."""
def __create_binary_chromosome(length_chromosome):
    chromosome = []
            
    for x in range(0,length_chromosome):
        number = r.randint(0,1)
        chromosome.append(number)
         
    return chromosome


def __create_float_point_chromosome(vector_ranges,decimal_precision):
    chromosome = []
    precision_string = "{0:." + str(decimal_precision) + "f}"
    for my_range in vector_ranges:
        lower_limit = my_range[0]
        upper_limit = my_range[1]
        number = r.uniform(lower_limit,upper_limit)
        chromosome.append(float(precision_string.format(number)))

    return chromosome


"""Método que calcula la longitud de todos los subcromosomas. Para ello
se hace uso del vector de rangos, así como de la precisión decimal."""
#Binary use only
def __calculate_length_subchromosomes(vector_ranges,decimal_precision):
    true_decimal_precision = 10**decimal_precision
    lower_limit = -1
    upper_limit = -1
    amount = -1
    how_many_bits_around = -1
    how_many_bits_real = -1
    length_subchromosomes = []
    #contador = 0
    for my_range in vector_ranges:
        #print "Hola",contador," ",my_range
        #contador+=1
        lower_limit = my_range[0]
        upper_limit = my_range[1]
        #print "Lower: ",lower_limit
        #print "Upper: ",upper_limit 
        amount = (upper_limit - lower_limit)*true_decimal_precision
        #print "Amount: ",amount
        how_many_bits_around = m.log(amount,2) 
        #print "Mas o menos: ",how_many_bits_around
        how_many_bits_real = int(m.ceil(how_many_bits_around))
        #print "Real: ",how_many_bits_real
        length_subchromosomes.append(how_many_bits_real)
        #print "----------------------------------------------"

    return length_subchromosomes



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


def create_population(representation,chromosome_set,length_subchromosomes,decimal_precision,vector_functions,vector_ranges,fitness_mode,fitness_options_extra):
    return p.Population(representation,chromosome_set,length_subchromosomes,decimal_precision,vector_functions,vector_ranges,fitness_mode,fitness_options_extra)


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
             
     

#Toda la mierda del blackboard y
def blackboard(population):
    pass

"""
[chromosomes,length_subchromosomes] = create_chromosomes(0,8,3,["10*x+y","x*y","34*x-y"],[[-3,3],[-2,2]])
#representation,chromosome_set,length_subchromosomes,decimal_precision,vector_functions,vector_ranges,fitness_mode,fitness_options_extra   
poblacion = create_population(0,chromosomes,length_subchromosomes,3,["10*x+y","x*y","34*x-y"],[[-3,3],[-2,2]],2,[])
print type(poblacion)
poblacion.print_population()
#my_pob = st.stochastic,universal(poblacion,0)

#print my_pob
""" 