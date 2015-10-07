#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

def deriv(polynome):
    for index in range(len(polynome)):
            polynome[index]*=index
    
    polynome.pop(0)
    if len(polynome) == 0:
        polynome.insert(0,0.0)
    

def evaluate_polynome(polynome,x):
    value = 0.0
    for index in range(len(polynome)):
        value = value+(x**index)*polynome[index]
  
    return value


def calculate_root(polynome,x_0,epsilon):
    value = (evaluate_polynome(polynome,x_0))
    polynome_1=[]
    for number  in polynome:
            polynome_1.append(number)    
    
    deriv(polynome_1)
    while abs(value) >= epsilon:
        derivalue=(evaluate_polynome(polynome_1,x_0))
        if derivalue == 0:
            x_0 = 0.0
            break
        
        x_0 = x_0 - (value/derivalue)
        value=(evaluate_polynome(polynome,x_0))
       
    return x_0
            

#Orden ascendente para que pueda hacerse bien el ranking.
def assign_non_linear_ranking_fitness(population,fitness_options):
    total_fitness = 0 0 
    sp = fitness_options[0] 
    population.sort_individuals(self,"get_pareto_dominants",False)

    polynome = [sp*population.get_length()]

    for x in range (,-1)
    

    solution = calculate_root(polynome,0.0,0.0000001)         

    for individual in population.get_individuals():
        current_fitness = 
        individual.set_fitness(current_fitness)
        total_fitness += current_fitness        
        y += 1
  
    population.set_total_fitness(total_fitness) 
    population.calculate_population_properties()
    
