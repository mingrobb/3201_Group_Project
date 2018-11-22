########################
######            ######
######    Test    ######
######            ######
########################
"""
#Extract_cities.py
cities = get_cities("Cities/TSP_WesternSahara_29.txt")
print(cities)
"""

"""
#City.py
file = "Cities/TSP_WesternSahara_29.txt"
city = City(1, 20833.3333, 17100.0000, file)
city.cal_distance()
print(city.distances)
"""

"""
#CityMap.py
file = "Cities/TSP_WesternSahara_29.txt"
cityMap = CityMap(file)
for k,v in cityMap.city_map.items():
    print(v.id, v.x, v.y)
    print(v.distances, v.x)
    print()
"""

"""
Tour.py
file = "Cities/TSP_WesternSahara_29.txt"
c = CityMap.CityMap(file)
city_map = c.city_map
tour = Tour(city_map, None)
print(tour.length)
print(tour.tour)
print(len(tour.tour))
print(len(tour.city_objects))
""
for k,v in tour.city_map.items():
    print(v.id, v.x, v.y)
    print(v.distances)
""
print()
print(tour.worst_idx)
print(tour.max_distance)
x = tour.city_objects[tour.worst_idx[0]].id
y = tour.city_objects[tour.worst_idx[1]].id
print(x, y)
print(city_map[x].distances[y])
"""

"""
Initialization
size = 10
file = "Cities/TSP_WesternSahara_29.txt"
c = CityMap.CityMap(file)
city_map = c.city_map
p = Population(10, city_map)
for i in p.population:
    print(i.tour)
print()
p.evalPopulation()
for i in p.population:
    print(i.tour)
"""

"""
Crossover.COWGC
file  = "Cities/TSP_WesternSahara_29.txt"
c = CityMap.CityMap(file)
city_map = c.city_map
Object = Initialization.Population(4, city_map)
pop = Object.population
p1 = pop[0][0]
p2 = pop[1][0]
print("parents:")
print(p1.tour, "fitness: ",p1.fitness )
print(p2.tour, "fitness: ",p2.fitness )
o1, o2 = COWGC(p1, p2, city_map)
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
"""
Crossover.order_crossover
file  = "Cities/TSP_WesternSahara_29.txt"
c = CityMap.CityMap(file)
city_map = c.city_map
Object = Initialization.Population(4, city_map)
pop = Object.population
p1 = pop[0]
p2 = pop[1]
print("parents:")
print(p1.tour)
print(p2.tour)
off1= order_crossover(p1.tour, p2.tour, city_map)
print("offsprings:")
print(off1.tour)
t = set(off1.tour)
print(len(t))
"""

"""
#Selection.parent
file  = "Cities/TSP_WesternSahara_29.txt"
c = CityMap.CityMap(file)
city_map = c.city_map
Object = Initialization.Population(30, city_map)
pop = Object.population
s = tournament_selection(pop, 10, 3)
print(len(s))
for i in s:
    print(i[0].tour, i[1])
"""
"""
#Selection.survival
file  = "Cities/TSP_WesternSahara_29.txt"
c = CityMap.CityMap(file)
city_map = c.city_map
Object = Initialization.Population(2, city_map)
off1 = Initialization.Population(1, city_map)
print('off length:', off1.population[0].length)
off2 = Initialization.Population(1, city_map)
for i in Object.population:
    print(i.length)
pop = mu_plus_lambda(Object.population, off1.population)
for i in pop:
    print(i.length)
"""

"""
#Mutation
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