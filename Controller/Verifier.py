#! /usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

#para el elitismo
#if elitism_amount > parents.get_population_size():
#             code = "ERROR. Class: Community. Method: elitism. Message: Elitism amount greater than number of individuals in current population" 
         

def verify_load_xml_features(data):
    verified_data = "ERROR. Class: Parser. Method: load_data_xml. Message: Problem while reading xml"
    if data != "ERROR":
       verified_data = data 

    return verified_data

#options.append((category_id,technique_id,category_name,technique_name,technique_class,technique_method))
def verify_write_xml_features(data,category_name,technique_name,technique_class,technique_method):
    verifier_code = "OK"

    #Primero se verifica que la categoria exista.
    if category_name in ["Representation","Fitness","SharingFunction","Selection","Crossover","Mutation","MOEA"]:
       for element in data:
           #Se verifica que la t
           if technique_name == element[3] and technique_class == element[4]:
              verifier_code = "ERROR. Class: Parser. Method: write_data_xml. Message: Technique already exists"              
               
    else:
        verifier_code = "ERROR. Class: Parser. Method: write_data_xml. Message: Category not found"
    
    return verifier_code
    

def verify_delete_xml_features(data,category_name,technique_name,technique_class,technique_method):
    verifier_code = "ERROR. Class: Parser. Method: delete_data_xml. Message: Technique doesn't exist"
    for element in data:
         #Se verifica que la tecnica exista antes de ser eliminada.
         if technique_name == element[3] and technique_class == element[4]:
            verifier_code = "OK"              
               
    return verifier_code


def verify_community_instance(community_class):
    #algorithm_instance = ""
    #try:
        community_instance = __import__(community_class, globals(), locals(), ['object'], -1) 
     
    #except:
    #    algorithm_instance = "ERROR: Class: Verifier. Method: verify_algorithm_insance. Message: Algorithm not found"

        return community_instance

def verify_algorithm_instance(algorithm_class):
    #algorithm_instance = ""
    #try:
        algorithm_instance = __import__(algorithm_class, globals(), locals(), ['object'], -1) 
     
    #except:
    #    algorithm_instance = "ERROR: Class: Verifier. Method: verify_algorithm_insance. Message: Algorithm not found"

        return algorithm_instance


def verify_representation_instance(representation_class):
    representation_instance = ""
    try:
        representation_instance = __import__(representation_class, globals(), locals(), ['object'], -1) 
     
    except:
        representation_instance = "ERROR: Class: Verifier. Method: verify_representation_instance. Message: Representation not found"

    return representation_instance
 

def verify_fitness_instance(fitness_class):
    print "La clase:-",fitness_class,"-"
    fitness_instance = ""
    #try:
    fitness_instance = __import__(fitness_class, globals(), locals(), ['object'], -1) 
     
    #except:
    #     fitness_instance = "ERROR: Class: Verifier. Method: verify_fitness_instance. Message: Fitness not found"
  
    print fitness_instance
    return fitness_instance
 

def verify_shared_fitness_instance(shared_fitness_class):
    shared_fitness_instance = ""
    try:
        shared_fitness_instance = __import__(shared_fitness_class, globals(), locals(), ['object'], -1) 
     
    except:
        shared_fitness_instance = "ERROR: Class: Verifier. Method: shared_verify_fitness_instance. Message: Shared fitness not found"

    return shared_fitness_instance


def verify_selection_instance(selection_class):
    selection_instance = ""
    try:
        selection_instance = __import__(selection_class, globals(), locals(), ['object'], -1) 
     
    except:
        selection_instance = "ERROR: Class: Verifier. Method: verify_selection_instance. Message: Selection not found"

    return selection_instance
 

def verify_crossover_instance(crossover_class):
    crossover_instance = ""
    try:
        crossover_instance = __import__(crossover_class, globals(), locals(), ['object'], -1) 
     
    except:
        crossover_instance = "ERROR: Class: Verifier. Method: verify_crossover_instance. Message: Crossover not found"

    return crossover_instance
 

def verify_mutation_instance(mutation_class):
    mutation_instance = ""
    try:
        mutation_instance = __import__(mutation_class, globals(), locals(), ['object'], -1) 
     
    except:
        mutation_instance = "ERROR: Class: Verifier. Method: verify_mutation_instance. Message: Mutation not found"

    return mutation_instance
 
#Verificar el sp y los demas valores
#verificar las de cruza y mutacion y los valores extras.
def verify_algorithm_settings(generations,population_size,decimal_precision,community_class,algorithm_class,representation_class,
                              fitness_class,shared_fitness_class,selection_class,crossover_class,mutation_class,elitism_amount):
      results = []

      if generations < 1:
         results.append("ERROR: Class: Verifier. Method: verify_algorithm_settings. Message: Invalid number of generations")              
      
      if population_size < 2:  
         results.append("ERROR: Class: Verifier. Method: verify_algorithm_settings. Message: Invalid population size")

      if decimal_precision < 0:
         results.append("ERROR: Class: Verifier. Method: verify_algorithm_settings. Message: Invalid decimal precision")

      if elitism_amount < 0:
         results.append("ERROR: Class: Verifier. Method: verify_algorithm_settings. Message: Invalid elitism amount")

      if elitism_amount > population_size:
         results.append("ERROR: Class: Verifier. Method: verify_algorithm_settings. Message: Elitism amount greater than population_size")
      

      results.append(verify_community_instance(community_class))
      results.append(verify_algorithm_instance(algorithm_class))
      results.append(verify_representation_instance(representation_class))
      results.append(verify_fitness_instance(fitness_class))
      results.append(verify_shared_fitness_instance(shared_fitness_class))
      results.append(verify_selection_instance(selection_class))
      results.append(verify_crossover_instance(crossover_class))
      results.append(verify_mutation_instance(mutation_class))
      
      return results








