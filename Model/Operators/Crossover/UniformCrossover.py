#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import random as r

def uniform_crossover(chromosome_a,chromosome_b,additional_options):
    pmask = additional_options[0]
    chromosome_son_1 = []
    chromosome_son_2 = []
    number = -1
         
    for x in range(0,len(chromosome_a)):
        number = r.random()
        if number <= pmask:
           chromosome_son_1 += [chromosome_b[x]]
           chromosome_son_2 += [chromosome_a[x]]
                    
        else:
           chromosome_son_1 += [chromosome_a[x]]
           chromosome_son_2 += [chromosome_b[x]]
                  

    return [chromosome_son_1,chromosome_son_2]    
