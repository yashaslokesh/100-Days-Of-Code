from population import Population
import time

                    # Whooo Westworld!!
def evolve(target, max_population, mutation_rate):

    population = Population(target, mutation_rate, max_population)

    print(f"\nYour target phrase is {len(target)} characters long")
    print("Starting genetic algorithm loop, press Ctrl+C to interrupt loop and print out current stats\n")

    start_time = time.time()

    try:
        while not population.finished:
            population.natural_selection()
            population.generate()
            population.calc_fitness()
            population.get_fittest()

            if population.generations % 100 == 0:
                print(f"UPDATE-- Generation: {population.generations}\n"
                      f"Best phrase: \'{population.get_fittest()}\'\n")

        end_time = round(time.time() - start_time, 3)

        print(f"""Final generation phrases: \n{population.get_all_phrases()}

    Phrase: {target}
    Phrase finding took {end_time} seconds over {population.generations} generations
    The average fitness by the final generation is {population.average_fitness()}
    The population of each generation was {max_population} with a mutation rate of {mutation_rate}\n""")

    except KeyboardInterrupt:

        end_time = round(time.time() - start_time, 3)

        print(f"""Phrases for generation {population.generations}: \n{population.get_all_phrases()}

    Phrase: {target}
    Closest phrase from this generation: {population.get_fittest()}
    Incomplete Phrase finding took {end_time} seconds over {population.generations} generations
    The average fitness by generation {population.generations} is {population.average_fitness()}
    The population of each generation was {max_population} with a mutation rate of {mutation_rate}\n""")
    
def main():
    target_phrase = input("Input phrase you'd like the genetic algorithm to reach, with only letters, spaces, and any of {.!,?}: ")
    max_population = int(input("Enter a population size for the genetic algorithm: "))
    mutation_rate = float(input("Enter the mutation rate that will be used on your population. Recommended to be <= 0.03, or else the population will have too much randomness: "))

    evolve(target_phrase.strip(),max_population,mutation_rate)

if __name__ == '__main__':
    main()