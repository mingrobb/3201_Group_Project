import Extract_cities
import random
import City

class Tour(object):
    """
    Stores an ordered list of all city id and the length of the tour
    """
    def __init__(self, file):
        """
        An initializer to initialize the tour object
        :param file: A file that contains city information

        self.tour: a random shuffle list of all city id
        self.cities: a dictionary that contains all the city information
        self.length: the length of the tour
        """
        self.cities = Extract_cities.get_cities(file)
        self.tour = sorted(list(self.cities.keys()), key=lambda *args: random.random())
        self.length = self.cal_len()


    def cal_len(self):
        """
        A function to calculate the length of a tour
        :return: the length of the tour
        """
        #cities = Extract_cities.get_cities(self.file)
        tour_length = 0.0

        for city in self.tour:
            #add distance between current city to the next city
            cur_city = City.City(city, self.cities[city][0], self.cities[city][1])
            cur_city.cal_distance()

            if city != self.tour[-1]:
                next = self.tour[self.tour.index(city)+1]
                next_city = City.City(next, self.cities[next][0], self.cities[next][1])
                next_city.cal_distance()

                distance_to_next = cur_city.distances[next_city.id]
                tour_length += distance_to_next

            else:
                #add the distance between the last city and the first city
                start = self.tour[0]
                start_city = City.City(start, self.cities[start][0], self.cities[start][1])

                distance_to_next = cur_city.distances[start_city.id]
                tour_length += distance_to_next

        return tour_length


########################
######            ######
######    Test    ######
######            ######
########################
"""
file  = "Cities/TSP_WesternSahara_29.txt"
tour = Tour(file)
print(tour.length)
print(tour.tour)
"""
