#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

#Clase que será por ahora la parte "gráfica" del programa.

import Controller.Controller as controlador
import math

def start_sequence():
    variables = "Variables.xml"
    functions = "Functions.xml"
    features = "Features.xml"
    settings = "Settings.xml"

    generations = 3
    population_size = 6
    vector_functions = ["12*(x-y)","pi**y","11*(x+y)"]
    vector_variables = [["x",[-5,7]],["y",[3,6]],["z",[-8,-2]]]
    available_expressions = {"pi":math.pi,"cos":math.cos}#,"hola":math.tan}
    decimal_precision = 4
    community_class = "Model.Community.Community"
    community_name = "Community"
    algorithm_class = "Model.MOEA.VEGA"
    algorithm_method = "vega_algorithm"
    #representation_class = "Model.ChromosomalRepresentation.BinaryRepresentation"
    representation_class = "Model.ChromosomalRepresentation.FloatPointRepresentation"
    representation_options  = [False] 
    fitness_class = "Model.Fitness.ProportionalFitness"
    fitness_method = "assign_proportional_fitness"
    fitness_options = [] #revisar por qué no dan los individuos que deben
    #selection_class = "Model.Operators.Selection.Roulette" 
    #selection_method = "roulette"
    #selection_class = "Model.Operators.Selection.StochasticUniversalSampling"
    #selection_method = "stochastic_universal_sampling"
    selection_class = "Model.Operators.Selection.ProbabilisticTournament"
    selection_method = "probabilistic_tournament"
    selection_options = [8]
    #crossover_class = "Model.Operators.Crossover.NPointsCrossover"
    #crossover_method = "n_points_crossover"
    crossover_class = "Model.Operators.Crossover.FloatPointCrossover"
    crossover_method = "float_point_crossover"
    crossover_options = [0.70,0.50]
    #mutation_class = "Model.Operators.Mutation.BinaryMutation"
    #mutation_method = "binary_mutation"
    mutation_class = "Model.Operators.Mutation.FloatPointMutation"
    mutation_method = "float_point_mutation"
    mutation_options = [0.08,decimal_precision,vector_variables]
    elitism_amount = 1

    print controlador.execute_algorithm(generations,population_size,vector_functions,vector_variables,available_expressions,decimal_precision,community_class,community_name,algorithm_class,algorithm_method,representation_class,representation_options,fitness_class,fitness_method,fitness_options,selection_class,selection_method,selection_options,crossover_class,crossover_method,crossover_options,mutation_class,mutation_method,mutation_options,elitism_amount)
 

    #print con.save_settings("Mutation","Otro","aaron","Hola")
    #print con.delete_settings("Mutation","Otro","aaron","Hola")




