import random

import CityMap
import Initialization
import Crossover
import Mutation
import Selection
import copy

def main():

    western29 = "Cities/TSP_WesternSahara_29.txt"
    uruguay734 = "Cities/TSP_Uruguay_734.txt"
    canada4663 = "Cities/TSP_Canada_4663.txt"

    popsize = 100
    mating_pool_size = 10
    tournament_size = 3
    mut_rate = 0.1
    xover_rate = 0.9
    gen_limit = 600

    print("Preparing information...")
    c = CityMap.CityMap(western29)
    city_map = c.city_map

    gen = 0
    init = Initialization.Population(popsize, city_map)
    population = init.population

    #EA algorithm
    while gen < gen_limit:

        #parent selection
        parents = Selection.tournament_selection(population, mating_pool_size, tournament_size)

        offsprings = []
        i = 0
        while len(offsprings) < mating_pool_size:
            p1 = parents[i][0]
            p2 = parents[i + 1][0]

            #crossover
            if random.random() < xover_rate:
                off1, off2 = Crossover.COWGC(p1, p2, city_map)
            else:
                off1 = copy.copy(p1)
                off2 = copy.copy(p2)

            #mutation
            if random.random() < mut_rate:
                off1 = Mutation.WGWWGM(p1, city_map)
            if random.random() < mut_rate:
                off2 = Mutation.WGWWGM(p2, city_map)

            offsprings.append([off1, off1.fitness])
            offsprings.append([off2, off2.fitness])
            i += 2

        #survial selection
        population = Selection.mu_plus_lambda(population, offsprings)
        best_fitness = population[0][1]
        best_tour = population[0][0].tour
        for i in population:
            if i[1] < best_fitness:
                best_fitness = i[1]
                best_tour = i.tour
        print("generation: ", gen, ": best fitness: ", best_fitness)

        gen += 1


main()