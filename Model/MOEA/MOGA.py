#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.


def execute_moea(generations,population_size,vector_functions,vector_variables,available_expressions,decimal_precision,community_instance,
                 representation_instance,representation_options,fitness_instance,fitness_options,shared_fitness_instance,shared_fitness_options,
                 selection_instance,selection_options,crossover_instance,crossover_options,mutation_instance,mutation_options,elitism_amount):
    final_information = [[]]*len(vector_functions)
    comunidad = getattr(community_instance,"Community")(vector_functions,vector_variables,available_expressions,decimal_precision,
                                                        representation_instance,representation_options,fitness_instance,fitness_options,
                                                        shared_fitness_instance,shared_fitness_options,selection_instance,selection_options,
                                                        crossover_instance,crossover_options,mutation_instance,mutation_options)

    parents = comunidad.init_population(population_size)

    #evaluate objective functions
    comunidad.evaluate_population_functions(parents)

    #extra step
    comunidad.calculate_population_pareto_dominance(parents)

    #assign rank based on pareto dominance
    comunidad.assign_rank_based_on_pareto_dominance(parents)
               
    #Compute niche count
    comunidad.calculate_population_niche_count(parents)
 
    #Assign linearly scaled fitness
    comunidad.assign_population_fitness(parents)

 
    #Assign shared fitness
    for x in range (1, generations + 1):
        selected_parents_chromosomes = comunidad.execute(parents,position)  
  
