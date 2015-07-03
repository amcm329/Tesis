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


def load_data_xml(document_name):
    category_id = 1
    options = []
    path = os.path.dirname(__file__)
    tree = et.parse(path + "/" + document_name)
    root = tree.getroot()

    for category in root:
        category_location = category.get('location')
        technique_id = 1

        for technique in category:
            technique_name = technique.get('name')        
            technique_class = technique.get('class')
            technique_method = technique.get('method')
            options.append((category_id,technique_id,category_location,technique_name,technique_class,technique_method))
            
            technique_id += 1
                
        category_id += 1
    
    return options

#LISTO
def write_data_xml(document_name,category_location,technique_name,technique_class,technique_method):
    path = os.path.dirname(__file__)
    tree = et.parse(path + "/" + document_name)
    root = tree.getroot()
    category = root.find(category_location) 
    new_child = et.SubElement(category, "Technique name=\"" + technique_name + "\" class=\"" + technique_class + "\" method=\"" + technique_method + "\"")
    indent(root)
    tree.write(path + "/" + document_name)
   

#En verifier verificar que el dato este antes de borrarlo, se usa con un load_settings y luego check.
def delete_data_xml(document_name,category_location,technique_name,technique_class,technique_method):
    path = os.path.dirname(__file__)
    tree = et.parse(path + "/" + document_name)
    root = tree.getroot()
    category = root.find(category_location)

    for technique in category:
        if technique.get('name') == technique_name and technique.get('class') == technique_class and technique.get('method') == technique_method: 
           category.remove(technique)
    
    indent(root)
    tree.write(path + "/" + document_name)
   
   