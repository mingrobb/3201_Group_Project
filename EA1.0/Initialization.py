import Tour

class Population(object):
    """
    Using dictionary to store a list of tour object

    Population:
        self.population = {1: [tour object1, fitness1], 2: [tour object2, fitness2],...... }
    """
    def __init__(self, size, city_map):
        """
        An initializer to initialize the population with a given size

        self.size: a size of the population
        self.file: a cities file to be generated
        self.population: a dictionary to store tour objects and automatically calculate the fitness for each tour
        """
        self.size = size
        self.city_map = city_map
        self.population = []

        for i in range(size):
            new_tour = Tour.Tour(self.city_map)
            fitness = new_tour.fitness
            self.population.append([new_tour, fitness])



########################
######            ######
######    Test    ######
######            ######
########################
""""
size = 10
file = "Cities/TSP_WesternSahara_29.txt"
c = CityMap.CityMap(file)
city_map = c.city_map
p = Population(10, city_map)
for i in p.population:
    print(i[1])
"""