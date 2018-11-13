import City
import Extract_cities

class CityMap(object):
    """

    """
    def __init__(self,file):
        """

        """
        self.city_map = {}
        cities = Extract_cities.get_cities(file)
        for k,v in cities.items():
            id = k
            x = v[0]
            y = v[1]
            city = City.City(id, x, y, file)
            city.cal_distance()
            self.city_map[id] = city


########################
######            ######
######    Test    ######
######            ######
########################
"""
file = "Cities/TSP_WesternSahara_29.txt"
cityMap = CityMap(file)
for k,v in cityMap.city_map.items():
    print(v.id, v.x, v.y)
    print(v.distances, v.x)
    print()
"""