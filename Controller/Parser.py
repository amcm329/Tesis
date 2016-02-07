#! /usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import os
import xml.etree.ElementTree as et


def indent(element, level=0):
    i = "\n" + level*"   "
    if len(element):
        if not element.text or not element.text.strip():
            element.text = i + "   "
        if not element.tail or not element.tail.strip():
            element.tail = i
        for element in element:
            indent(element, level+1)
        if not element.tail or not element.tail.strip():
            element.tail = i
    else:
        if level and (not element.tail or not element.tail.strip()):
            element.tail = i


def load_xml_features(features_filename):
    category_options = {}
    path = os.path.dirname(__file__)
    tree = et.parse(path + "/XML/" + features_filename)
    root = tree.getroot()

    for category in root:
        category_name = category.get("name")
        division_options = {}
    
        for division in category:
            division_name = division.get("name")
            division_path = division.get("path")
            technique_options = {}

            for technique in division:
                technique_name = technique.get("name")        
                technique_class = technique.get("class")
                parameters = []

                for parameter in technique:
                    parameter_name = parameter.get("name")
                    parameter_value = parameter.get("value")
                    parameters.append({"name":parameter_name,"value":parameter_value})

                technique_options[technique_name] = {"class":technique_class,"parameter":parameters}
            
            division_options[division_name] = [division_path,technique_options]              
  
        category_options[category_name] = division_options    
  
    return category_options

#LISTO
def write_xml_features(features_filename,category_name,division_name,category_path,technique_name,technique_class):
    path = os.path.dirname(__file__)
    tree = et.parse(path + "/" + features_filename)
    root = tree.getroot()
    category = root.find(category_name)
    division = category.find(division_name) 
    new_child = et.SubElement(division, "Technique name=\"" + technique_name + "\" class=\"" + technique_class + "\"")
    indent(root)
    tree.write(path + "/" + features_filename)
   

#En verifier verificar que el dato este antes de borrarlo, se usa con un load_settings y luego check.
def delete_xml_features(features_filename,category_name,division_name,category_path,technique_name,technique_class):
    path = os.path.dirname(__file__)
    tree = et.parse(path + "/" + features_filename)
    root = tree.getroot()
    category = root.find(category_name)
    division = category.find(division_name)

    for technique in division:
        if technique.get('name') == technique_name and technique.get('class') == technique_class: 
           category.remove(technique)
    
    indent(root)
    tree.write(path + "/" + features_filename)
