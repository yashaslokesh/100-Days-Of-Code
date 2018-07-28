import population
import time

target = "Anthony Ford is alive" # Whoo Westworld!
mutation_rate = 0.01
max_population = 300

population = population.Population(target, mutation_rate, max_population)

start_time = time.time()

try:
    while not population.finished:
# for i in range(0, 1):
        population.naturalSelection()
        population.generate()
        population.calcFitness()
        population.getFittest()
except KeyboardInterrupt:
    print(f"Phrases for generation {population.generations}: \n{population.getAllPhrases()}")
    print(f"Phrase: {target}")
    print(f"Best phrase from this generation was: {population.getFittest()}")

# print(f"Generations: {population.generations}, Avg. Fitness: {population.averageFitness()}")

end_time = time.time() - start_time

print(f"Final generation phrases: \n{population.getAllPhrases()}")
print(f"Phrase: {target}")
print(f"Phrase finding took {end_time} seconds over {population.generations} generations")
print(f"The average fitness by the final generation is {population.averageFitness()}")
print(f"The population of each generation was {max_population}, with a mutation rate of {mutation_rate}")
    
