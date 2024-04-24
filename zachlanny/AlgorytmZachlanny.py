import os
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

def plot_route(route, cities, file_name):
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
    plt.savefig(file_name)  # Zapisz wykres do pliku obrazu
    plt.close()  # Zamknij bieżący wykres

data_dir = 'data'

program_start_time = time.time()

for filename in os.listdir(data_dir):
    if filename.endswith('.tsp'):
        # Wczytaj dane z pliku
        cities = read_lines(os.path.join(data_dir, filename))
        # Wykonaj algorytm TSP
        greedy_path, total_distance, execution_time = greedy_tsp(cities)
        # Wygeneruj nazwę pliku dla wykresu
        plot_file_name = os.path.splitext(filename)[0] + '_route.png'
        # Wygeneruj wykres trasy i zapisz go do pliku obrazu
        plot_route(greedy_path, cities, plot_file_name)

        # Wypisz informacje o wynikach do pliku tekstowego
        with open('results.txt', 'a') as file:
            file.write('File: {}\n'.format(filename))
            file.write('Total distance: {}\n'.format(total_distance))
            file.write('Execution time: {} seconds\n'.format(execution_time))
            file.write('Route plot: {}\n\n'.format(plot_file_name))

total_program_time = time.time() - program_start_time
print("Total program time:", total_program_time, "seconds")
