#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.


def calculate_length_subchromosomes(calculation_options):
    vector_ranges = calculation_options[0]
    return [1]*len(vector_ranges)


def create_chromosome(chromosome_options):
    vector_ranges = chromosome_options[0]
    decimal_precision = chromosome_options[1]
    precision_string = "{0:." + str(decimal_precision) + "f}"
    chromosome = []
    for my_range in vector_ranges:
        lower_limit = my_range[0]
        upper_limit = my_range[1]
        number = r.uniform(lower_limit,upper_limit)
        chromosome.append(float(precision_string.format(number)))

    return chromosome

