import dna
import random
import operator
import math

class Population():

    population = []

    def __init__(self, target_string, mutation_rate, max_population):
        self.target_string = target_string
        self.mutation_rate = mutation_rate

        self.population = [dna.DNA(len(self.target_string)) for _ in range(max_population)]

        self.calc_fitness()

        self.matingPool = []
        self._generations = 0
        self._finished = False
        self.perfect = 1

    # Getters / Setters for properties called in object

    @property
    def generations(self):
        return self._generations

    @property
    def finished(self):
        return self._finished
    
    @finished.setter
    def finished(self, value):
        self._finished = value

    # End Getters / Setters

    def calc_fitness(self):
        # Don't use list comprehension for side effects
        # [member.calc_fitness(self.target_string) for member in self.population]
        for member in self.population:
            member.calc_fitness(self.target_string)

    def natural_selection(self):
        self.matingPool.clear()

        max_fitness = max([member.fitness for member in self.population])

        for member in self.population:
            fitness = member.fitness / max_fitness
            self.matingPool += [member] * int(fitness * 10_000)

    def generate(self):
        # Don't use list comprehension for readability
        for i,_ in enumerate(self.population):
            # Child is created by selecting two parents from the mating pool and using genetic crossover
            child = random.choice(self.matingPool).crossover(random.choice(self.matingPool))
            # We then use mutation to introduce small variations to the system, in case the initial
            # random character selection did not bring out the required letters in spaces
            child.mutate(self.mutation_rate)

            self.population[i] = child

        self._generations += 1

    
    """
        Obtain the max_fitness by using the max function on a list of all of the population members'
        fitness values. Then we sort the population by fitness value using the sort method of the 
        list data structure and the operator module. The best_member will then be the last element in the list, 
        since the fitness values were sorted in ascending order.
    """
    def get_fittest(self):

        max_fitness = max([member.fitness for member in self.population])
        self.population.sort(key=operator.attrgetter("fitness"))
        best_member = self.population[-1]
        
        if max_fitness == self.perfect:
            self.finished = True

        return f"{best_member.phrase()}    Fitness : {round(best_member.fitness, 4)}"
    
    def average_fitness(self):
        total_fitness = sum([member.fitness for member in self.population])

        return round(total_fitness / len(self.population), 4)

    """
        Join each phrase and its fitness value with a new line in between for an easy-to-read string
    """
    def get_all_phrases(self):
        return "\n".join([f"{member.phrase()}    Fitness : {round(member.fitness, 4)}" for member in self.population])
