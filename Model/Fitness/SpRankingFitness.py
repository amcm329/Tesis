#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

def assign_sp_ranking_fitness(population,fitness_options):
    total_fitness = [0] * population.get_length_vector_functions()
    sp = fitness_options[0] 
    for x in range (population.get_length_vector_functions()):
          population.get_population().sort(key=lambda individual: individual.evaluated_functions[x])
          y = 0
          for individual in population.get_individuals():
                individual.set_fitness(x,2.0 - sp + 2.0 * (sp - 1.0) * (y/(population.get_size() - 1.0)))
                total_fitness[x] += individual.get_fitness(x)
                y += 1
  
    for z in range (population.get_length_vector_functions()):
          population.set_total_fitness(z,total_fitness[z]) 

    population.calculate_population_properties()
    
