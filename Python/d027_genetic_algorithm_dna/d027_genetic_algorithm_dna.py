import random

class DNA():

    def __init__(self, data_length):
        self.chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !,."
        self.genes = [letter for letter in random.choices(self.chars, k=data_length)]
    
    def calc_fitness(self, target):
        result = 0
        for i in range(len(self.genes)):
            result += 1 if self.genes[i] == target[i] else 0
        self.fitness = result / len(target)

    def crossover(self, partner):
        child = DNA(len(self.genes))

        mid = int(random.randrange(len(self.genes)))

        for gene in range(len(self.genes)):
            child.genes[gene] = self.genes[gene] if gene > mid else partner.genes[gene]
        return child

    def mutate(self, rate):
        for gene in range(len(self.genes)):
            if random.randrange(2) < rate:
                self.genes[gene] = random.choice(self.chars)