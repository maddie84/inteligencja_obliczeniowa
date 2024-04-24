import random
import math
# Implementacja operacji zmiany trasy
def swap(tour, i, j):
    tour[i], tour[j] = tour[j], tour[i]
def reverse(tour, i, j):
    while i < j:
        tour[i], tour[j] = tour[j], tour[i]
        i += 1
        j -= 1
def insert(tour, i, j):
    if i < j:
        tour[i+1:j+1] = tour[i:j]
    elif i > j:
        tour[j:i+1] = tour[j+1:i+2]
# Implementacja funkcji kosztu (koszt całego cyklu)
def total_distance(tour, distances):
    total = 0
    n = len(tour)
    for i in range(n):
        total += distances[tour[i]][tour[(i+1) % n]]
    return total
# Implementacja algorytmu symulowanego wyżarzania
def simulated_annealing(distances, initial_solution, initial_temperature, cooling_rate, iterations):
    current_solution = initial_solution[:]
    best_solution = initial_solution[:]
    current_cost = total_distance(current_solution, distances)
    best_cost = current_cost
    temperature = initial_temperature
    for _ in range(iterations):
        # Wybór losowej operacji zmiany trasy
        operator = random.choice([swap, reverse, insert])
        # Wybór losowych indeksów dla operacji
        i, j = random.sample(range(len(current_solution)), 2)
        # Zastosowanie wybranej operacji na aktualnym rozwiązaniu
        operator(current_solution, i, j)
        new_cost = total_distance(current_solution, distances)
        # Akceptacja nowego rozwiązania w zależności od różnicy kosztów i temperatury
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temperature):
            current_cost = new_cost
            if current_cost < best_cost:
                best_solution = current_solution[:]
                best_cost = current_cost
        else:
            # Odrzucenie zmiany, przywrócenie poprzedniego rozwiązania
            operator(current_solution, i, j)
        # Aktualizacja temperatury
        temperature *= cooling_rate
    return best_solution, best_cost
# Przykładowe wywołanie algorytmu dla zestawu danych
# Tutaj zakładamy, że distances to macierz odległości dla konkretnego zestawu danych z TSPlib,
# a initial_solution to początkowe rozwiązanie w postaci permutacji indeksów
# distances = ... # Macierz odległości dla danego zestawu danych
# initial_solution = ... # Początkowe rozwiązanie
# initial_temperature = ... # Temperatura początkowa
# cooling_rate = ... # Współczynnik chłodzenia
# iterations = ... # Liczba iteracji
# best_solution, best_cost = simulated_annealing(distances, initial_solution, initial_temperature, cooling_rate, iterations)