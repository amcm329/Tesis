#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.


def moga_algorithm(generations,population_size,vector_functions,vector_variables,available_expressions,decimal_precision,community_instance,community_name,representation_instance,representation_options,fitness_instance,fitness_method,fitness_options,selection_instance,selection_method,selection_options,crossover_instance,crossover_method,crossover_options,mutation_instance,mutation_method,mutation_options,elitism_amount):
    comunidad = getattr(community_instance,community_name)(vector_functions,vector_variables,available_expressions,decimal_precision,representation_instance,representation_options,fitness_instance,fitness_method,fitness_options,selection_instance,selection_method,selection_options,crossover_instance,crossover_method,crossover_options,mutation_instance,mutation_method,mutation_options)
    parents = comunidad.init_population(population_size)
    comunidad.evaluate_population_functions(parents)
    #assign rank based on pareto dominance
    #Compute niche count
    #Assign linearly scaled fitness
    #Assign shared fitness
    for x in range (1, generations + 1):
        selected_parents_chromosomes = comunidad.execute(parents,position)  
  
