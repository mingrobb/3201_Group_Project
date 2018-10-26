import Extract_cities
from math import sqrt

#file to open
file = "Cities/TSP_WesternSahara_29.txt"

#extract all the cities information from the given file
cities = Extract_cities.get_cities(file)

class City(object):
    """
    A city class which is use to store city object, and automatically add to the cities dictionary
    """

    def __init__(self, name, x, y, distances=None):
        """
        Initialize city object and automatically add the city into the cities dictionary
        :param name: city name
        :param x: x coordinate
        :param y: y coordinate
        """
        self.name = name
        self.x = x
        self.y = y

        self.distances = {}
        if distances:
            self.distances = distances


    def cal_distance(self):
        """
        A function to calculate the distance between salesman city and the other cities.
        Add the distance into the distances dictionary
        """
        for key, value in cities.items():
            point_dist = self.point_distance(self.x, self.y, value[0], value[1])
            self.distances[key] = point_dist


    def point_distance(self, x1, y1, x2, y2):
        """
        A function to calculate the Euclidean distance between two cities
        :param x1, y1: coordinates of the city that the salesman in
        :param x2, y2: coordinates of the destination city
        :return: Euclidean distance between teo cities
        """
        return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


########################
######            ######
######    Test    ######
######            ######
########################
"""
city = City('1', 20833.3333, 17100.0000)
city.cal_distance()
print(city.distances)
"""


