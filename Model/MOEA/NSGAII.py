#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

def execute_moea(generations,population_size,vector_functions,vector_variables,available_expressions,decimal_precision,
                 community_instance,algorithm_options,representation_instance,representation_options,fitness_instance,fitness_options,
                 shared_fitness_instance,shared_fitness_options,selection_instance,selection_options,crossover_instance,crossover_options,
                 mutation_instance,mutation_options,elitism_amount):

    final_information = [[]]*len(vector_functions)
    comunidad = getattr(community_instance,"Community")(vector_functions,vector_variables,available_expressions,decimal_precision,
                                                        representation_instance,representation_options,fitness_instance,fitness_options,
                                                        shared_fitness_instance,shared_fitness_options,selection_instance,selection_options,
                                                        crossover_instance,crossover_options,mutation_instance,mutation_options)
