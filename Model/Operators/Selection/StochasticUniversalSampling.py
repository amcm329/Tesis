#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import random as aleatorio


#offspring debe ser entero menor 
def stochastic_universal_sampling(population,position,options):
    chromosome_set = []
    cumulative_sum = 0
    population_selected = 0
    population_count = 0
    population_size = population.get_population_size() 
    individuals = population.get_population()
    ptr = aleatorio.random()
    
    

    while population_selected < population_size:
          #print "El elegido: ", population_count
          individual = individuals[population_count % population_size]
          cumulative_sum += individual.get_expected_value(position)
          while cumulative_sum > ptr and population_selected < population_size:
                print "           Entró: ", population_count
                chromosome_set.append(individual.get_complete_chromosome())
                population_selected += 1
                ptr += 1  
          
          population_count += 1
          #print "1 mas"
     
    print "Len: ", len(chromosome_set)
    return chromosome_set


