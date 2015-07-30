

def calculate_shared_fitness(individual_a,individual_b,shared_fitness_options):
    chromosome_a = individual_a.get_complete_chromosome()
    chromosome_b = individual_b.get_complete_chromosomse()
    hamming_distance = 0

    for x in range (len(chromosome_a)):
        gen_a = chromosome_a[x]
        gen_b = chromosome_b[x]
        if gen_a != gen_b:
           hamming_distance += 1


    return hamming_distance
     
