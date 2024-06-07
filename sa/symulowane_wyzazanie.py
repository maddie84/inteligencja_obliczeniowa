import math
import random
import matplotlib.pyplot as plt
from typing import List, Tuple

def load_tsp_file(file_path: str) -> List[Tuple[int, int]]:
    with open(file_path, 'r') as f:
        lines = f.readlines()[6:]  # Pomijanie pierwszych 6 wierszy
        coords = []
        for line in lines:
            if "EOF" in line:
                break
            parts = line.strip().split()
            coords.append((int(parts[0]), float(parts[1]), float(parts[2])))
        return [(int(coord[1]), int(coord[2])) for coord in coords]


def calculate_total_distance(tour: List[int], coords: List[Tuple[int, int]]) -> float:
    total_distance = 0
    for i in range(len(tour)):
        x1, y1 = coords[tour[i - 1]]
        x2, y2 = coords[tour[i]]
        total_distance += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return total_distance


def swap_cities(tour: List[int]) -> List[int]:
    new_tour = tour[:]
    i, j = random.sample(range(len(tour)), 2)
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour

def reverse_segment(tour: List[int]) -> List[int]:
    new_tour = tour[:]
    i, j = sorted(random.sample(range(len(tour)), 2))
    new_tour[i:j + 1] = reversed(new_tour[i:j + 1])
    return new_tour

def insert_city(tour: List[int]) -> List[int]:
    new_tour = tour[:]
    i, j = random.sample(range(len(tour)), 2)
    city = new_tour.pop(i)
    new_tour.insert(j, city)
    return new_tour

def shuffle_segment(tour: List[int]) -> List[int]:
    new_tour = tour[:]
    i, j = sorted(random.sample(range(len(tour)), 2))
    segment = new_tour[i:j + 1]
    random.shuffle(segment)
    new_tour[i:j + 1] = segment
    return new_tour

def simulated_annealing(coords: List[Tuple[int, int]], initial_temp: float, final_temp: float, alpha: float, max_iterations: int):
    tour = list(range(len(coords)))
    current_temp = initial_temp
    best_tour = tour[:]
    best_distance = calculate_total_distance(tour, coords)
    
    iteration = 0
    while iteration < max_iterations:
        new_tour = random.choice([swap_cities, reverse_segment, insert_city, shuffle_segment])(tour)
        new_distance = calculate_total_distance(new_tour, coords)
        
        if new_distance < best_distance or random.random() < math.exp((best_distance - new_distance) / current_temp):
            tour = new_tour
            best_distance = new_distance
            best_tour = new_tour
        
        current_temp *= alpha
        iteration += 1
        
        # Wizualizacja co 500 iteracji
        if iteration % 500 == 0:
            plt.clf()
            plt.scatter([coords[i][0] for i in tour], [coords[i][1] for i in tour], c='red')
            for i in range(len(tour)):
                x1, y1 = coords[tour[i - 1]]
                x2, y2 = coords[tour[i]]
                plt.plot([x1, x2], [y1, y2], c='blue')
            plt.title(f'Iteration: {iteration}, Distance: {best_distance:.2f}')
            plt.pause(0.01)
    
    return best_tour, best_distance



def main():

    # Dla tras o co najmniej 300 punktach:
    # coords = load_tsp_file('data/pr1002.tsp') 
    # coords = load_tsp_file('data/pr2392.tsp')
    # coords = load_tsp_file('data/u1060.tsp')
    # coords = load_tsp_file('data/ali535.tsp')
    coords = load_tsp_file('data/lin318.tsp')

    initial_temp = 10000
    final_temp = 1
    alpha = 0.995 # współczynnik chłodzenia
    max_iterations = 10000
    best_tour, best_distance = simulated_annealing(coords, initial_temp, final_temp, alpha, max_iterations)

    print(f'Best distance: {best_distance}')
    print(f'Best tour: {best_tour}')

    plt.scatter([coords[i][0] for i in best_tour], [coords[i][1] for i in best_tour], c='red')
    for i in range(len(best_tour)):
        x1, y1 = coords[best_tour[i - 1]]
        x2, y2 = coords[best_tour[i]]
        plt.plot([x1, x2], [y1, y2], c='blue')
    plt.title(f'Final Solution, Distance: {best_distance:.2f}')
    plt.show()

if __name__ == '__main__':
    main()
