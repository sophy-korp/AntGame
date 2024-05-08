from Evolution import Evolution
import random


class Optimizer:
    POPULATION_SIZE = 5000
    ITERATIONS = 10
    CHROMOSOME_LENGTH = 83
    SEED = 42

    @staticmethod
    def optimize(field):
        rand = random.seed(Optimizer.SEED)
        evolution = Evolution(rand, field, Optimizer.CHROMOSOME_LENGTH, Optimizer.POPULATION_SIZE)

        population = [evolution.random_chromosome() for _ in range(Optimizer.POPULATION_SIZE)]

        for _ in range(Optimizer.ITERATIONS):
            # создайте здесь своего муравья используя реализованные методы в Evolution
            pass

        # After final iteration, select the best chromosomes
        final_population = evolution.select(population)
        # The best chromosome is the first in the sorted list
        return final_population[0]
