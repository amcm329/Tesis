#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import Community.Community as com

#No tiene completar population porque eso le corresponde al controlador, no a esto.
#Verificar el caso de las poblaciones incompletas.
#Verificar el caso de las selecciones incompletas. 
#representation options = gray coding.

desde el tester probar existencia de la clase y el método y de hecho desde el tester sólo pedir la instancia, no el método.
selection_instance 


#Creating as much populations as number of vector_functions
def create_subpopulations(main_population):
    subpopulations = []
    how_many_individuals = main_population.get_population_size()
    how_many_objectives = main_population.get_length_vector_functions()
    lower_limit = 0
    upper_limit = 0
    for y in range (main_population.get_length_vector_functions()):
        individuals_per_objective = int(how_many_individuals/how_many_objectives)
        upper_limit += individuals_per_objective   
        provisional_parents = parents_chromosomes[lower_limit:upper_limit]
        subpopulation = com.create_population(provisional_parents)          
        subpopulations.append(subpopulation)
        lower_limit = upper_limit
        how_many_individuals -= individuals_per_objective
        how_many_objectives -= 1
      
    return subpopulations


def merge_subpopulations(subpopulations):
    chromosomes = []
    for subpopulation in subpopulations:
        for individual in subpopulation:
            chromosomes.append(individual.get_complete_chromosome())
 
    return com.create_population(chromosomes)


def vega_algorithm(generations,population_size,vector_functions,vector_variables,available_expressions,decimal_precision,representation_class,representation_options,fitness_class,fitness_method,fitness_options,selection_class,selection_method,selection_options,crossover_class,crossover_method,crossover_options,mutation_class,mutation_method,mutation_options,elithism_number): 
    final_information = [0]*length_vector_functions
    community = com.Community(population_size,vector_functions,vector_variables,available_expressions,decimal_precision,representation_class,representation_options,fitness_class,fitness_method,fitness_options,selection_class,selection_method,selection_options,crossover_class,crossover_method,crossover_options,mutation_class,mutation_method,mutation_options)           

    parents = community.init_population()

       for x in range (generations):
           result_evaluation = community.evaluate_population_functions(parents)
           result_fitness = community.assign_population_fitness(parents)
           parents.shuflle_population()
           subpopulations = create_subpopulations(parents)
           children_population = []

           for y in range (len(subpopulations)):
               subpopulation = subpopulations[i]
               subpopulation.shuffle_population()
               children = evolve_next_generation(subpopulation,y)
               com.evaluate_population_functions(children)
               com.assign_population_fitness(parents)
               com.elitism(subpopulation,children,True,"get_fitness",y,elitism_amount)
               children_population.append(children)

           #aqui falta cosechar la info
           parents =  merge_subpopulations(parents)



         

       

       
               
        #as much individuals for generation as number of functions.
        #adding the best elements for generation
        for x in range (length_vector_functions):
            best_individual = children.get_best_individual(x).get_evaluated_function(x)
            final_information[x].append(best_individual)

        #final_information.append(best_individuals_per_generation)

        parents_chromosomes = next_generation_chromosomes

   
    return final_information
