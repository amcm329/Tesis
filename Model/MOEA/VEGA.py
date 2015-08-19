#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

#No tiene completar population porque eso le corresponde al controlador, no a esto.
#Verificar el caso de las poblaciones incompletas.
#Verificar el caso de las selecciones incompletas. 
#representation options = gray coding.


#Agregar caso en que las poblaciones con los objetivos no sean pares.
#corregir el final population
#Agregar community_name
#Ver si se shufflean los tamaños de los objetivos.


#Creating as much populations as number of vector_functions
def create_subpopulations(comunidad,main_population):
    subpopulations = []
    how_many_individuals = main_population.get_size()
    how_many_objectives = main_population.get_length_vector_functions()
    complete_population = main_population.get_individuals()
    lower_limit = 0
    upper_limit = 0
    for y in range (main_population.get_length_vector_functions()):
        individuals_per_objective = int(how_many_individuals/how_many_objectives)
        #print "Individuals: ", individuals_per_objective
        upper_limit += individuals_per_objective   
        provisional_parents = complete_population[lower_limit:upper_limit]
        chromosome_set = []
        for provisional_parent in provisional_parents:
            chromosome_set.append(provisional_parent.get_complete_chromosome())

        subpopulation = comunidad.create_population(chromosome_set)          
        subpopulations.append(subpopulation)
        lower_limit = upper_limit
        how_many_individuals -= individuals_per_objective
        how_many_objectives -= 1
      
    return subpopulations


def vega_algorithm(generations,population_size,vector_functions,vector_variables,available_expressions,decimal_precision,community_instance,community_name,representation_instance,representation_options,fitness_instance,fitness_method,fitness_options,selection_instance,selection_method,selection_options,crossover_instance,crossover_method,crossover_options,mutation_instance,mutation_method,mutation_options,elitism_amount): 
    final_information = [[]]*len(vector_functions)
    comunidad = getattr(community_instance,community_name)(vector_functions,vector_variables,available_expressions,decimal_precision,representation_instance,representation_options,fitness_instance,fitness_method,fitness_options,selection_instance,selection_method,selection_options,crossover_instance,crossover_method,crossover_options,mutation_instance,mutation_method,mutation_options)
    parents = comunidad.init_population(population_size)
    #try:

    for x in range (1,generations + 1):
           print "Generation: ", x
           parents.shuffle_individuals()
           parents_subpopulations = create_subpopulations(comunidad,parents)
           children_subpopulations = []
           children_chromosomes = []

           #Shuffliing subpopulations
           for y in range (len(parents_subpopulations)):
               current_subpopulation = parents_subpopulations[y]
               comunidad.evaluate_population_functions(current_subpopulation)
               comunidad.calculate_population_pareto_dominance(current_subpopulation)
               #aquí va a haber problema con el fitness.
               comunidad.assign_population_fitness(current_subpopulation)
               final_information[y].append(comunidad.get_best_individual(current_subpopulation,y))
               selected_parents_chromosomes = comunidad.execute_selection(current_subpopulation,y)
               for parent_chromosome in selected_parents_chromosomes: 
                   children_chromosomes.append(parent_chromosome)
               
           children = comunidad.execute_crossover_and_mutation(children_chromosomes)
           parents = children

    #except:
    #      final_information = "ERROR: Class: VEGA. Method: vega_algorithm. Message: problem while executing vega algorithm agregar get message."
        
    return final_information
