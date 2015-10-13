 #!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

#Menos dominados -> mayor fitness -> ultima posicion

def assign_pareto_dominance_ranking_fitness(population,fitness_options):
    total_fitness = 0.0
    position = 0
    position_dictionary = {}
    #Primero asignar el rango como fitness   
    for individual in population.get_individuals():
        individual.set_fitness(1 + individual.get_pareto_dominated())
    
    #Ordenar descendente con base en el rango (que es el fitness).
    population.sort_individuals("get_fitness",True)

    #Asignar fitness de acuerdo a una funcion lineal (y=x)
    for individual in population.get_individuals():
        if position_dictionary.has_key(individual.get_fitness()):
           position_dictionary[individual.get_fitness()].append(position)
     
        else:
             position_dictionary[individual.get_fitness()] = []

        individual.set_fitness(position + 1)
        position += 1

    #promediar los fitness con los mismos rangos
    individuals = population.get_individuals():
    for key in position_dictionary.keys():
        for positions in position_dictionary[key]:
            sume = 0.0
            total = len(positions)
            #Getting sume of fitnesses.
            for position in positions:
                sume += individual[position].get_fitness()
                 
            #Setting average of fitnesses.
            for position in positions:
                indidivual[position].set_fitness(sume/total)
                total_fitness += individual[position].get_fitness()
        

    population.set_total_fitness(total_fitness) 
    population.calculate_population_properties()
