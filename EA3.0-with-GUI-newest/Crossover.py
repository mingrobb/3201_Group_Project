
import Tour
import random
#from numpy import random
import collections

def COWGC(parent1, parent2, city_map):
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
    #p1_city_objects = parent1.city_objects
    #p2_city_objects = parent2.city_objects

    cut_point1, distance1 = cal_cut_point_COWGC(parent1)
    cut_point2, distance2 = cal_cut_point_COWGC(parent2)

    #Modified crossover
    if distance1 > distance2:
        offspring1, offspring2 = modified_crossover_COWGC(parent1, parent2,cut_point1, city_map)
    else:
        offspring1, offspring2 = modified_crossover_COWGC(parent1, parent2, cut_point2, city_map)

    return offspring1, offspring2


def cal_cut_point_COWGC(parent):
    """
    A function to calculate the cut point for the COWGC method.
    THe cut point is the index of the city that has longest distance
    :param parent: a list of parent city objects
    :return: the cut point
    """
    cut_point = parent.worst_idx[1]
    max_distance = parent.max_distance

    """
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
    """

    return cut_point, max_distance


def modified_crossover_COWGC(parent1, parent2, cut_point, city_map):
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
    off1 = collections.deque(p1_left)
    off2 = collections.deque(p2_left)

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

    offspring1 = Tour.Tour(city_map, list(off1))
    offspring2 = Tour.Tour(city_map, list(off2))

    return offspring1, offspring2

def order_crossover(parent1, parent2, city_map):
    """
    Perform order crossover between two parents and generate two offsprings
    :param parent1: a tour object
    :param parent2: a tour object
    :param city_map: a map that contains all the city information
    :return:
    """
    p1 = parent1.tour
    p2 = parent2.tour
    off1 = collections.deque()
    off2 = collections.deque()
    length = len(p1)

    #points = random.randint(1, length-1, 2)
    point1 = random.randint(0, 28)
    point2 = random.randint(0, 28)
    points = [point1, point2]
    if points[0] > points[1]:
        points[0], points[1] = points[1], points[0]

    cut1 = points[0]
    cut2 = points[1]

    part1 = p1[cut1:cut2+1]
    part2 = p2[cut1:cut2+1]

    for i in range(length):
        if p1[i] in part2:
            off1.appendleft(None)
        else:
            off1.append(p1[i])
        if p2[i] in part1:
            off2.appendleft(None)
        else:
            off2.append(p2[i])

    off1.rotate(cut1)
    off2.rotate(cut1)
    j = 0
    for i in range(cut1, cut2+1):
        off1[i] = part2[j]
        off2[i] = part1[j]
        j += 1


    offspring1 = Tour.Tour(city_map, list(off1))
    offspring2 = Tour.Tour(city_map, list(off2))

    return offspring1, offspring2


