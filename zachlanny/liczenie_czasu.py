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

    return path

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

def measure_total_execution_time(file_path):
    start_time = time.time()  # Czas rozpoczęcia programu

    cities = read_lines(file_path)
    greedy_path = greedy_tsp(cities)

    end_algorithm_time = time.time()  # Czas zakończenia działania algorytmu
    total_algorithm_time = end_algorithm_time - start_time  # Całkowity czas działania algorytmu

    plot_route(greedy_path, cities)

    end_display_time = time.time()  # Czas zakończenia wyświetlania trasy
    total_execution_time = end_display_time - start_time  # Całkowity czas działania programu do wyświetlenia trasy

    return total_algorithm_time, total_execution_time

file_path = 'lin105.tsp'
total_algorithm_time, total_execution_time = measure_total_execution_time(file_path)
print("Całkowity czas działania algorytmu:", total_algorithm_time, "sekund")
print("Całkowity czas działania programu do wyświetlenia trasy:", total_execution_time, "sekund")
