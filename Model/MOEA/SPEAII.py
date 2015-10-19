#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import sys

def execute_moea(generations,population_size,vector_functions,vector_variables,available_expressions,decimal_precision,community_instance,
                 representation_instance,representation_options,fitness_instance,fitness_options,shared_fitness_instance,shared_fitness_options,
                 selection_instance,selection_options,crossover_instance,crossover_options,mutation_instance,mutation_options,elitism_amount):
    final_information = [[]]*len(vector_functions)
    comunidad = getattr(community_instance,"Community")(vector_functions,vector_variables,available_expressions,decimal_precision,
                                                        representation_instance,representation_options,fitness_instance,fitness_options,
                                                        shared_fitness_instance,shared_fitness_options,selection_instance,selection_options,
                                                        crossover_instance,crossover_options,mutation_instance,mutation_options)


    population_p = comunidad.init_population(population_size)
    external_set_e = comunidad.init_population(population_size)

    for x in range (1, generations + 1):
        print "Generation: ", x
        #Compute fitness of each individual in P and E.
        comunidad.evaluate_population_functions(population_p)
        comunidad.calculate_population_pareto_dominance(population_p)
        comunidad.assign_population_fitness(population_p)

        comunidad.evaluate_population_functions(external_set_e)
        comunidad.calculate_population_pareto_dominance(external_set_e)
        comunidad.assign_population_fitness(external_set_e)


        #Agregar primero todo lo de external set y luego todo lo de population
        external_set_e_list = 

        #añadiendo los no dominados (todos) 
        position = 0
        for individual in population_p.get_invididuals():
            if individual.get_pareto_dominated() == 0:
               external_set_e.add_individual(position,individual.get_complete_chromosome())
               position += 1

        #Si faltan elementos se añaden de la lista (los que estan dominados
        

        #Si despues de haber anadido todos se pasa entonces se eliminan al azar hasta que sea igual al external set
        while len(external_set_elist) > population_size:
              external_set_e_list

        auxiliar_external_set_e = comunidad.init_population(population_size)
        
        for element 

        external_set_e = auxiliar_external_e

        
        selected_parents_chromosomes = comunidad.execute_selection(external_set_e)
        external_set_e_child = comunidad.execute_crossover_and_mutation(selected_parents_chromosomes)
        
        for y in range(parents.get_length_vector_functions()):        
            final_information[y].append(comunidad.get_best_individual(children,y))

        population_p = external_set_e_child

     
    return final_information
