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
def execute_algorithm(generations,population_size,vector_functions,vector_variables,available_expressions,decimal_precision,community_class,algorithm_class,algorithm_method,representation_class,representation_options,fitness_class,fitness_method,fitness_options,selection_class,selection_method,selection_options,crossover_class,crossover_method,crossover_options,mutation_class,mutation_method,mutation_options,elitism_amount):
    result_instances = vr.verify_algorithm_settings(generations,population_size,decimal_precision,community_class,algorithm_class,representation_class,fitness_class,selection_class,crossover_class,mutation_class,elitism_amount)
    results = []

    if "ERROR" in result_instances:
        for element in algorithm_instances: 
            if "ERROR" not in element:
                result_instances.remove(perro)

        results = result_instances
   
    else:
        community_instance = result_instances[0]
        algorithm_instance = result_instances[1]
        representation_instance = result_instances[2]
        fitness_instance = result_instances[3]
        selection_instance = result_instances[4]
        crossover_instance = result_instances[5]
        mutation_instance = result_instances[6]
        results = getattr(algorithm_instance,algorithm_method)(generations,population_size,vector_functions,vector_variables,available_expressions,decimal_precision,community_instance,representation_instance,representation_options,fitness_instance,fitness_method,fitness_options,selection_instance,selection_method,selection_options,crossover_instance,crossover_method,crossover_options,mutation_instance,mutation_method,mutation_options,elitism_amount)
                
    return results


