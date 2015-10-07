#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import random as aleatorio

def real_crossover(chromosome_a,chromosome_b,crossover_options):
    crossover_probability = crossover_options[0]
    crossover_flip = crossover_options[1]
    chromosome_child_1 = []
    chromosome_child_2 = []
    number = aleatorio.random()    

    if number <= crossover_probability:
       for x in range(len(chromosome_a)):
           flip = aleatorio.random()
           if flip <= crossover_flip:
                   chromosome_child_1 += chromosome_a[x]
                   chromosome_child_2 += chromosome_b[x]

           else:
               chromosome_child_1 += chromosome_b[x]
               chromosome_child_2 += chromosome_a[x]
          
    else:
         chromosome_child_1 = chromosome_a
         chromosome_child_2 = chromosome_b      
 
    return [chromosome_child_1,chromosme_child_2]
   

