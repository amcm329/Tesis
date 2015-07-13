#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

#Clase que será por ahora la parte "gráfica" del programa.

import Controller.Controller as con


def start_sequence():
    variables = "Variables.xml"
    functions = "Functions.xml"
    features = "Features.xml"
    settings = "Settings.xml"


    algorithm_class = ""
    algorithm_method = ""

    generations = 100   
    population_size = 20
    vector_functions = ["10*x+y","x*y","34*x-y"]
    vector_ variables = [['x',[-3,3]],['y',[-2,2]]]
    decimal_precision = 4
    representation_name  = "BinaryRepresentation "
    representation_class = "BinaryRepresentation"
    
    #Cambiar fitness mode.
    fitness_mode = 2
    fitness_extra_options = []

    selection_class = ""
    selection_method = ""
 #position_0 always is for selecting based in a position given
    selection_options = [-1000] 

    crossover_class = ""
    crossover_method = ""
    crossover_options = [1,0.70]

    mutation_class = ""
    mutation_method = ""
    mutation_options = [0.05]

    elithism = False
    
    options = con.load_features(features)
    selection_code = ""
    crossover_code = ""
    mutation_code = ""
    algorithm_code = ""

    """
    for option in options:
        if option[0] == 1:
           print str(option[1]) + ".- " + option[2]

    selection_code = int(raw_input("Código de selección: "))

    for option in options:
        if option[0] == 2:
           print str(option[1]) + ".- " + option[2]
        
    crossover_code = int(raw_input("Código de cruza: "))

    for option in options:
        if option[0] == 3:
           print str(option[1]) + ".- " + option[2]
        
    mutation_code = int(raw_input("Código de mutacion: "))
    
    for option in options:   
        if option[0] == 4:
           print str(option[1]) + ".- " + option[2]
        
    algorithm_code = int(raw_input("Código de algoritmo: "))


    for option in options:
        if option[0] == 1:
           if selection_code == option[1]:
              selection_class = option[3]
              selection_method = option[4]

    for option in options:
        if option[0] == 2:
           if crossover_code == option[1]:
              crossover_class = option[3]
              crossover_method = option[4]

    for option in options:
        if option[0] == 3:
           if mutation_code == option[1]:
              mutation_class = option[3]
              mutation_method = option[4]

    for option in options:
        if option[0] == 4:
           if algorithm_code == option[1]:
              algorithm_class = option[3]
              algorithm_method = option[4]


    best_guys = con.execute_algorithm(algorithm_class,algorithm_method,generations,population_size,vector_functions,vector_ranges,decimal_precision,representation,fitness_mode,fitness_extra_options,selection_class,selection_method,selection_options,crossover_class,crossover_method,crossover_options,mutation_class,mutation_method,mutation_options,elithism)

    contador = 1
    for objetivo in best_guys:
        print "Objetivo: " + str(contador)
        print objetivo
        print " "
        contador +=1
     
    """
    for option in options:
        print option


    #print con.save_settings("Mutation","Otro","aaron","Hola")
    #print con.delete_settings("Mutation","Otro","aaron","Hola")
