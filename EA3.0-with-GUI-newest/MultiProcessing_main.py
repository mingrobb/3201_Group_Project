import random
import CityMap
import Initialization
import Crossover
import Mutation
import Selection
import copy
import multiprocessing
import time

class EAProcess(multiprocessing.Process):
    def __init__(self, q, parents, city_map, mating_pool_size, mut_rate, xover_rate):
        multiprocessing.Process.__init__(self)
        self.city_map = city_map
        self.parents = parents
        self.mating_pool_size = mating_pool_size
        self.mut_rate = mut_rate
        self.xover_rate = xover_rate
        #self.sub_offspring = sub_offspring
        #self.pro_num =pro_num
        #self.return_dict = return_dict


    def run(self):
        """

        :return:
        """
        offspring = []
        i = 0
        while len(offspring) < self.mating_pool_size:  # 2 parents  ->  2 individuals
            p1 = self.parents[i]
            p2 = self.parents[i + 1]

            # crossover ################################################################################################
            # print("crossover...")
            if random.random() < self.xover_rate:
                # off1, off2 = Crossover.COWGC(p1, p2, city_map)
                off1 = Crossover.order_crossover(p1, p2, city_map)
                off2 = Crossover.order_crossover(p1, p2, city_map)
            else:
                off1 = copy.copy(p1)
                off2 = copy.copy(p2)
            # print("crossover end")

            # mutation #################################################################################################
            # print("Mutation...")
            if random.random() < self.mut_rate:
                off1 = Mutation.WGWWGM(p1, city_map)
                # off1 = Mutation.IRGIBNNM_mutation(p1, city_map)
                # off1 = Mutation.inversion_mutation(p1, city_map)
            if random.random() < self.mut_rate:
                off2 = Mutation.WGWWGM(p2, city_map)
                # off2 = Mutation.IRGIBNNM_mutation(p2, city_map)
                # off2 = Mutation.inversion_mutation(p2, city_map)
            # print("Mutation end")

            offspring.append(off1)
            offspring.append(off2)
            # print(len(offsprings))

            i += 2
        q.put(offspring)
        print('end')



if __name__ == '__main__':

    western29 = "Cities/TSP_WesternSahara_29.txt"
    uruguay734 = "Cities/TSP_Uruguay_734.txt"
    canada4663 = "Cities/TSP_Canada_4663.txt"

    popsize = 2000
    mating_pool_size = 1200
    tournament_size = 3
    mut_rate = 0.2
    xover_rate = 0.9
    gen_limit = 500

    print("Preparing for the information...")
    c = CityMap.CityMap(western29)
    city_map = c.city_map
    print("preparation end.")

    gen = 0
    print("Initialize population...")
    init = Initialization.Population(popsize, city_map)
    init.evalPopulation()
    print("Initialization end.")

    while gen < gen_limit:

        #parent selection
        #print("parent selection...")
        parents = Selection.tournament_selection(init.population[1:], mating_pool_size, tournament_size)
        #print("parent selection end.")

        CPU_num = multiprocessing.cpu_count()
        sub_mating_pool_size = int(mating_pool_size/CPU_num)

        q = multiprocessing.Queue()

        pro1 = EAProcess(q, parents, city_map, sub_mating_pool_size, mut_rate, xover_rate)
        pro2 = EAProcess(q, parents, city_map, sub_mating_pool_size, mut_rate, xover_rate)
        pro3 = EAProcess(q, parents, city_map, sub_mating_pool_size, mut_rate, xover_rate)
        pro4 = EAProcess(q, parents, city_map, sub_mating_pool_size, mut_rate, xover_rate)

        pro1.daemon = True
        pro2.daemon = True
        pro3.daemon = True
        pro4.daemon = True

        pro1.start()
        pro2.start()
        pro3.start()
        pro4.start()

        sub1 = q.get()
        sub2 = q.get()
        sub3 = q.get()
        sub4 = q.get()

        pro1.join()
        pro2.join()
        pro3.join()
        pro4.join()

        pro1.terminate()
        pro2.terminate()
        pro3.terminate()
        pro4.terminate()

        offsprings = sub1+sub2+sub3+sub4

        # survival selection ############################################################################################
        #print("survival selection")
        init.population[1:] = Selection.mu_plus_lambda(init.population[1:], offsprings)
        #print("survival selection end")

        init.evalPopulation()

        print("generation:", gen, " Average length:", init.AverageLength, " Longest length: ", init.worstTour.length, " shortest length:", init.bestTour.length)


        gen += 1









