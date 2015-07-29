#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import random as aleatorio

def float_point_mutation(chromosome,mutation_options):
    mutation_probability = mutation_options[0]
    decimal_precision = mutation_options[1]
    vector_variables = mutation_options[2]
    precision_string = "{0:." + str(decimal_precision) + "f}"
    mutated_chromosome = []
    for x in range(len(chromosome)):
        gen = chromosome[x]
        number = aleatorio.random()
             
        if number <= mutation_probability:
           current_variable =  vector_variables[x]
           variable_range = current_variable[1]
           lower_value = variable_range[0] 
           upper_value = variable_range[1]
           new_number = aleatorio.uniform(lower_value,upper_value)
           mutated_chromosome += [float(precision_string.format(new_number))] 
            
        else:
            mutated_chromosome += [gen]       
          
    return mutated_chromosome
    