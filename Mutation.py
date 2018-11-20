import Tour
import random

def WGWWGM(individual, city_map):
    """
    Worst gene with worst gene mutation
    :param individual: a tour object
    :return: mutated offspring
    """
    city_objects = individual.city_objects
    tour = individual.tour
    max_distance = individual.max_distance
    length = len(city_objects)
    worst_idx1 = individual.worst_idx[1]
    second_max_distance = 0.0
    worst_idx2 = 0

    for city in range(length):
        cur_city = city_objects[city]
        if city != length-1:
            next_city = city_objects[city+1]
            distance = cur_city.distances[next_city.id]
            if distance > second_max_distance and distance < max_distance:
                second_max_distance = distance
                worst_idx2 = city+1
        else:
            start_city = city_objects[0]
            distance = cur_city.distances[start_city.id]
            if distance > second_max_distance and distance < max_distance:
                max_distance = distance
                worst_idx2 = 0

    temp = tour[worst_idx1]
    tour[worst_idx1] = tour[worst_idx2]
    tour[worst_idx2] = temp

    offspring = Tour.Tour(city_map, tour)

    return offspring

def WGWRGM(individual, city_map):
    """
    Worst gene with random gene mutation
    :param individual: a tour object
    :param city_map: city map
    :return: mutated offspring
    """
    worst_idx = individual.worst_idx[1]
    tour = individual.tour
    length = len(tour)

    rand_idx = random.randint(0, length-1)
    temp  = tour[worst_idx]
    tour[worst_idx] = tour[rand_idx]
    tour[rand_idx] = temp

    offspring = Tour.Tour(city_map, tour)

    return offspring

def random_mutate(indiidual, city_map):
    """

    :param indiidual:
    :param city_map:
    :return:
    """


########################
######            ######
######    Test    ######
######            ######
########################
"""
file  = "Cities/TSP_WesternSahara_29.txt"
c = CityMap.CityMap(file)
city_map = c.city_map
tour = Tour.Tour(city_map)
print("        ", tour.tour)
mutant1 = WGWRGM(tour,city_map)
print("WGWRGM: ",mutant1.tour)
mutant2 = WGWWGM(tour,city_map)
print("WGWWGM: ",mutant2.tour)
"""



