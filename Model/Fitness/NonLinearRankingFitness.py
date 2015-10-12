#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

def derivate(polynome):
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
    
    derivate(polynome_1)
    while abs(value) >= epsilon:
        deriv_value=(evaluate_polynome(polynome_1,x_0))
        if derivalue == 0:
            x_0 = 0.0
            break
        
        x_0 = x_0 - (value/deriv_value)
        value=(evaluate_polynome(polynome,x_0))
       
    return x_0
            

def assign_non_linear_ranking_fitness(population,fitness_options):
    total_fitness = 0.0 
    sum_roots = 0.0
    sp = fitness_options[0] 
    population_size = population.get_size()
    #Orden ascendente
    population.sort_individuals(self,"get_pareto_dominants",False)
    
    #Creating polynome
    polynome = [sp - population_size]

    for x in range (population_size - 1,-1,-1):
        polynome.append(sp)

    solution = calculate_root(polynome,0.0,0.0000001)         

    for x in range (population_size):
        sum_roots += solution**x

    y = 0
    for individual in population.get_individuals():
        current_fitness = (population_size*(solution**y))/sum_roots
        individual.set_fitness(current_fitness)
        total_fitness += current_fitness        l
        y += 1
  
    population.set_total_fitness(total_fitness) 
    population.calculate_population_properties()
    
