#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.


def create_float_point_chromosome(vector_ranges,decimal_precision):
    chromosome = []
    precision_string = "{0:." + str(decimal_precision) + "f}"
    for my_range in vector_ranges:
        lower_limit = my_range[0]
        upper_limit = my_range[1]
        number = r.uniform(lower_limit,upper_limit)
        chromosome.append(float(precision_string.format(number)))

    return chromosome


def calculate_length_subchromosomes():
    pass
