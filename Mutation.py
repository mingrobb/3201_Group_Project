import Tour
import random
import CityMap

def inversion_mutation(individual, city_map):
    """

    :param indeividual:
    :param citymap:
    :return:
    """
    tour = individual.tour
    point1 = random.randint(0, len(tour)-1)
    while point1 == len(tour)-1:
        point1 = random.randint(0, len(tour)-1)
    point2 = random.randint(point1+1, len(tour)-1)

    partial_tour = tour[point1:point2+1]
    reversed= partial_tour[::-1]

    tour[point1:point2+1] = reversed

    offspring = Tour.Tour(city_map, tour)

    return offspring

def RGIBNNM_mutation(individual, city_map):
    """

    :param individual:
    :param city_map:
    :return:
    """
    tour = individual.tour
    rand_idx = random.randint(0, len(tour)-1)
    city = tour[rand_idx]

    #find the nearest city
    distance_to = city_map[city].distances
    #nearest_city = min(distance_to.keys(), key=(lambda k: distance_to[k]))
    nearest_city = sorted(distance_to.items(), key=lambda kv: kv[1], reverse=False)[1][0]

    #get a random city around nearest_city (range = 5)
    d = city_map[nearest_city].distances
    five_neignbours = sorted(d.items(), key=lambda kv: kv[1], reverse=False)[1:6]
    selected = random.choice(five_neignbours)[0]

    n_i = 0
    s_i = 0
    for i in range(len(tour)):
        if tour[i] == nearest_city:
            n_i = i
        if tour[i] == selected:
            s_i = i

    temp = tour[n_i]
    tour[n_i] = tour[s_i]
    tour[s_i] = temp

    offspring = Tour.Tour(city_map, tour)

    return offspring


def IRGIBNNM_mutation(individual, city_map):
    """

    :param indeividual:
    :param city_map:
    :return:
    """
    #apply inversion mutation first
    invert = inversion_mutation(individual, city_map)

    #apply RGIBNNM mutation
    offspring = RGIBNNM_mutation(invert, city_map)

    return offspring



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
"""
Inversion mutation
file  = "Cities/TSP_WesternSahara_29.txt"
c = CityMap.CityMap(file)
city_map = c.city_map
tour = Tour.Tour(city_map)
print(tour.tour)
mut = inversion_mutation(tour, city_map)
print(mut.tour)
s = set(mut.tour)
print(len(s))
"""
"""
#RGIBNNM
file  = "Cities/TSP_WesternSahara_29.txt"
c = CityMap.CityMap(file)
city_map = c.city_map
tour = Tour.Tour(city_map)
print(tour.tour)
mut = IRGIBNNM_mutation(tour, city_map)
print(mut.tour)
"""
