#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import math


#Decimal precision used as a parameter because python doesnt want to truncate precision by itself.     
class Individual:
      def __init__(self,complete_chromosome,vector_functions,available_expressions,decimal_precision):
          self.__complete_chromosome = complete_chromosome
          self.__vector_functions = vector_functions
          self.__available_expressions = available_expressions
          self.__precision_string = "{0:." + str(decimal_precision) + "f}"

          self.__decision_variables = {}
          self.__evaluated_functions = []
          self.__dominates = 0
          self.__is_dominated = 0
          self.__fitness = 0
          self.__niche_count = 0
          self.__expected_value = 0


      def get_complete_chromosome(self):
          return self.__complete_chromosome

      def get_vector_functions(self):
          return self.__vector_functions


      def get_decision_variables(self):
          return self.__decision_variables
           

      def get_evaluated_function(self,position):
          return self.__evaluated_functions[position]


      def get_pareto_dominates(self):
          return self.__dominates


      def set_pareto_dominates(self,value):
          self.__dominates = value     


      def get_pareto_dominated(self):
          return self.__is_dominated


      def set_pareto_dominated(self,value):
          self.__is_dominated = value     

      
      def get_fitness(self):
          return self.__fitness


      def set_fitness(self,value):
          self.__fitness = value     

     
      def get_niche_count(self):
          return self.__niche_count
 

      def set_niche_count(self,value):
          self.__niche_count = value

     
      """Número de copias"""    
      def get_expected_value(self):
          return self.__expected_value


      def set_expected_value(self,value):
          self.__expected_value = value
   

      # Expressions = variables + constants + user built-in functions
      def __evaluate_single_function(self,function,expressions): 
          evaluation = eval(function,expressions)
          return float(self.__precision_string.format(evaluation))


      def evaluate_functions(self,decision_variables):
          self.__decision_variables = decision_variables
          #print "Decision variables: ", self.__decision_variables
          all_expressions = {}
          all_expressions.update(self.__decision_variables)
          all_expressions.update(self.__available_expressions)
          #print "All expressions: ", all_expressions
          #print "Available expressions: ",self.__available_expressions
          for function in self.__vector_functions:
              result = self.__evaluate_single_function(function,all_expressions)
              self.__evaluated_functions.append(result)
                            

      def print_info(self):
           print "    Complete chromosome: " + str(self.__complete_chromosome)
           print "    Decision variables: " + str(self.__evaluated_subchromosomes)
           print "    Evaluated functions: " + str(self.__evaluated_functions)
           print "    Fitness: " + str(self.__fitness)
           print "    Selection probabilites: " + str(self.__selection_probabilities)
           print "    Expected values: " + str(self.__expected_values)
           print "\n"
