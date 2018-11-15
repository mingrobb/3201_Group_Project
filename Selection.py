import random
import Initialization
import CityMap

def tournament_selection(population, mating_pool_size, tournament_size):
    """

    :return:
    """
    selected_to_mate = []
    mating_pool = random.sample(population, mating_pool_size)
    while len(selected_to_mate) < mating_pool_size:
        tour_pool = random.sample(mating_pool, tournament_size)
        best_fitness = -1
        best = None
        for i in tour_pool:
            fitness = i[1]
            if fitness > best_fitness:
                best_fitness = fitness
                best = i
        selected_to_mate.append(best)

    return selected_to_mate


def mu_plus_lambda(cur_pop, offsprings):
    """

    :param cur_pop:
    :param offsprings:
    :return:
    """
    length = len(cur_pop)
    temp_pop = cur_pop + offsprings

    temp_pop = sorted(temp_pop, key=lambda item:item[1])
    pop = []
    for i in range(length):
        pop.append(temp_pop[i])

    return pop



########################
######            ######
######    Test    ######
######            ######
########################
"""
file  = "Cities/TSP_WesternSahara_29.txt"
c = CityMap.CityMap(file)
city_map = c.city_map
Object = Initialization.Population(30, city_map)
pop = Object.population
s = tournament_selection(pop, 10, 3)
print(len(s))
for i in s:
    print(i[0].tour, i[1])
"""