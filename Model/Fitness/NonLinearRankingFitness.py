#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

def evaluate(poly, x):
    value=0.0
    for index in range(len(poly)):
        value  = value+(x**index)*poly[index]
    return value

def Deriv(poly):
    for index in range(len(poly)):
            poly[index]*=index
    poly.pop(0)
    if len(poly) == 0:
        poly.insert(0,0.0)
    return poly

def Root(poly, x_0, epsilon):
    value = (evaluate(poly,x_0))
    poly1=[]
    for num  in poly:
            poly1.append(num)    
    Deriv(poly1)
    count = 0
    while abs(value)  >= epsilon:
        derivalue=(evaluate(poly1,x_0))
        if derivalue == 0:
            x_0 = 0
            break
        x_0 = x_0 - (value/derivalue)
        value=(evaluate(poly,x_0))
        count += 1
    return [x_0,count]
    
  def main():
    poly = [-13.39, 0.0, 17.5, 3.0, 1.0]    
    #poly=[1]
    x_0 = 0.1
    epsilon = .0001
    print computeRoot(poly, x_0, epsilon)    
            

#Orden ascendente para que pueda hacerse bien el ranking.
def assign_linear_ranking_fitness(population,fitness_options):
    total_fitness = 0 0 
    sp = fitness_options[0] 

    population.sort_individuals(self,"get_pareto_dominants",False)
    y = 0
         
    for individual in population.get_individuals():
        current_fitness = 2.0 - sp + 2.0 * (sp - 1.0) * (y/(population.get_size() - 1.0))
        individual.set_fitness(current_fitness)
        total_fitness += current_fitness        
        y += 1
  
    population.set_total_fitness(total_fitness) 
    population.calculate_population_properties()
    
