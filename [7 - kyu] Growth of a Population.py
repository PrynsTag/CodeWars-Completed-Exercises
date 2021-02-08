def nb_year(population, percent, aug, target):
    year = 0
    while population < target:
        population = int(population + (population * float((percent / 100)) + aug))
        year += 1

    return year


if __name__ == '__main__':
    print(nb_year(1000, 2, 50, 1213) == 3)
    print(nb_year(1500, 5, 100, 5000) == 15)
    print(nb_year(1500000, 2.5, 10000, 2000000) == 10)
    print(nb_year(1500000, 0.25, 1000, 2000000) == 94)
