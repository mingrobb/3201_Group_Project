import random
import CityMap

class Tour(object):
    """
    Stores an ordered list of all city id and the length of the tour
    """
    def __init__(self, city_map, tour=None):
        """
        An initializer to initialize the tour object
        :param file: A file that contains city information

        self.tour: a random shuffle list of all city id
        self.cities: a dictionary that contains all the city information
        self.length: the length of the tour
        """
        self.city_map = city_map
        self.cities = city_map.keys()
        self.city_objects = []
        if tour:
            self.tour = tour
            self.length = self.cal_len()
        else:
            self.tour = sorted(list(self.cities), key=lambda *args: random.random())
            self.length = self.cal_len()
        self.fitness = 1/self.length


    def cal_len(self):
        """
        A function to calculate the length of a tour
        :return: the total length of the tour
        """
        tour_length = 0.0

        for city in self.tour:
            # add distance between current city to the next city
            self.city_objects.append(self.city_map[city])
            if city != self.tour[-1]:
                next_city = self.tour[self.tour.index(city)+1]
                distance_to_next = self.city_map[city].distances[next_city]
                tour_length += distance_to_next

            else:
                #add the distance between the last city and the first city
                start_city = self.tour[0]
                distance_to_next = self.city_map[city].distances[start_city]
                tour_length += distance_to_next

        return tour_length


########################
######            ######
######    Test    ######
######            ######
########################
"""
file = "Cities/TSP_WesternSahara_29.txt"
c = CityMap.CityMap(file)
city_map = c.city_map
tour = Tour(city_map, None)
print(tour.length)
print(tour.tour)
print(len(tour.tour))
print(len(tour.city_objects))
for k,v in tour.city_map.items():
    print(v.id, v.x, v.y)
    print(v.distances)
"""