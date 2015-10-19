#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

def calculate_distance(individual_i,individual_j,shared_fitness_options):
    sum_squared = 0.0
    for position in range(len(individual_i.get_vector_functions())):
       sum_squared += (individual_i.get_evaluated_function(position) - individual_j.get_evaluated_function(position))**2

    return sum_squared**(1.0/2.0)

    
