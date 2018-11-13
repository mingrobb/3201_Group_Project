
import random
import Tour
import Initialization

def COWGC(parent1, parent2, file):
    """
    cut on worst gene crossover (advanced method of crossover)
    • Step1: find the worst gene in the first parent, and the worst gene in the second parent.
    • Step 2: using worst gene's city id of parent 1 as the cut point for parent1, and same as parent2
    • Step 3: If (distance1) > (distance2) then
    • Apply the Modified crossover in both parents at the index that have the larger distance.
      Else apply the Modified crossover in both parents at index (4)
    :param parent1: parent tour1
    :param parent2: parent tour2
    :return: offspring tour1 and offspring tour2
    """
    p1_city_objects = parent1.city_objects
    p2_city_objects = parent2.city_objects

    cut_point1, distance1 = cal_cut_point_COWGC(p1_city_objects)
    cut_point2, distance2 = cal_cut_point_COWGC(p2_city_objects)

    print("cut point: ",cut_point1, cut_point2)
    print("distance: ",distance1, distance2)
    print("city1 cut:",parent1.tour[cut_point1])
    print("city2 cut:",parent2.tour[cut_point2])

    #Modified crossover
    if distance1 > distance2:
        offspring1, offspring2 = modified_crossover_COWGC(parent1, parent2,cut_point1, file)
    else:
        offspring1, offspring2 = modified_crossover_COWGC(parent1, parent2, cut_point2, file)

    return offspring1, offspring2


def cal_cut_point_COWGC(parent):
    """
    A function to calculate the cut point for the COWGC method.
    THe cut point is the index of the city that has longest distance
    :param parent: a list of parent city objects
    :return: the cut point
    """
    length = len(parent)
    max_distance = 0
    cut_point = 0

    for city in range(length):
        cur_city = parent[city]
        cur_city.cal_distance()

        if city != length-1:
            next_city = parent[city+1]
            distance = cur_city.distances[next_city.id]
            if distance > max_distance:
                max_distance = distance
                cut_point = city+1
        else:
            start_city = parent[0]
            distance = cur_city.distances[start_city.id]
            if distance > max_distance:
                max_distance = distance
                cut_point = 0

    return cut_point, max_distance


def modified_crossover_COWGC(parent1, parent2, cut_point, file):
    """
    A function to apply modified crossover with given parents and cut point
    :param parent1: a list with tour object
    :param parent2: a list with tour object
    :param cut_point: the cut point use to apply crossover
    :return: the offsprings (the lists with city id)
    """
    tour1 = parent1.tour
    tour2 = parent2.tour
    p1_left = tour1[:cut_point]
    p2_left = tour2[:cut_point]
    off1 = p1_left
    off2 = p2_left

    for i in tour2:
        if i not in p1_left:
            off1.append(i)
        else:
            continue

    for i in tour1:
        if i not in p2_left:
            off2.append(i)
        else:
            continue

    offspring1 = Tour.Tour(file, off1)
    offspring2 = Tour.Tour(file, off2)

    return offspring1, offspring2


########################
######            ######
######    Test    ######
######            ######
########################
"""
file  = "Cities/TSP_WesternSahara_29.txt"
Object = Initialization.Population(4, file)
pop = Object.population
p1 = pop[0][0]
p2 = pop[1][0]
print("parents:")
print(p1.tour, "fitness: ",p1.fitness )
print(p2.tour, "fitness: ",p2.fitness )
o1, o2 = COWGC(p1, p2, file)
print("offsprings:")
print(o1.tour, "fitness: ",o1.fitness)
print(o2.tour, "fitness: ", o2.fitness)
print()
#check unique
o11 =set(o1.tour)
o22 = set(o2.tour)
print(len(o11))
print(len(o22))
"""

