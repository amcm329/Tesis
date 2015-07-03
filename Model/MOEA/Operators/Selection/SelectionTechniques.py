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
         

def reward_based_selection(population):
    pass

     #shuffle elements
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



#offspring debe ser entero menor 
def stochastic_universal_sampling(population,options):
    fitness_position = options[0]
    offspring = additional_options[1]
    my_chromosome_set = []
    my_total_fitness = population.get_total_fitness(fitness_position)
    my_population = population.get_population()
    shuffle(my_population)

    distance = my_total_fitness/offspring
    start = r.uniform(0,distance)

    pointers = [(start + distance*i) for i in range(offspring)]

    for point in pointers:
        cumulative_sum = 0.0
        count = 0
        individual = ""
        while cumulative_sum < point:
              individual = my_population[count]
              cumulative_sum += individual.get_fitness(fitness_position)
              count += 1
        
        my_chromosome_set.append(individual.get_complete_chromosome())

    return my_chromosome_set


#SUS(Population, N)
#    F := total fitness of population
#    N := number of offspring to keep
#    P := distance between the pointers (F/N)
#    Start := random number between 0 and P
#    Pointers := [Start + i*P | i in [0..N-1]]
#    return RWS(Population,Pointers)

#RWS(Population, Points)
#    Keep = []
#    i := 0
#    for P in Points
#        while fitness sum of Population[1~i] < P
#            i++
#        add Population[i] to Keep
#    return Keep

    pass
    
#version con reemplazo, version sin reemplazo.
def estocastico_sobrante(population,options):
    pass

def torneo_probabilistico(population,options):
    pass

def torneo_determinista(population,options):
    pass

