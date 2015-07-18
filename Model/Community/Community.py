#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import Population.Population as p

asignar fitness implica de una vez evaluar en funciones objetivo.
#Cambiarle nombre a length subchromosomes
class Community:
      def __init__(self,population_size,vector_functions,vector_variables,available_expressions,decimal_precision,representation_class,representation_options,fitness_class,fitness_method,fitness_options,selection_class,selection_method,selection_options,crossover_class,crossover_method,crossover_options,mutation_class,mutation_method,mutation_options):
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
          self.__selection_class = selection_class
          self.__selection_method = selection_method
          self.__selection_options = selection_options
          self.__crossover_class = crossover_class
          self.__crossover_method = crossover_method
          self.__crossover_options = crossover_options
          self.__mutation_class = mutation_class
          self.__mutation_method = mutation_method
          self.__mutation_options = mutation_options
          
          #Agregados para el create population.
          self.__length_chromosomes = []


      def init_population(self):
          population = []
          chromosome = []
          try:
             rc = __import__(self.__representation_class, globals(), locals(), ['object'], -1)
             self.__length_subchromosomes = getattr(rc,"calculate_length_subchromosomes")(self.__decimal_precision,self.__vector_ranges)              
             population = p.Population(self.__population_size,self.__vector_functions,self.__vector_variables,self.__available_expressions,self.__decimal_precision)
             for x in range (self.__population_size):
                 complete_chromosome =  getattr(rc,"create_chromosome")(self.__length_subchromosomes,self.__decimal_precision,self.__vector_ranges)
                 population.add_individual(x,complete_chromosome)
           
          except:
              population =  "ERROR. Class: Community. Method: init_population. Message: Problem found with chromosomal representation"


          return population


      def create_population(self,set_chromosomes):
          population = p.Population(self.__population_size,self.__vector_functions,self.__vector_variables,self.__available_expressions,self.__decimal_precision)
          for x in range(len(set_chromosomes)):
              population.append(x,set_chromosomes[x])

          return population

      #------------------------------------------------
      
      #This evaluates only functions
      def evaluate_population_functions(self,population):
          code = "OK"
          complete_chromosome = ""
          decision_variables = {}
        
          try:
              rc = __import__(self.__representation_class, globals(), locals(), ['object'], -1)
              individuals = population.get_population()
              for individual in individuals:
                  complete_chromosome = individual.get_complete_chromosome()          
                  decision_variables = getattr(rc,"evaluate_subchromosomes")(complete_chromosome,self.__length_subchromosomes,self.__vector_variables,self.__decimal_precision,self.__representation_options)
                  individual.evaluate_functions(decision_variables)

          except:
              code = "ERROR. Class: Community. Method: evaluate_population_functions. Message: Problem while evaluating functions"

          return code 


      def assign_population_fitness(self,population):
          code = "OK"
          try: 
             fc = __import__(self.__fitness_class, globals(), locals(), ['object'], -1)
             getattr(fc,self.__fitness_method)(population,self.__fitness_options)
                
          except:
               return "ERROR. Class: Community. Method: assign_population_fitness. Message: Problem while assignating fitness" 

          return code


      def evolve_next_generation(self,parents,position):
          children = p.Population(self.__population_size,self.__vector_functions,self.__vector_variables,self.__available_expressions,self.__decimal_precision)
          try:
             st = __import__(self.__selection_class, globals(), locals(), ['object'], -1)
             ct = __import__(self.__crossover_class, globals(), locals(), ['object'], -1)
             mt = __import__(self.__mutation_class, globals(), locals(), ['object'], -1)  
             selected_parents_chromosomes = getattr(st,self.__selection_method)(parents,position,self.__selection_options)   
             for x in range(1,population.get_population_size(),2):
                 chromosome_a = selected_parents_chromosomes[x - 1]
                 chromosome_b = selected_parents_chromosomes[x]
                 [child_1,child_2] = getattr(ct,self.__crossover_method)(chromosome_a,chromosome_b,self.__crossover_options)        
                 modified_child_1 = getattr(mt,self.__mutation_method)(child_1,self.__mutation_options)
                 modified_child_2 = getattr(mt,self.__mutation_method)(child_2,self.__mutation_options)
                 children.add_individual(x - 1,modified_child_1)
                 children.add_individual(x,modified_child_2)
        
              
          except:
               children = "ERROR. Class: Community. Method: evolve_next_generation. Message: Problem while making child population""      


          return children


      #children[i] = parents[i]                     
      def elitism(self,parents,children,is_descendent,function,position,elitism_amount):
          parents.sort_individuals(is_descendent,function,position)
          children.sort_individuals(is_descendent,function,position)
          parents_population = parents.get_population()
          offset = parents.get_size_population() - elitism_amount
          for x in range(0,elitism_amount):
              parent_complete_chromosome = parents_population[i].get_complete_chromosome()
              children.add_individual(x + offset,complete_chromosome)

          

"""
[chromosomes,length_subchromosomes] = create_chromosomes(0,8,3,["10*x+y","x*y","34*x-y"],[[-3,3],[-2,2]])
#representation,chromosome_set,length_subchromosomes,decimal_precision,vector_functions,vector_ranges,fitness_mode,fitness_options_extra   
poblacion = create_population(0,chromosomes,length_subchromosomes,3,["10*x+y","x*y","34*x-y"],[[-3,3],[-2,2]],2,[])
print type(poblacion)
poblacion.print_population()
#my_pob = st.stochastic,universal(poblacion,0)

#print my_pob
""" 
