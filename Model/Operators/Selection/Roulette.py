#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import random as aleatorio

"""Also called fitness proportionate selection."""
def roulette(population,selection_options):
    chromosome_set = []
    total_expected_value = population.get_total_expected_value()
    #print "My_total_expected value: ",total_expected_value
    my_population = population.get_individuals()
    #print "Population: ", my_population    

    for x in range (population.get_size()):
        random_expected = aleatorio.uniform(0,total_expected_value)
        #print "Random: ", random_expected
        cumulative_sum = 0.0
        count = 0
        individual = ""
        while cumulative_sum < random_expected:
              individual = my_population[count]
              cumulative_sum += individual.get_expected_value()
              count += 1
        
      #  print "Individual: " + str(individual)
        chromosome_set.append(individual.get_complete_chromosome())

    return chromosome_set
