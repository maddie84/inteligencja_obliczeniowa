import random

# Funkcja celu - minimalizujemy funkcję kwadratową
def funkcja_celu(x):
    return x ** 2

# Funkcja generująca populację początkową
def generuj_populacje_rozwiazan(rozmiar_populacji, przedzial):
    populacja = []
    for _ in range(rozmiar_populacji):
        x = random.uniform(przedzial[0], przedzial[1])
        populacja.append(x)
    return populacja

# Funkcja oceny - oceniamy wszystkie rozwiązania w populacji
def ocen_rozwiazania(populacja):
    oceny = []
    for osobnik in populacja:
        oceny.append(funkcja_celu(osobnik))
    return oceny

# Funkcja selekcji - wybieramy rozwiązania do reprodukcji
def selekcja(populacja, oceny, liczba_osobnikow_do_selekcji):
    najlepsi_indeksy = sorted(range(len(oceny)), key=lambda i: oceny[i])[:liczba_osobnikow_do_selekcji]
    najlepsi_osobnicy = [populacja[i] for i in najlepsi_indeksy]
    return najlepsi_osobnicy

# Funkcja reprodukcji - krzyżujemy wybrane rozwiązania
def reprodukcja(selekcja):
    nowa_populacja = []
    for _ in range(len(selekcja)):
        rodzic1 = random.choice(selekcja)
        rodzic2 = random.choice(selekcja)
        dziecko = (rodzic1 + rodzic2) / 2  # Prosta metoda krzyżowania - średnia arytmetyczna
        nowa_populacja.append(dziecko)
    return nowa_populacja

# Funkcja mutacji - mutujemy nową populację
def mutacja(nowa_populacja, prawdopodobienstwo_mutacji, przedzial):
    for i in range(len(nowa_populacja)):
        if random.random() < prawdopodobienstwo_mutacji:
            nowa_populacja[i] = random.uniform(przedzial[0], przedzial[1])
    return nowa_populacja

# Parametry algorytmu
rozmiar_populacji = 10
przedzial = (-10, 10)
liczba_generacji = 50
liczba_osobnikow_do_selekcji = 5
prawdopodobienstwo_mutacji = 0.1

# Główna pętla algorytmu ewolucyjnego
populacja = generuj_populacje_rozwiazan(rozmiar_populacji, przedzial)
for _ in range(liczba_generacji):
    oceny = ocen_rozwiazania(populacja)
    najlepsi_osobnicy = selekcja(populacja, oceny, liczba_osobnikow_do_selekcji)
    nowa_populacja = reprodukcja(najlepsi_osobnicy)
    nowa_populacja = mutacja(nowa_populacja, prawdopodobienstwo_mutacji, przedzial)
    populacja = nowa_populacja

# Wybieramy najlepszego osobnika
oceny = ocen_rozwiazania(populacja)
najlepszy_indeks = oceny.index(min(oceny))
najlepsze_rozwiazanie = populacja[najlepszy_indeks]
najlepsza_ocena = min(oceny)

print("Najlepsze rozwiązanie:", najlepsze_rozwiazanie)
print("Wartość funkcji celu dla najlepszego rozwiązania:", najlepsza_ocena)
