import math
import time
import matplotlib.pyplot as plt

def distance(city1, city2):
    return math.sqrt((city1[1] - city2[1])**2 + (city1[2] - city2[2])**2)

def read_lines(file_path):
    cities = []
    with open(file_path, 'r') as file:
        next(file)
        next(file)
        next(file)
        next(file)
        next(file)
        next(file)
        for line in file:
            if line.startswith('EOF'):
                break
            if line.strip():
                city_data = line.strip().split()
                city_id = int(city_data[0])
                x_coord = float(city_data[1])
                y_coord = float(city_data[2])
                cities.append((city_id, x_coord, y_coord))
    return cities

def greedy_tsp(cities):
    start_time = time.time()  # Początkowy czas wykonania funkcji
    visited = [False] * len(cities)
    path = [cities[0]]
    visited[0] = True

    while len(path) < len(cities):
        current_city = path[-1]
        min_distance = float('inf')
        closest_city = None

        for city in cities:
            if not visited[city[0] - 1]:
                dist = distance(current_city, city)
                if dist < min_distance:
                    min_distance = dist
                    closest_city = city

        path.append(closest_city)
        visited[closest_city[0] - 1] = True

    total_distance = sum(distance(path[i], path[(i + 1) % len(path)]) for i in range(len(path)))  # Obliczanie długości trasy
    execution_time = time.time() - start_time  # Obliczanie czasu wykonania funkcji
    return path, total_distance, execution_time

def plot_route(route, cities):
    x = [city[1] for city in cities]
    y = [city[2] for city in cities]
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'bo')
    for i in range(len(route) - 1):
        plt.arrow(route[i][1], route[i][2], 
                  route[i + 1][1] - route[i][1], 
                  route[i + 1][2] - route[i][2], 
                  head_width=0.5, length_includes_head=True)
    plt.arrow(route[-1][1], route[-1][2], 
              route[0][1] - route[-1][1], 
              route[0][2] - route[-1][2], 
              head_width=0.5, length_includes_head=True)
    plt.show()

cities1 = read_lines('data/lin105.tsp')
cities2 = read_lines('data/pr1002.tsp')
cities3 = read_lines('data/pr2392.tsp')
cities4 = read_lines('data/rl5934.tsp')
cities5 = read_lines('data/tsp225.tsp')

greedy_path1, total_distance1, execution_time1 = greedy_tsp(cities1)
greedy_path2, total_distance2, execution_time2 = greedy_tsp(cities2)
greedy_path3, total_distance3, execution_time3 = greedy_tsp(cities3)
greedy_path4, total_distance4, execution_time4 = greedy_tsp(cities4)
greedy_path5, total_distance5, execution_time5 = greedy_tsp(cities5)

plot_route(greedy_path1, cities1)
plot_route(greedy_path2, cities2)
plot_route(greedy_path3, cities3)
plot_route(greedy_path4, cities4)
plot_route(greedy_path5, cities5)

print("Długość trasy:", total_distance1)
print("Czas wykonania:", execution_time1, "sekund")

print("Długość trasy:", total_distance2)
print("Czas wykonania:", execution_time2, "sekund")

print("Długość trasy:", total_distance3)
print("Czas wykonania:", execution_time3, "sekund")

print("Długość trasy:", total_distance4)
print("Czas wykonania:", execution_time4, "sekund")

print("Długość trasy:", total_distance5)
print("Czas wykonania:", execution_time5, "sekund")
