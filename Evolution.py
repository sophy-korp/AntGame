import copy

import numpy as np
import random


class Evolution:
    def __init__(self, field, chromosome_length, population_size):
        self.field = copy.deepcopy(field)
        self.chromosome_length = chromosome_length
        self.population_size = population_size

    def mutate(self, chromosome):
        mutated = self.invert_bit(chromosome, random.randint(0, self.chromosome_length - 1))
        return mutated if self.field.testAnt(mutated) > self.field.testAnt(chromosome) else chromosome

    def invert_bit(self, chromosome, index):
        mutated = copy.deepcopy(chromosome)
        mutated[index] = not mutated[index]
        return mutated

    def select(self, population):
        scored_population = [(chromosome, self.field.testAnt(chromosome)) for chromosome in population]
        scored_population.sort(key=lambda x: x[1], reverse=True)
        return [chromosome for chromosome, score in scored_population[:len(population) // 2]]

    def crossover(self, parents):
        next_generation = []
        ind = 0
        if len(parents) % 2 == 1:
            next_generation.append(copy.deepcopy(parents[0]))
            ind += 1

        for i in range(ind, len(parents), 2):
            child1 = self.make_child(parents[i], parents[i + 1])
            child2 = self.make_child(parents[i + 1], parents[i])
            next_generation.extend([child1, child2, parents[i], parents[i + 1]])

        return next_generation[:self.population_size]

    def make_child(self, parent1, parent2):
        child = copy.deepcopy(parent1)
        parent2_0 = copy.deepcopy(parent2)
        quarter = self.chromosome_length // 4
        half = self.chromosome_length // 2

        child[:quarter] = parent2_0[:quarter]
        child[half:half + quarter] = parent2_0[half:half + quarter]

        return child

    def random_chromosome(self, SEED):
        random.seed(SEED)
        population = []
        for _ in range(self.population_size):
            chromosome = []
            for _ in range(self.chromosome_length):
                chromosome.append(random.choice([True, False]))
            population.append(chromosome)
        return population
