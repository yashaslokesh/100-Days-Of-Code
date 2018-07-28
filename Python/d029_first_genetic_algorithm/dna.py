import random

class DNA():
    
    def __init__(self, data_length):
        self.chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .!,?"
        self.genes = [letter for letter in random.choices(self.chars, k=data_length)]
        self._fitness = 0
    
    def phrase(self):
        return "".join(self.genes)
    
    def calc_fitness(self, target):
        result = 0
        for i in range(len(self.genes)):
            result += 1 if self.genes[i] == target[i] else 0
        self._fitness = result / len(target)
    
    @property
    def fitness(self):
        return self._fitness

    def crossover(self, partner):

        child = DNA(len(self.genes))
        mid = int(random.randrange(len(self.genes)))

        for i,gene in enumerate(self.genes):
            child.genes[i] = gene if i > mid else partner.genes[i]
        return child

    def mutate(self, rate):
        for i,_ in enumerate(self.genes):
            if random.random() < rate:
                self.genes[i] = random.choice(self.chars)