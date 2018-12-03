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

    popsize = 20000
    mating_pool_size = 16000
    tournament_size = 10
    mut_rate = 0.2
    xover_rate = 0.9
    gen_limit = 1000


    # choose the instance you are using ################################################################################
    instance_name = "Uruguay"
    evolution_all = 1


    source = None
    city_all = 0

    if instance_name == "WesternSahara" :
        city_all = 29
        source = western29
    if instance_name == "Uruguay" :
        city_all = 734
        source = uruguay734
    if instance_name == "Canada" :
        city_all = 4663
        source = canada4663

    experiment = {
        "description": {
            "instance_name": instance_name,
            "algorithm": "advanced",
            "city_all": city_all,
            "evolution_all": evolution_all,
            "generation_all": gen_limit,
            "generation_size": popsize
        },
        "evolutions": [
            # nothing yet
        ]
    }

    print(   json.dumps(experiment)   )




    for evo in range(evolution_all):    # Experiment

        # construct a trial #
        trial = [
            {"time_cost": 0}
        ]

        print("trial", evo+1)

        start_time = time.time()


        print("Preparing for the information...")
        c = CityMap.CityMap(source)
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

            trial[0]["time_cost"] = time.time() - start_time

        experiment["evolutions"].append(trial)



    # here processing generating json file #############################################################################

    output_file = None
    variable_declaration = "none"

    if instance_name == "WesternSahara" :
        output_file = open("advanced_WesternSahara.js", "w")
        variable_declaration = "let advanced_WesternSahara = "
    if instance_name == "Uruguay" :
        output_file = open("advanced_Uruguay.js", "w")
        variable_declaration = "let advanced_Uruguay = "
    if instance_name == "Canada" :
        output_file = open("advanced_Canada.js", "w")
        variable_declaration = "let advanced_Canada = "

    output_file.write(variable_declaration)
    output_file.write(json.dumps(experiment))

    output_file.close()





main()
