import random

def tournament_selection(population, mating_pool_size, tournament_size):
    """
    Tournament selection
    :param population: A list of tour objects
    :param mating_pool_size: mating pool size
    :param tournament_size: tournament size
    :return: individuals that selected into the mating pool
    """
    selected_to_mate = []
    mating_pool = random.sample(population, mating_pool_size)
    while len(selected_to_mate) < mating_pool_size:
        tour_pool = random.sample(mating_pool, tournament_size)
        best_fitness = -1
        best = tour_pool[0]
        shortest  = tour_pool[0].length
        for i in tour_pool:
            if i.length < shortest:
                shortest = i.length
                best = i
        selected_to_mate.append(best)
    return selected_to_mate

def MPS(population, mating_pool_size):
    fitness = []
    selected_to_mate = []
    for i in range(len(population)):
        fitness.append(population[i].length)
    fit_sum = sum(fitness)
    cumul_prop = []
    cumul_prop.append(fitness[0]/fit_sum)
    for i in range (1, len(fitness)):
        cumul_prop.append(cumul_prop[i-1] + fitness[i]/fit_sum)
    rv = random.uniform(0,1/mating_pool_size)
    i=0
    while len(selected_to_mate) < mating_pool_size:
        while rv <= cumul_prop[i]:
            selected_to_mate.append(population[i])
            rv = rv +1/mating_pool_size
        i = i+1
    return selected_to_mate


def mu_plus_lambda(cur_pop, offsprings):
    """
    Mu plus lambda selection
    :param cur_pop: current population
    :param offsprings: current offspring
    :return: new population
    """
    length = len(cur_pop)
    temp_pop = cur_pop + offsprings

    temp_pop = sorted(temp_pop, key=lambda item:item.length)
    pop = []
    for i in range(length):
        pop.append(temp_pop[i])

    return pop


def random_selection(population, mating_pool_size):
    """

    :param population:
    :param mating_pool_size:
    :return:
    """
    selected_to_mate = random.sample(population, mating_pool_size)
    return selected_to_mate

def random_survival(cur_pop, offsprings):
    """

    :param cur_pop:
    :param offsprings:
    :return:
    """
    temp_pop = cur_pop + offsprings

    pop = random.sample(temp_pop, len(cur_pop))

    return pop

