#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import operator as operador 
import random as aleatorio 
import Individual.Individual as individuo

#Complete population flag will be used in the corresponding methods, not here.
class Population:
      """Método para inicializar los elementos de la Poblacion."""
      def __init__(self,population_size,vector_functions,vector_variables,available_expressions,decimal_precision):
          self.__population_size = population_size
          self.__vector_functions = vector_functions
          self.__vector_variables = vector_variables 
          self.__available_expressions = available_expressions        
          self.__decimal_precision = decimal_precision
          
          #valor que se usa muchas veces, por eso se pone como atributo.
          self.__population = [0]*self.__population_size  
          self.__length_vector_functions = len(vector_functions)
          self.__total_fitness = 0
          self.__total_expected_value = 0


      def get_individuals(self):
          return self.__population


      def get_size(self):
          return self.__population_size


      def get_length_vector_functions(self):
          return self.__length_vector_functions


      def get_total_fitness(self):
          return self.__total_fitness


      def set_total_fitness(self,value):
          self.__total_fitness = value


      def get_total_expected_value(self):
          return self.__total_expected_value

 
      def add_individual(self,position,complete_chromosome):
          self.__population[position] = individuo.Individual(complete_chromosome,self.__vector_functions,self.__available_expressions,self.__decimal_precision)
          
      
      def calculate_population_properties(self):
          for individual in self.__population:
              #Assigning expected value.
              expected_value = individual.get_fitness()/(self.__total_fitness/self.__population_size)
              individual.set_expected_value(expected_value)
              #Assigning total expected value
              self.__total_expected_value += expected_value     


      #Método que ordena los individuos en orden descendente.
      def sort_individuals(self,method,is_descendent):
          self.__population.sort(key=operador.methodcaller(method),reverse=is_descendent)


      def shuffle_individuals(self):
          aleatorio.shuffle(self.__population)


      def print_population(self):
          print "Total fitness: " + str(self.__total_fitness)
          print "Total expected value: " + str(self.__total_expected_values)
          print "Individuals: "
          for x in range (self.__population_size):
              print "Number: " + str(x)
              self.__population[x].print_info()      
