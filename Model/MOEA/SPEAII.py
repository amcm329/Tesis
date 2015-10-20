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


    population_p = comunidad.init_population(population_size)
    external_set_e = comunidad.init_population(algorithm_options["length_external_set_e_spea_ii"])

    #cleaning external_set 

    for x in range (1, generations + 1):
        print "Generation: ", x
        #Compute fitness of each individual in P and E.
        comunidad.evaluate_population_functions(population_p)
        comunidad.calculate_population_pareto_dominance(population_p)
        comunidad.assign_population_fitness(population_p)

        if x > 1:
           comunidad.evaluate_population_functions(external_set_e)
           comunidad.calculate_population_pareto_dominance(external_set_e)
           comunidad.assign_population_fitness(external_set_e)


        #Agregar primero todo lo de external set y luego todo lo de population
        external_set_e_list = []

        #añadiendo los no dominados de population_p a external_set_e_list 
        for current_individual in population_p.get_individuals():
            if current_individual.get_pareto_dominated() == 0:
               external_set_e_list.append(current_individual)

        #Añadiendo los no dominados de external_set_e a external_set_e_list
        if x > 1:
           for current_individual in external_set_e.get_individuals():
               if current_individual.get_pareto_dominated() == 0:
                  external_set_e_list.append(current_individual)
      
        #Si faltan elementos se añaden de la lista (los que estan dominados
        if len(external_set_e_list) < algorithm_options["length_external_set_e_spea_ii"]:
           difference = algorithm_options["length_external_set_e_spea_ii"] - len(external_set_e_list)
           auxiliar = 0 
           for current_individual in population_p.get_individuals():
               if current_individual.get_pareto_dominated() > 0 and auxiliar < difference:
                  external_set_e_list.append(current_individual)
                  auxiliar += 1
           print "1: "
         
        #Si despues de haber anadido todos se pasa entonces se hace truncamiento al azar hasta que sea igual al external set
        if len(external_set_e_list) > algorithm_options["length_external_set_e_spea_ii"]: 
              external_set_e_list = external_set_e_list[0:algorithm_options["length_external_set_e_spea_ii"]]
              print "2: "
        
        auxiliar_external_set_e = []
        #adding elements to external set e (aqui esta el problema)
        for element in external_set_e_list:
            auxiliar_external_set_e.append(element.get_complete_chromosome())
               
        print auxiliar_external_set_e #falta ver por que me estan dando cosas negativas
        external_set_e = comunidad.create_population(auxiliar_external_set_e)
        external_set_e.print_features()

        #Recalculating settings
        comunidad.evaluate_population_functions(external_set_e)
        comunidad.calculate_population_pareto_dominance(external_set_e)
        comunidad.assign_population_fitness(external_set_e)

        #Executing selection and mutation to the mating pool  
        selected_parents_chromosomes = comunidad.execute_selection(external_set_e)
        external_set_e_child = comunidad.execute_crossover_and_mutation(selected_parents_chromosomes)
        
        
        for y in range(external_set_e_child.get_length_vector_functions()):        
            final_information[y].append(comunidad.get_best_individual(external_set_e_child,y))

        population_p = external_set_e_child

     
    return final_information
