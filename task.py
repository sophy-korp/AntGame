from Evolution import Evolution
import random


class Optimizer:
    POPULATION_SIZE = 5000
    ITERATIONS = 1000
    CHROMOSOME_LENGTH = 83
    SEED = 100

    @staticmethod
    def optimize(field):
        evolution = Evolution(field, Optimizer.CHROMOSOME_LENGTH, Optimizer.POPULATION_SIZE)

        population = [evolution.random_chromosome() for _ in range(Optimizer.POPULATION_SIZE)]

        for _ in range(Optimizer.ITERATIONS):
            for i in range(len(population)):
                population[i] = evolution.mutate(population[i])

            population = evolution.crossover(population)
            population = evolution.select(population)
            pass

        # After final iteration, select the best chromosomes
        final_population = evolution.select(population)
        # The best chromosome is the first in the sorted list
        return final_population[0]
