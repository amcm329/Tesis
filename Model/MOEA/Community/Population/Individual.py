#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import math as m

class Individual:
      #Representation is only used at the beginning, that's why we never use it as an attribute.
      #Decimal precision used as a parameter because python doesnt want to truncate precision by itself.     
      def __init__(self,representation,complete_chromosome,decimal_precision,length_subchromosomes,vector_functions,vector_ranges):

          self.__precision_string = "{0:." + str(decimal_precision) + "f}"  

          self.__complete_chromosome = complete_chromosome
          self.__evaluated_subchromosomes = []
          self.__fitness = [0]*len(vector_functions)
          self.__selection_probabilities = [0]*len(vector_functions)
          self.__expected_values = [0]*len(vector_functions)
          
          if representation == 0: #Evaluated subchromosomes. Binary representation. NO gray coding.
             self.__evaluate_binary_subchromosomes(complete_chromosome,vector_ranges,length_subchromosomes,False)

          elif representation == 1:  #Evaluated subchromosomes. Binary representation with gray coding
             self.__evaluate_binary_subchromosomes(complete_chromosome,vector_ranges,length_subchromosomes,True)
         
          elif representation == 2:  #At this point we don't need any representation, so it's enough to making the assignment to the complete chromosome with the evaluated subchromosomes because they are already "evaluated".   
             self.__evaluated_subchromosomes = complete_chromosome

          else:
             return "ERROR. Class: Individual. Method: __init__. Message: Representation not implemented yet."    
        
          #This attribute has to be public in order to give it a ranking fitness.
          self.evaluated_functions = self.__evaluate_functions(vector_functions,self.__evaluated_subchromosomes)   
      
         
      def __evaluate_binary_subchromosomes(self,complete_chromosome,vector_ranges,length_subchromosomes,gray_coding): 
          lower_limit = 0
          upper_limit = 0
          subchromosome = []
          
          for i in range (0,len(length_subchromosomes)):
              m = length_subchromosomes[i]
              subrange = vector_ranges[i]
              a = subrange[0]
              b = subrange[1]
              upper_limit += m
              subchromosome = complete_chromosome[lower_limit:upper_limit]
              #print "El subcromosoma del agente: ",self.__individual_id," es:",subchromosome
              if gray_coding == True:
                      gray_subchromosome = [subchromosome[0]]
                      
                      for j in range (1,len(subchromosome)):
                          gray_subchromosome.append(subchromosome[j]^subchromosome[j-1])
                     
                      subchromosome = gray_subchromosome   
                          
              decimal_number = self.__binary_to_decimal(subchromosome)
              number = a + (decimal_number*((b-a)/((2.0**m) - 1)))
              #print "El number del agente ", self.__individual_id, " es: ",number             
              
              self.__evaluated_subchromosomes.append(float(self.__precision_string.format(number)))
              lower_limit = upper_limit

      
      def __binary_to_decimal(self,chromosome):
          m = len(chromosome) - 1
          number = 0

          for i in range (m,-1,-1):
              number += chromosome[m-i]*(2**i)
          
          return number

             
      def __evaluate_one_function(self,function,x,y):      
          evaluation = eval(function,{"x":x,"y":y,"sin":m.sin,"cos":m.cos,"tan":m.tan,"e":m.e,"pi":m.pi})
          return float(self.__precision_string.format(evaluation))


      def __evaluate_functions(self,vector_functions,evaluated_subchromosomes):
          evaluation_of_functions = []
              
          for function in vector_functions:
              result = self.__evaluate_one_function(function,evaluated_subchromosomes[0],evaluated_subchromosomes[1])
              evaluation_of_functions.append(result)
               
          return evaluation_of_functions
                 
                       
      def get_complete_chromosome(self):
          return self.__complete_chromosome
           

      def get_evaluated_function(self,position):
          return self.evaluated_functions[position]

      #-------------------------------------------------------------------    
      

      def get_fitness(self,position):
          return self.__fitness[position]


      def set_fitness(self,position,fitness):
          self.__fitness[position] = float(self.__precision_string.format(fitness))

      #-------------------------------------------------------------------
    
      def get_selection_probability(self,position):
          return self.__selection_probability[position]
      

      def set_selection_probability(self,position,selection_probability):
          self.__selection_probabilities[position] = float(self.__precision_string.format(selection_probability))

      #-------------------------------------------------------------------   
       
 
   
      """Número de copias"""    
      def get_expected_value(self,position):
          return self.__expected_values[position]

      
      def set_expected_value(self,position,expected_value):
          self.__expected_values[position] = float(self.__precision_string.format(expected_value))

       #-------------------------------------------------------------------
    

      def print_info(self):
           print "    Complete chromosome: " + str(self.__complete_chromosome)
           print "    Decision variables: " + str(self.__evaluated_subchromosomes)
           print "    Evaluated functions: " + str(self.evaluated_functions)
           print "    Fitness: " + str(self.__fitness)
           print "    Selection probabilites: " + str(self.__selection_probabilities)
           print "    Expected values: " + str(self.__expected_values)
           print "\n"
