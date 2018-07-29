import random

class DNA():
    
    def __init__(self, data_length):
        self.chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .!,?"
        self.genes = [letter for letter in random.choices(self.chars, k=data_length)]
        self._fitness = 0
    
    def phrase(self):
        return "".join(self.genes)
    
    def calc_fitness(self, target):
        raw_fitness = sum([1 if self.genes[i] == target[i] else 0
                           for i,_ in enumerate(self.genes)])
        self.fitness = raw_fitness / len(target)
    
    @property
    def fitness(self):
        return self._fitness
    
    @fitness.setter
    def fitness(self, value):
        self._fitness = value

    def crossover(self, partner):
        child = DNA(len(self.genes))
        mid = int(random.randrange(len(self.genes)))
        # Keep this parent's character if greater than the midpoint split, otherwise the other parent's
        child.genes = [gene if i > mid else partner.genes[i]
                       for i, gene in enumerate(self.genes)]
        return child

    def mutate(self, rate):
        self.genes = [random.choice(self.chars) if random.random() < rate else gene
                      for gene in self.genes]
        return self