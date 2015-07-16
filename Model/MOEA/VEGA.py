#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import random as r
import Community.Community as com

#No tiene completar population porque eso le corresponde al controlador, no a esto.
#Verificar el caso de las poblaciones incompletas.
#Verificar el caso de las selecciones incompletas. 
#representation options = gray coding.


agregar método create_population

def create_subpopulations(main_population,subpopulations_amount):
    subpopulations = []
    how_many_individuals = population_size
    how_many_objectives = length_vector_functions
    lower_limit = 0
    upper_limit = 0
    for y in range (length_vector_functions):
          #This guarantees selection in an critera given (poner como objetivo o alguna mierda así)
          selection_options[0] = y

          individuals_per_objective = int(how_many_individuals/how_many_objectives)
          upper_limit += individuals_per_objective   
          provisional_parents = parents_chromosomes[lower_limit:upper_limit]
          local_parents = com.create_population(representation,provisional_parents,length_subchromosomes,decimal_precision,vector_functions,vector_ranges,fitness_mode,fitness_options_extra)
          selected_parents_chromosomes += provisional_parents_chromosomes 
          lower_limit = upper_limit
          how_many_individuals -= individuals_per_objective
          how_many_objectives -= 1
      
    return subpopulations[]





def vega_algorithm(generations,population_size,vector_functions,vector_variables,available_expressions,decimal_precision,representation_class,representation_options,fitness_class,fitness_method,fitness_options,selection_class,selection_method,selection_options,crossover_class,crossover_method,crossover_options,mutation_class,mutation_method,mutation_options,elithism_number): 
    
    length_vector_functions = len(vector_functions)
    final_information = [0]*length_vector_functions
    community = com.Community()     
    parents = community.init_population()

    for x in range (generations):
        #print "Generation: ", x
        #elegir las n/k individuos (automaticamente se evaluan primero)
        #juntar toda la poblacion
        selected_parents_chromosomes = []
        childrens_chromosomes = []
        next_generation_chromosomes = []
        best_individuals_per_generation = []
        

        global_parents = com.create_population(representation,parents_chromosomes,length_subchromosomes,decimal_precision,vector_functions,vector_ranges,fitness_mode,fitness_options_extra)
        
       
                
        while (selected_parents_chromosomes != []):
              
        children =  com.create_population(representation,childrens_chromosomes,length_subchromosomes,decimal_precision,vector_functions,vector_ranges,fitness_mode,fitness_options_extra) 
          
        
               com.elitism(parents,children)
        



        #as much individuals for generation as number of functions.
        #adding the best elements for generation
        for x in range (length_vector_functions):
            best_individual = children.get_best_individual(x).get_evaluated_function(x)
            final_information[x].append(best_individual)

        #final_information.append(best_individuals_per_generation)

        for kid in children.get_population():
            next_generation_chromosomes.append(kid.get_complete_chromosome())

        parents_chromosomes = next_generation_chromosomes

   
    return final_information
