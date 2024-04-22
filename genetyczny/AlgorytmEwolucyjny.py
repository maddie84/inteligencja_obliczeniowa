import numpy as np
from funkcje_wizualizacja.functions import *

# Algorytm ewolucyjny
def evolutionary_algorithm(objective_function, num_of_ind, num_of_gen, k, pc, pm, bounds, dim):
    # Inicjalizacja populacji
    def initialize_population(num_of_ind, bounds):
        population = []
        for _ in range(num_of_ind):
            individual = [np.random.uniform(low, high) for low, high in bounds]
            population.append(individual)
        return population

    # Ocena populacji
    def evaluate_population(population):
        return [objective_function(individual) for individual in population]

    # Selekcja
    def selection(population, fitness, k):
        selected_population = []
        for _ in range(len(population)):
            selected = tournament_selection(population, fitness, k)
            selected_population.append(selected)
        return selected_population

    # Krzyżowanie
    def crossover(population, pc):
        new_population = []
        for i in range(0, len(population), 2):
            parent1 = population[i]
            parent2 = population[i+1]

            if np.random.rand() < pc:
                crossover_point = np.random.randint(1, len(parent1))
                child1 = parent1[:crossover_point] + parent2[crossover_point:]
                child2 = parent2[:crossover_point] + parent1[crossover_point:]
                new_population.append(child1)
                new_population.append(child2)
            else:
                new_population.append(parent1)
                new_population.append(parent2)

        return new_population

    # Mutacja
    def mutation(population, pm, bounds):
        for i in range(len(population)):
            if np.random.rand() < pm:
                mutation_index = np.random.randint(len(population[i]))
                population[i][mutation_index] = np.random.uniform(bounds[mutation_index][0], bounds[mutation_index][1])

    # Sukcesja
    def succession(population_P, fitness_P, population_O, fitness_O):
        population_P += population_O
        fitness_P += fitness_O
        sorted_indices = np.argsort(fitness_P)
        return [population_P[index][:dim] for index in sorted_indices[:len(sorted_indices)//2]]  

    # Inicjalizacja populacji początkowej
    population_P = initialize_population(num_of_ind, bounds)

    # Ocena populacji początkowej
    fitness_P = evaluate_population(population_P)

    best_fitness = min(fitness_P)
    best_solution = population_P[np.argmin(fitness_P)][:dim]  

    # Pętla algorytmu ewolucyjnego
    for gen in range(num_of_gen):
        # Selekcja
        population_T = selection(population_P, fitness_P, k)
        # Krzyżowanie
        population_O = crossover(population_T, pc)
        # Mutacja
        mutation(population_O, pm, bounds)
        # Ocena nowej populacji
        fitness_O = evaluate_population(population_O)

        # Sukcesja
        population_P = succession(population_P, fitness_P, population_O, fitness_O)
        fitness_P = evaluate_population(population_P)

        current_best_fitness = min(fitness_P)
        if current_best_fitness < best_fitness:
            best_fitness = current_best_fitness
            best_solution = population_P[np.argmin(fitness_P)][:dim]  

    return best_fitness, best_solution

# Funkcja do turniejowej selekcji
def tournament_selection(population, fitness, k):
    selected_index = np.random.choice(len(population), k)
    selected_fitness = [fitness[index] for index in selected_index]
    return population[selected_index[np.argmin(selected_fitness)]]

# Parametry algorytmu
num_of_ind = 100    # rozmiar populacji
num_of_gen = 100   # liczba generacji 
k = int(round(0.3*num_of_ind, 0))   # liczba osobnikow do turnieju
pc = 0.95   # prawdopodobienstwo krzyzowania
pm = 0.05   # prawdopodobienstwo mutacji 
bounds = [(-5.12, 5.12)] * 10  # 10 wymiarów dla funkcji sphere_function
dim = 5  # liczba zmiennych decyzyjnych do zwrócenia jako rozwiązanie

# func = levy_function
func = perm_function
# func = schwefel_function
# func = sphere_function
# func = ackley_function

best_fitness_sphere, best_solution_sphere = evolutionary_algorithm(func, num_of_ind, num_of_gen, k, pc, pm, bounds, dim)
print("Best Fitness:", best_fitness_sphere)
print("Best Solution:", best_solution_sphere)
