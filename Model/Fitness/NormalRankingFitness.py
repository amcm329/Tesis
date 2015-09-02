#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

#Faltan las evaluated_functions

def assign_normal_ranking_fitness(population):
    total_fitness = 0.0
    #Primero se ordenan los elementos con base en la cosa esa de pareto.    
    population.sort_individuals(self,"get_pareto_dominants",False):
    y = 0
    #Luego se hace el ranking normal.
    for individual in population.get_population():
        current_fitness = y + 1.0
        individual.set_fitness(current_fitness)
        total_fitness += current_fitness
        
        y += 1

    #al final se pone el total fitness.
    population.set_total_fitness(total_fitness)
    population.calculate_population_properties() 
