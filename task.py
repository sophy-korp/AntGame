from Evolution import Evolution
import random


class Optimizer:
    POPULATION_SIZE = 5000
    ITERATIONS = 10
    CHROMOSOME_LENGTH = 83
    SEED = 39

    @staticmethod
    def optimize(field):
        evolution = Evolution(field, Optimizer.CHROMOSOME_LENGTH, Optimizer.POPULATION_SIZE)

        # population = [evolution.random_chromosome(Optimizer.SEED) for _ in range(Optimizer.POPULATION_SIZE)]
        population = evolution.random_chromosome(Optimizer.SEED)
        for _ in range(Optimizer.ITERATIONS):
            # создайте здесь своего муравья используя реализованные методы в Evolution
            # Возможный вариант реализации:
            # Проведите несколько мутаций с каждой особью
            # Сделайте селекцию
            # Сделайте кроссовер
            mutated_population = [evolution.mutate(chromosome) for chromosome in population]
            population = evolution.crossover(mutated_population)
            mutated_population = [evolution.mutate(chromosome) for chromosome in population]
            population = evolution.select(mutated_population)

        # After final iteration, select the best chromosomes
        final_population = evolution.select(population)
        # The best chromosome is the first in the sorted list
        return final_population[0]
