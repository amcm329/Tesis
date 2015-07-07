#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import math as m
import random as r
import Individual as i

falta el numero de elitismos.
Conviene ordenar a los elementos por fitness para así hacer el elitismo de n n metodos.
El elitismo hay que ponerlo en blackboard.


class Population:
      #fitness options, en caso de que se requiera se añaden elementos adicionales en fitness options.
      #There's no need for using the population size as a parameter, because we already have the chromosome_set.
      #The complete population flag will be used in the corresponding methods, not here.
      """Método para inicializar los elementos de la Poblacion."""
      def __init__(self,chromosome_set,length_subchromosomes,decimal_precision,vector_functions,vector_ranges):
          
          
          #valor que se usa muchas veces, por eso se pone como atributo.  
          self.__population = []
          self.__length_vector_functions = len(vector_functions)
          self.__population_size = len(chromosome_set)
          self.__length_subchromosomes = length_subchromosomes
          self.__decimal_precision = decimal_precision
          self.__vector_functions = vector_functions
          self.__vector_ranges = vector_ranges          
          self.__total_fitness = [0]*self.__length_vector_functions
          self.__total_expected_values = [0]*self.__length_vector_functions
          
  
          def _assign rest of the elements, despues de haberse evaluado las clases.
          for individual in self.__population:
              for x in range (self.__length_vector_functions):
                  #Assigning selection probability
                  individual.set_selection_probability(x,individual.get_fitness(x)/self.__total_fitness[x])
                  #Assigning expected value.
                  individual.set_expected_value(x,individual.get_fitness(x)/(self.__total_fitness[x]/self.__population_size))
                  #Assigning total expected value
                  self.__total_expected_values[x] += individual.get_expected_value(x)        


      def get_length_vector_functions(self):
          return self.__length_vector_functions

      def get_population_size(self):
          return self.__population_size

      def get_total_fitness(self,position):
          return self.__total_fitness[position]

      def set_total_fitness(self,position,value):
          self.__total_fitness[position] = value

      def get_total_expected_value(self,position):
          return self.__total_expected_values[position]

      def get_population(self):
          return self.__population

      #No lo estás evaluando, pero a la siguiente vuelta de la generación se evalúa.
      def set_individual(self,position,new_individual):
          self.__population[position] = new_individual

     
      def print_population(self):
          print "Total fitness: " + str(self.__total_fitness)
          print "Total expected value: " + str(self.__total_expected_values)
          print "Individuals: "
          for x in range (self.__population_size):
              print "Number: " + str(x)
              self.__population[x].print_info()      