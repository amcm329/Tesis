#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.


"""Método que crea un cromosoma binario."""
def create_binary_chromosome(length_chromosome):
    chromosome = []
            
    for x in range(0,length_chromosome):
        number = r.randint(0,1)
        chromosome.append(number)
         
    return chromosome



"""Método que calcula la longitud de todos los subcromosomas. Para ello
se hace uso del vector de rangos, así como de la precisión decimal."""
#Binary use only
def calculate_length_subchromosomes(vector_ranges,decimal_precision):
    true_decimal_precision = 10**decimal_precision
    lower_limit = -1
    upper_limit = -1
    amount = -1
    how_many_bits_around = -1
    how_many_bits_real = -1
    length_subchromosomes = []
    #contador = 0
    for my_range in vector_ranges:
        #print "Hola",contador," ",my_range
        #contador+=1
        lower_limit = my_range[0]
        upper_limit = my_range[1]
        #print "Lower: ",lower_limit
        #print "Upper: ",upper_limit 
        amount = (upper_limit - lower_limit)*true_decimal_precision
        #print "Amount: ",amount
        how_many_bits_around = m.log(amount,2) 
        #print "Mas o menos: ",how_many_bits_around
        how_many_bits_real = int(m.ceil(how_many_bits_around))
        #print "Real: ",how_many_bits_real
        length_subchromosomes.append(how_many_bits_real)
        #print "----------------------------------------------"

    return length_subchromosomes

