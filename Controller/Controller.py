#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.


import Parser as pr
import Verifier as vr

#OK.
def load_features(features_filename):
    data = None
    try:
       data = pr.load_xml_features(features_filename)
    
    except:
       data = "ERROR"
    
    return vr.verify_load_xml_features(data)    

#OK
def save_features(features_filename,category_location,technique_name,technique_class,technique_method):
    data = load_features(features_filename)
    verifier_code =  vr.verify_write_xml_features(data,category_location,technique_name,technique_class,technique_method)
    if verifier_code == "OK": 
       pr.write_xml_features(features_filename,category_location,technique_name,technique_class,technique_method)

    return verifier_code

#OK
def delete_features(features_filename,category_location,technique_name,technique_class,technique_method):
    data = load_features(features_filename)
    verifier_code = vr.verify_delete_xml_features(data,category_location,technique_name,technique_class,technique_method)
    if verifier_code == "OK":
       pr.delete_xml_features(features_filename,category_location,technique_name,technique_class,technique_method)


    return verifier_code

#Agregar un código de error
#Este metodo tiene que pasar primero por el parser.
#poner excepciones al código
def execute_algorithm(algorithm_class,algorithm_method,generations,population_size,vector_functions,vector_variables,available_expressions,decimal_precision,representation_class,representation_options,fitness_class,fitness_method,fitness_options,selection_class,selection_method,selection_options,crossover_class,crossover_method,crossover_options,mutation_class,mutation_method,mutation_options,elithism_number):
    alg = __import__(algorithm_class, globals(), locals(), ['object'], -1) 
    return getattr(alg,algorithm_method)(generations,population_size,vector_functions,vector_variables,decimal_precision,representation_class,representation_options,fitness_class,fitness_method,fitness_options,selection_class,selection_method,selection_options,crossover_class,crossover_method,crossover_options,mutation_class,mutation_method,mutation_options,elithism_number)

