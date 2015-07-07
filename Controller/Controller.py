#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.


import Parser as pr
import Verifier as vr

#OK.
def load_settings():
    data = None
    try:
       data = pr.load_data_xml("Settings.xml")
    
    except:
       data = "ERROR"
    
    return vr.verify_load_data_xml(data)    

#OK
def save_settings(category_location,technique_name,technique_class,technique_method):
    data = load_settings()
    verifier_code =  vr.verify_write_data_xml(data,category_location,technique_name,technique_class,technique_method)
    if verifier_code == "OK": 
       pr.write_data_xml("Settings.xml",category_location,technique_name,technique_class,technique_method)

    return verifier_code

#OK
def delete_settings(category_location,technique_name,technique_class,technique_method):
    data = load_settings()
    verifier_code = vr.verify_delete_data_xml(data,category_location,technique_name,technique_class,technique_method)
    if verifier_code == "OK":
       pr.delete_data_xml("Settings.xml",category_location,technique_name,technique_class,technique_method)


    return verifier_code

#Agregar un código de error
#Este metodo tiene que pasar primero por el parser.
#poner excepciones al código
def execute_algorithm(algorithm_class,algorithm_method,generations,population_size,vector_functions,vector_ranges,decimal_precision,representation,fitness_class,fitness_method,fitness_options,selection_class,selection_method,selection_options,crossover_class,crossover_method,crossover_options,mutation_class,mutation_method,mutation_options,elithism_number):
    alg = __import__(algorithm_class, globals(), locals(), ['object'], -1) 
    return getattr(alg,algorithm_method)(generations,population_size,vector_functions,vector_ranges,decimal_precision,representation,fitness_class,fitness_method,fitness_options,selection_class,selection_method,selection_options,crossover_class,crossover_method,crossover_options,mutation_class,mutation_method,mutation_options,elithism_number)

