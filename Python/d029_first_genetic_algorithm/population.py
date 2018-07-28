import dna
import random

class Population():

    population = []

    def __init__(self, target_string, mutation_rate, max_population):
        self.target_string = target_string
        self.mutation_rate = mutation_rate

        self.population = [dna.DNA(len(self.target_string)) for _ in range(max_population)]

        self.calcFitness()

        self.matingPool = []
        self._generations = 0
        self._finished = False
        self.perfect = 1

    # Getters / Setters for properties called in object

    @property
    def generations(self):
        return self._generations
    
    @generations.setter
    def generations(self, increment):
        self._generations += increment

    @property
    def finished(self):
        return self._finished
    
    @finished.setter
    def finished(self, value):
        self._finished = value

    # End Getters / Setters

    def calcFitness(self):
        for member in self.population:
            member.calc_fitness(self.target_string)

    def naturalSelection(self):
        self.matingPool.clear()
        max_fitness = 0
        for member in self.population:
            max_fitness = max(member.fitness, max_fitness)
        for member in self.population:
            fitness = member.fitness / max_fitness
            self.matingPool += [member] * int(fitness * 100)

    def generate(self):
        for i,_ in enumerate(self.population):
            parent_one = random.choice(self.matingPool)
            parent_two = random.choice(self.matingPool)

            child = parent_one.crossover(parent_two)
            child.mutate(self.mutation_rate)

            self.population[i] = child

        self.generations += 1

    def getFittest(self):
        max_fitness = 0
        for member in self.population:
            if member.fitness > max_fitness:
                # best_index = index
                best_member = member
                max_fitness = member.fitness
        
        if max_fitness == self.perfect:
            self.finished = True

        return best_member.phrase()
    
    def averageFitness(self):
        total = 0
        for member in self.population:
            total += member.fitness
        return total / len(self.population)

    def getAllPhrases(self):
        return "\n".join([f"{member.phrase()}    Fitness : {round(member.fitness, 3)}" for member in self.population])
    


    

    


            

        


