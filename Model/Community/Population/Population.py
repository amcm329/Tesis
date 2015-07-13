#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import Individual as i


#Complete population flag will be used in the corresponding methods, not here.
class Population:
      """Método para inicializar los elementos de la Poblacion."""
      def __init__(self,population_size,length_subchromosomes,vector_functions,vector_variables,available_expressions,decimal_precision):
          self.__population = []
          self.__population_size = population_size
          self.__length_subchromosomes = length_subchromosomes
          self.__vector_functions = vector_functions
          self.__vector_variables = vector_variables 
          self.__available_expressions = available_expressions        
          self.__decimal_precision = decimal_precision
          
          #valor que se usa muchas veces, por eso se pone como atributo.  
          self.__length_vector_functions = len(vector_functions)
          self.__total_fitness = [0]*self.__length_vector_functions
          self.__total_expected_values = [0]*self.__length_vector_functions


      def get_population(self):
          return self.__population


      def get_length_subchromosomes(self):
          return self.__length_subchromosomes


      def get_length_vector_functions(self):
          return self.__length_vector_functions


      def get_total_fitness(self,position):
          return self.__total_fitness[position]


      def set_total_fitness(self,position,value):
          self.__total_fitness[position] = value


      def get_total_expected_value(self,position):
          return self.__total_expected_values[position]


      def set_total_expected_value(self,position,value):
          self.__total_expected_values[position] = value      

     
      def add_individual(self,complete_chromosome):
          self.__population.append(i.Individual(complete_chromosome,self.__length_subchromosomes,self.__vector_functions,self.__available_expressions,self.__decimal_precision))
          
      
      def calculate_individuals_properties(self):
          for individual in self.__population:
              for x in range (self.__length_vector_functions):
                  #Assigning selection probability
                  individual.set_selection_probability(x,individual.get_fitness(x)/self.__total_fitness[x])
                  #Assigning expected value.
                  individual.set_expected_value(x,individual.get_fitness(x)/(self.__total_fitness[x]/self.__population_size))
                  #Assigning total expected value
                  self.__total_expected_values[x] += individual.get_expected_value(x)     


      def fitness_compare(x, y):
          if x > y:
             return 1
          elif x == y:
             return 0
      else:  #x < y
          return -1

      
      def functions_compare(x,y):
          pass      


      def print_population(self):
          print "Total fitness: " + str(self.__total_fitness)
          print "Total expected value: " + str(self.__total_expected_values)
          print "Individuals: "
          for x in range (self.__population_size):
              print "Number: " + str(x)
              self.__population[x].print_info()      
