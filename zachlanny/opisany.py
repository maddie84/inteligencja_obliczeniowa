import math
import time
import matplotlib.pyplot as plt

# Funkcja obliczająca odległość między dwoma miastami
def distance(city1, city2):
    return math.sqrt((city1[1] - city2[1])**2 + (city1[2] - city2[2])**2)

# Funkcja obliczająca długość trasy dla danej permutacji miast
def route_length(route):
    total_distance = 0
    for i in range(len(route)):
        total_distance += distance(route[i], route[(i + 1) % len(route)])
    return total_distance

# Funkcja wczytująca dane z pliku lin105.tsp
def read_lines(file_path):
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

def greedy_tsp(cities):
    """
    Implementacja algorytmu zachłannego dla problemu komiwojażera.

    Args:
    - cities (list): Lista miast, gdzie każde miasto jest krotką (id_miasta, wsp_x, wsp_y).

    Returns:
    - path (list): Lista miast tworzących trasę.
    - total_distance (float): Całkowita długość trasy.
    - execution_time (float): Czas wykonania funkcji w sekundach.

    Opis algorytmu:
    1. Odwiedź pierwsze miasto i oznacz je jako odwiedzone.
    2. Powtarzaj poniższe kroki, dopóki nie odwiedzisz wszystkich miast:
        a. Wybierz ostatnie odwiedzone miasto jako bieżące miasto.
        b. Znajdź najbliższe nieodwiedzone miasto.
        c. Dodaj to miasto do trasy.
        d. Oznacz dodane miasto jako odwiedzone.
    3. Oblicz całkowitą długość trasy.
    4. Zwróć trasę, długość trasy i czas wykonania funkcji.
    """
    start_time = time.time()  # Początkowy czas wykonania funkcji
    visited = [False] * len(cities)  # Lista odwiedzonych miast, początkowo wszystkie jako False
    path = [cities[0]]  # Rozpoczynamy od pierwszego miasta
    visited[0] = True  # Oznaczamy pierwsze miasto jako odwiedzone

    while len(path) < len(cities):  # Dopóki nie odwiedzimy wszystkich miast
        current_city = path[-1]  # Aktualne miasto to ostatnie miasto na trasie
        min_distance = float('inf')  # Inicjalizujemy minimalną odległość jako nieskończoność
        closest_city = None  # Najbliższe miasto początkowo jako None

        # Iterujemy przez wszystkie miasta
        for city in cities:
            if not visited[city[0] - 1]:  # Sprawdzamy, czy miasto nie zostało odwiedzone
                dist = distance(current_city, city)  # Obliczamy odległość między miastami
                if dist < min_distance:  # Jeśli odległość mniejsza niż dotychczasowa minimalna
                    min_distance = dist  # Aktualizujemy minimalną odległość
                    closest_city = city  # Ustawiamy aktualne miasto jako najbliższe

        path.append(closest_city)  # Dodajemy najbliższe miasto do trasy
        visited[closest_city[0] - 1] = True  # Oznaczamy dodane miasto jako odwiedzone

    total_distance = route_length(path)  # Obliczamy całkowitą długość trasy
    execution_time = time.time() - start_time  # Obliczamy czas wykonania funkcji

    return path, total_distance, execution_time  # Zwracamy trasę, długość trasy i czas wykonania funkcji

# Funkcja rysująca trasę z oznaczeniem numerów miast
def plot_route(route, cities):
    x = [city[1] for city in cities]  # Współrzędne x miast
    y = [city[2] for city in cities]  # Współrzędne y miast
    plt.figure(figsize=(8, 6))  # Ustawienie rozmiaru wykresu
    plt.plot(x, y, 'bo')  # Narysowanie wszystkich miast jako niebieskich kropek

    # Dodanie numerów miast nad każdą kropką
    for i, city in enumerate(route):
        plt.text(city[1], city[2], str(i+1), fontsize=9, ha='center', va='center')

    # Narysowanie linii łączących miasta w kolejności odwiedzania
    for i in range(len(route) - 1):
        plt.arrow(route[i][1], route[i][2], 
                  route[i + 1][1] - route[i][1], 
                  route[i + 1][2] - route[i][2], 
                  head_width=0.5, length_includes_head=True)
    # Narysowanie linii łączącej ostatnie miasto z pierwszym, aby zamknąć trasę
    plt.arrow(route[-1][1], route[-1][2], 
              route[0][1] - route[-1][1], 
              route[0][2] - route[-1][2], 
              head_width=0.5, length_includes_head=True)

    plt.show()

# Wczytaj dane z pliku lin105.tsp
#cities = read_lines('data/lin105.tsp')
cities = read_lines('data/pr2392.tsp')

# Znajdź trasę algorytmem zachłannym
greedy_path, total_distance, execution_time = greedy_tsp(cities)

# Wyświetl trasę
print("Trasa znaleziona przez algorytm zachłanny:")
for city in greedy_path:
    print(city)

# Wyświetl wizualizację trasy z oznaczonymi numerami miast
plot_route(greedy_path, cities)

# Wyświetl długość trasy i czas wykonania
print("Długość trasy:", total_distance)
print("Czas wykonania:", execution_time, "sekund")
