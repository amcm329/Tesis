#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

def execute_moea(generations,population_size,vector_functions,vector_variables,available_expressions,decimal_precision,
                 community_instance,algorithm_options,representation_instance,representation_options,fitness_instance,fitness_options,
                 shared_fitness_instance,shared_fitness_options,selection_instance,selection_options,crossover_instance,crossover_options,
                 mutation_instance,mutation_options,elitism_amount):

    final_information = [[]]*len(vector_functions)
    comunidad = getattr(community_instance,"Community")(vector_functions,vector_variables,available_expressions,decimal_precision,
                                                        representation_instance,representation_options,fitness_instance,fitness_options,
                                                        shared_fitness_instance,shared_fitness_options,selection_instance,selection_options,
                                                        crossover_instance,crossover_options,mutation_instance,mutation_options)


    parents = comunidad.init_population(population_size)
    comunidad.evaluate_population_functions(parents)
    comunidad.calculate_population_pareto_dominance(parents)
    comunidad.assign_population_fitness(parents)

    for x in range (1,generations + 1):
        selected_parents_chromosomes = comunidad.execute_selection(parents)
        children = comunidad.execute_crossover_and_mutation(selected_parents_chromosomes)
        comunidad.evaluate_population_functions(children)
        comunidad.calculate_population_pareto_dominance(children)
        comunidad.assign_population_fitness(children)

        parents_and_children = []
        for parent in parents.get_individuals():
            parents_and_children.append(parent.get_complete_chromosome())

        for child in children.get_individuals():
            parents_and_children.append(child.get_complete_chromosome())

        #creando población de tamaño 2n
        new_population = comunidad.create_population(parents_and_children)
        comunidad.evaluate_population_functions(new_population)
        comunidad.calculate_population_pareto_dominance(new_population)
        comunidad.assign_rank_based_on_pareto_dominance(new_population)
   
        
        pareto_fronts = {}
        auxiliar_pareto_fronts = []

        #Dividiendo en frentes de pareto de acuerdo a la dominancia (dominancia 0, dominancia 1, etc)
        for individual in new_population.get_individuals():
            if pareto_fronts.has_key(individual.get_pareto_dominated()):
               pareto_fronts[individual.get_pareto_dominated()].append(individual.get_complete_chromosome()) 

            else:
               pareto_fronts[individual.get_pareto_dominated()] = []
               auxiliar_pareto_fronts.append(individual.get_pareto_dominated())
            
        print auxiliar_pareto_fronts 
        chosen = []
        sorted(auxiliar_pareto_fronts)       
        for current_front in auxiliar_pareto_fronts:
            if len (chosen) + len(pareto_fronts[current_front]) < parents.get_size():
               for individual in pareto_fronts[current_front]:
                   chosen.append(individual)

            else:
                 difference = parents.get_size() - len(chosen)
                 provisional = comunidad.create_population(pareto_fronts[current_front])
                 comunidad.evaluate_population_functions(provisional)
                 comunidad.calculate_population_pareto_dominance(provisional)
                 comunidad.assign_population_fitness(provisional)
                 comunidad.calculate_population_niche_count(provisional)
                 provisional.sort_individuals("get_niche_count",True)

                 individuals = provisional.get_individuals()
                 for x in range (difference):
                     chosen.append(individuals[x].get_complete_chromosome())


                  
        parents = comunidad.create_population(chosen)


           


