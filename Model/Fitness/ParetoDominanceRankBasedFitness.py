 #!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

def assign_pareto_dominance_rank_based_fitness(population,fitness_options):
    #Primero asignar el rango
     1 + dominados

    #Ordenar ascendente con base en el rango.
    population.sort_individuals("get_pareto_dominants",False)
    
    for individual in population:
        individual.set_fitness(1 + individual.get_pareto_dominance())

        
    
    population.calculate_population_properties()


