#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import random as r
import Blackboard.Blackboard as br

#No tiene completar population porque eso le corresponde al controlador, no a esto.
#Verificar el caso de las poblaciones incompletas.
#Verificar el caso de las selecciones incompletas.
def vega_algorithm(generations,population_size,vector_functions,vector_ranges,decimal_precision,representation,fitness_class,fitness_method,fitness_options,selection_class,selection_method,selection_options,crossover_class,crossover_method,crossover_options,mutation_class,mutation_method,mutation_options,elithism_number):
    st = __import__(selection_class, globals(), locals(), ['object'], -1)
    ct = __import__(crossover_class, globals(), locals(), ['object'], -1)
    mt = __import__(mutation_class, globals(), locals(), ['object'], -1) 
    length_vector_functions = len(vector_functions)
    final_information = []     
    [parents_chromosomes,length_subchromosomes] = br.create_chromosomes(representation,population_size,decimal_precision,vector_functions,vector_ranges)
    
    for z in range (length_vector_functions):
        final_information.append([])

    for x in range (generations):
        #print "Generation: ", x
        #elegir las n/k individuos (automaticamente se evaluan primero)
        #juntar toda la poblacion
        selected_parents_chromosomes = []
        childrens_chromosomes = []
        next_generation_chromosomes = []
        best_individuals_per_generation = []
        how_many_individuals = population_size
        how_many_objectives = length_vector_functions
        lower_limit = 0
        upper_limit = 0

        global_parents = br.create_population(representation,parents_chromosomes,length_subchromosomes,decimal_precision,vector_functions,vector_ranges,fitness_mode,fitness_options_extra)
        
        for y in range (length_vector_functions):
            #This garantices selection in an critera given
            selection_options[0] = y

            individuals_per_objective = int(how_many_individuals/how_many_objectives)
            upper_limit += individuals_per_objective   
            provisional_parents = parents_chromosomes[lower_limit:upper_limit]
            local_parents = br.create_population(representation,provisional_parents,length_subchromosomes,decimal_precision,vector_functions,vector_ranges,fitness_mode,fitness_options_extra)
            provisional_parents_chromosomes = getattr(st,selection_method)(local_parents,selection_options)
            selected_parents_chromosomes += provisional_parents_chromosomes 
            lower_limit = upper_limit
            how_many_individuals -= individuals_per_objective
            how_many_objectives -= 1
                
        while (selected_parents_chromosomes != []):
              chromosome_a = selected_parents_chromosomes.pop(0)
              chromosome_b = selected_parents_chromosomes.pop(0)
              [child_1,child_2] = getattr(ct,crossover_method)(chromosome_a,chromosome_b,crossover_options)        
              modified_child_1 = getattr(mt,mutation_method)(child_1,mutation_options)
              modified_child_2 = getattr(mt,mutation_method)(child_2,mutation_options)
              childrens_chromosomes.append(modified_child_1)
              childrens_chromosomes.append(modified_child_2)
        
        children =  br.create_population(representation,childrens_chromosomes,length_subchromosomes,decimal_precision,vector_functions,vector_ranges,fitness_mode,fitness_options_extra) 
          
        if elithism == True:
           for x in range (length_vector_functions):
               best_parent = global_parents.get_best_individual(x)
               position_worst_child = children.get_position_worst_individual(x)
               children.set_individual(position_worst_child,best_parent)
        
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
