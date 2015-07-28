#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

def assign_pareto_dominance_based_fitness(population,fitness_options):
    individuals = population.get_population()
    size = population.get_size_population()
    length = population.get_length_vector_functions()
    total_fitness = 0 
    for x in range (size):
        current = individuals[x]
        how_many_individuals_dominate_current = 0
        for y in range (size):
            if x != y:
               challenger = individuals[y]
               for z in range (length):
                   if not(not(challenger.get_evaluated_function(z) > current.get_evaluated_function(z)) or not(challenger.get_evaluated_function(z) >= current.get_evaluated_function(z))):
                      how_many_individuals_dominate_current +=1

        current_rank = 1 + how_many_individuals_dominate_current
        total_fitness += current_rank
        current.set_fitness(0,current_rank)


    population.set_total_fitness(0,total_fitness)
    population.calculate_population_properties()


