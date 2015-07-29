#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

def assign_proportional_fitness(population,fitness_options):
    total_fitness = [0] * population.get_length_vector_functions()
    for individual in population.get_individuals():
        for x in range (population.get_length_vector_functions()):
            #Asigning total fitness
            individual.set_fitness(x,individual.get_evaluated_function(x))
            total_fitness[x] += individual.get_fitness(x) 

    for y in range (population.get_length_vector_functions()):
        population.set_total_fitness(y,total_fitness[y])

    population.calculate_population_properties()

