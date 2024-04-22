import math
import random
import matplotlib.pyplot as plt

# Funkcja obliczająca odległość między dwoma punktami (miastami)
def distance(city1, city2):
    return math.sqrt((city1[1] - city2[1])**2 + (city1[2] - city2[2])**2)

# Funkcja generująca losowe początkowe rozwiązanie (losowa permutacja miast)
def initial_solution(cities):
    return random.sample(cities, len(cities))

# Funkcja obliczająca długość trasy dla danej permutacji miast
def route_length(route):
    total_distance = 0
    for i in range(len(route)):
        total_distance += distance(route[i], route[(i + 1) % len(route)])
    return total_distance

# Algorytm Symulowanego Wyżarzania (SA)
def simulated_annealing(cities, initial_temperature, cooling_rate, iterations):
    current_solution = initial_solution(cities)
    best_solution = current_solution.copy()
    temperature = initial_temperature

    for i in range(iterations):
        # Wybierz losową parę miast i zamień je miejscami
        new_solution = current_solution.copy()
        index1, index2 = random.sample(range(len(new_solution)), 2)
        new_solution[index1], new_solution[index2] = new_solution[index2], new_solution[index1]

        # Oblicz różnicę w długości tras
        delta_distance = route_length(new_solution) - route_length(current_solution)

        # Jeśli nowe rozwiązanie jest lepsze lub spełnia warunek akceptacji
        if delta_distance < 0 or random.random() < math.exp(-delta_distance / temperature):
            current_solution = new_solution.copy()

            # Zapisz najlepsze znalezione rozwiązanie
            if route_length(current_solution) < route_length(best_solution):
                best_solution = current_solution.copy()

        # Schładzanie
        temperature *= cooling_rate

    return best_solution

# Funkcja wczytująca dane z pliku lin105.tsp
def read_lin105(file_path):
    cities = []
    with open(file_path, 'r') as file:
        next(file)  # Pomijamy pierwszą linię (NAME: lin105)
        next(file)  # Pomijamy drugą linię (TYPE: TSP)
        next(file)  # Pomijamy trzecią linię (COMMENT)
        next(file)  # Pomijamy czwartą linię (DIMENSION)
        next(file)  # Pomijamy piątą linię (EDGE_WEIGHT_TYPE)
        next(file)  # Pomijamy linię przed sekcją danych (NODE_COORD_SECTION)
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

# Funkcja rysująca trasę
def plot_route(route, cities):
    x = [city[1] for city in cities]
    y = [city[2] for city in cities]
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'bo')
    for i in range(len(route) - 1):
        plt.arrow(cities[route[i][0] - 1][1], cities[route[i][0] - 1][2], 
                  cities[route[i + 1][0] - 1][1] - cities[route[i][0] - 1][1], 
                  cities[route[i + 1][0] - 1][2] - cities[route[i][0] - 1][2], 
                  head_width=0.5, length_includes_head=True)
    plt.arrow(cities[route[-1][0] - 1][1], cities[route[-1][0] - 1][2], 
              cities[route[0][0] - 1][1] - cities[route[-1][0] - 1][1], 
              cities[route[0][0] - 1][2] - cities[route[-1][0] - 1][2], 
              head_width=0.5, length_includes_head=True)
    plt.show()


# wczytanie danych z pliku lin105.tsp
cities = read_lin105('data/lin105.tsp')

# parametry
initial_temperature = 1000
cooling_rate = 0.99
iterations = 1000

print("Simulated Annealing:")
sa_route = simulated_annealing(cities, initial_temperature, cooling_rate, iterations)
print("Route Length:", route_length(sa_route))

plot_route(sa_route, cities)
