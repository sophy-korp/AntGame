from Evolution import Evolution
import random


class Optimizer:
    # эти константы НЕ желательно менять:
    POPULATION_SIZE = 5000
    ITERATIONS = 10
    CHROMOSOME_LENGTH = 83
    SEED = 39

    @staticmethod
    def optimize(field):
        evolut = Evolution(field, Optimizer.CHROMOSOME_LENGTH, Optimizer.POPULATION_SIZE)

        population = evolut.random_chromosome(Optimizer.SEED)
        for _ in range(Optimizer.ITERATIONS):
            # создайте здесь своего муравья используя реализованные методы в Evolution
            # Возможный вариант реализации:
            # Проведите несколько мутаций с каждой особью
            # Сделайте селекцию
            # Сделайте кроссовер
            pass

        # После последней итерации выбираем наилучшего муравья (наилучшую последовательность хромосом)
        final_population = evolut.select(population)
        # наилучшая последовательность хромосом находится в начале отсортированного списка
        return final_population[0]
