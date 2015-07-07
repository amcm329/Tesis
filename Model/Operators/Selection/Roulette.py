#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import random as r

def shuffle(my_list):
    for i in range (len(my_list)-1,1,-1):
        j = r.randint(0,1)
        provisional = my_list[j]
        my_list[j] = my_list[i]
        my_list[i] = provisional


"""Also called fitness proportionate selection."""
def roulette(population,options):
    expected_value_position = options[0]
    my_chromosome_set = []
    my_total_expected_value = population.get_total_expected_value(expected_value_position)
    my_population = population.get_population()
    shuffle(my_population)

    for x in range (population.get_population_size()):
        random_expected = r.uniform(0,my_total_expected_value)
        cumulative_sum = 0.0
        count = 0
        individual = ""
        while cumulative_sum < random_expected:
              individual = my_population[count]
              cumulative_sum += individual.get_expected_value(expected_value_position)
              count += 1
        
        my_chromosome_set.append(individual.get_complete_chromosome())

    return my_chromosome_set
