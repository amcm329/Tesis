#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.


def assign_scaling_fitness(population,fitness_options):
    alpha = fitness_options[0]
    beta = fitness_options[1]
    total_fitness = [0] * population.get_length_vector_functions()
    for individual in population.get_population():
        for x in range (population.get_length_vector_functions()):
              individual.set_fitness(x, alpha*individual.get_evaluated_function(x) + beta)
              total_fitness[x] += individual.get_fitness(x) 
     
    for y in range (population.get_length_vector_functions()):
        population.set_total_fitness(y,total_fitness[y])

    population.calculate_individuals_properties() 
