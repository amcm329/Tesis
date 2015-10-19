#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import random as aleatorio

def execute_selection_technique(population,selection_options):
    population_count = 0
    chromosome_set = []
    contenders_amount = selection_options["contenders_amount_probabilistic_tournament"]
    population_size = population.get_size()
    individuals = population.get_individuals()

    while population_count < population_size:
          tournament = []
          count = 0
          for x in range(contenders_amount):
              index = aleatorio.randint(0,population_size - 1)
              tournament.append(individuals[index])

          best = tournament[0]
          for contender in tournament:
              flip = aleatorio.random()
              if flip <= 0.5: 
                 best = contender
                 count+=1
          
          chromosome_set.append(best.get_complete_chromosome())
          population_count+=1

    return chromosome_set

