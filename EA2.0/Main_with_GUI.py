import random
import CityMap
import Initialization
import Crossover
import Mutation
import Selection
import copy
import json
import time

def main():

    western29 = "Cities/TSP_WesternSahara_29.txt"
    uruguay734 = "Cities/TSP_Uruguay_734.txt"
    canada4663 = "Cities/TSP_Canada_4663.txt"

    popsize = 2000
    mating_pool_size = 300
    tournament_size = 3
    mut_rate = 0.2
    xover_rate = 0.9
    gen_limit = 100

    advanced_Canada = {
        "description": {
            "instance_name": "none",
            "algorithm": "none",
            "city_all": 4663,
            "generation_all": gen_limit
        },
        "evolutions": [
            # nothing yet
        ]
    }

    advanced_Uruguay = {
        "description": {
            "instance_name": "none",
            "algorithm": "none",
            "city_all": 734,
            "generation_all": gen_limit
        },
        "evolutions": [
            # nothing yet
        ]
    }

    advanced_WesternSahara = {
        "description": {
            "instance_name": "none",
            "algorithm": "none",
            "city_all": 29,
            "evolution_all": 10,
            "generation_all": gen_limit,
            "generation_size": mating_pool_size
        },
        "evolutions": [
            # nothing yet
        ]
    }

    print(   json.dumps(advanced_WesternSahara)   )




    for evo in range(10):    # Experiment

        # construct a trial #
        trial = [
            [{"time_cost": 0}]
        ]

        print("trial", evo+1)



        # t = time.time()
        print("Preparing for the information...")
        c = CityMap.CityMap(western29)
        city_map = c.city_map
        print("preparation end.")

        gen = 0
        print("Initialize population...")
        init = Initialization.Population(popsize, city_map)
        init.evalPopulation()
        print("Initialization end.")

        # Evolution ########################################################################################################
        while gen < gen_limit:

            # parent selection ---------------------------------------------------------------------------------------------
            #print("parent selection...")
            parents = Selection.tournament_selection(init.population[1:], mating_pool_size, tournament_size)
            #print("parent selection end.")

            offsprings = []
            i = 0
            while len(offsprings) < mating_pool_size:    # 2 parents  ->  2 individuals
                p1 = parents[i]
                p2 = parents[i + 1]

                # crossover ------------------------------------------------------------------------------------------------
                #print("crossover...")
                if random.random() < xover_rate:
                    #off1, off2 = Crossover.COWGC(p1, p2, city_map)
                    off1, off2 = Crossover.order_crossover(p1, p2, city_map)
                else:
                    off1 = copy.copy(p1)
                    off2 = copy.copy(p2)
                #print("crossover end")

                # mutation ------------------------------------------------------------------------------------------------
                #print("Mutation...")
                if random.random() < mut_rate:
                    off1 = Mutation.WGWWGM(p1, city_map)
                    #off1 = Mutation.WGWRGM(p1, city_map)
                    #off1 = Mutation.IRGIBNNM_mutation(p1, city_map)
                    #off1 = Mutation.inversion_mutation(p1, city_map)
                if random.random() < mut_rate:
                    off2 = Mutation.WGWWGM(p2, city_map)
                    #off2 = Mutation.WGWRGM(p2, city_map)
                    #off2 = Mutation.IRGIBNNM_mutation(p2, city_map)
                    #off2 = Mutation.inversion_mutation(p2, city_map)
                #print("Mutation end")

                offsprings.append(off1)
                offsprings.append(off2)
                #print(len(offsprings))

                i += 2

            # survial selection --------------------------------------------------------------------------------------------
            #print("survival selection")
            init.population[1:] = Selection.mu_plus_lambda(init.population[1:], offsprings)
            #print("survival selection end")

            init.evalPopulation()

            print("generation:", gen, " Average length:", init.AverageLength, " Longest length: ", init.worstTour.length, " shortest length:", init.bestTour.length)


            # construct a generation #
            generation = {
                "best-individual-sequence": init.bestTour.tour,
                "best-individual-distance": init.bestTour.length,
                "worst-individual-sequence": init.worstTour.tour,
                "worst-individual-distance": init.worstTour.length,
                "average-distance": init.AverageLength,
                "individual-distances": [round(distance.length) for distance in init.population]    # distance.length for distance in init.population
            }

            trial.append(generation)

            gen += 1

        advanced_WesternSahara["evolutions"].append(trial)



    # here processing generating json file #############################################################################

    output_file = open("advanced_WesternSahara.js", "w")

    output_file.write("let advanced_WesternSahara = ")
    output_file.write(json.dumps(advanced_WesternSahara))

    output_file.close()





main()
