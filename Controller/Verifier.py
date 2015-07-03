#! /usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.


def verify_load_data_xml(data):
    verified_data = "ERROR. Class: Parser. Method: load_data_xml. Message: Problem while reading xml"
    if data != "ERROR":
       verified_data = data 

    return verified_data

#options.append((category_id,technique_id,category_name,technique_name,technique_class,technique_method))
def verify_write_data_xml(data,category_name,technique_name,technique_class,technique_method):
    verifier_code = "OK"

    #Primero se verifica que la categoria exista.
    if category_name in ["Fitness","Selection","Crossover","Mutation","MOEA"]:
       for element in data:
           #Se verifica que la t
           if technique_name == element[3] and technique_class == element[4] and technique_method == element[5]:
              verifier_code = "ERROR. Class: Parser. Method: write_data_xml. Message: Technique already exists"              
               
    else:
        verifier_code = "ERROR. Class: Parser. Method: write_data_xml. Message: Category not found"
    
    return verifier_code
    

def verify_delete_data_xml(data,category_name,technique_name,technique_class,technique_method):
    verifier_code = "ERROR. Class: Parser. Method: delete_data_xml. Message: Technique doesn't exist"
    for element in data:
         #Se verifica que la tecnica exista antes de ser eliminada.
         if technique_name == element[3] and technique_class == element[4] and technique_method == element[5]:
            verifier_code = "OK"              
               
    return verifier_code

def verify_basic_algorithm_parameters():
    pass


