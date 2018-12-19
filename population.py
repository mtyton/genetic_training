from genetic import DNA
import random

class Pupulation:
    def __init__(self, population_size):
        self.pupulation_size = population_size
        self.population = []
        self.basic_word = 'word'
        self.mutation_rate = 0.4
        self.max_score = 0

    def __str__(self):
        return self.pupulation_size

    def create_population(self):
        """
        Simply creates a pupulation of words
        :return:
        """
        for i in range(0, self.pupulation_size):
            dna = DNA()
            dna.randomize(self.basic_word)
            self.population.append(dna)

    def add_few_words(self, number):
        """
        simply adds a given number of words to a population
        :return:
        """
        for i in range(number):
            dna = DNA()
            dna.randomize(self.basic_word)
            self.population.append(dna)

    def fitnesse(self):
        """
        invokes fitness method for every word
        :return:
        """
        for pop in self.population:
            pop.count_fitness(self.basic_word)

    def evolve(self):
        """
        evolves our words, cross them over and mutate them
        :return:
        """
        self.find_max_fitnesse()
        chosen_to_evolve = self.choose_to_evolve()
        new_population = Pupulation(len(chosen_to_evolve))
        for iterator, element in enumerate(chosen_to_evolve):
            if iterator + 1 == len(chosen_to_evolve):
                break
            dna = element.crossover(chosen_to_evolve[iterator].word)
            dna.mutate(0.02)
            new_population.population.append(dna)

        self.begin_mutation(new_population)
        random.shuffle(new_population.population)
        return new_population

    def find_max_fitnesse(self):
        """
        gives us the max fitnesse of this population
        :return:
        """
        self.max_score = 0
        for pop in self.population:
            if self.max_score<pop.score:
                self.max_score = pop.score

    def choose_to_evolve(self):
        """
        choses words to evolve
        :return:
        """
        chosen_to_evolve = []
        best = Pupulation.select_best_samples(self.population, self.max_score)
        luckers = Pupulation.select_lucky_few(self.population, self.max_score)
        for b in best:
            chosen_to_evolve.append(b)
        for l in luckers:
            chosen_to_evolve.append(l)
        random.shuffle(chosen_to_evolve)
        return chosen_to_evolve

    @staticmethod
    def select_best_samples(pop, max):
        """
        returns words with best fitness
        """
        best = []
        for p in pop:
            if p.score >= max-1:
                best.append(p)
        return best

    @staticmethod
    def select_lucky_few(pop, max):
        """
        returns few random words
        """
        random.seed()
        luckers = []
        for p in range(10):
            numb = random.randrange(len(pop))
            if pop[numb].score < max-1:
                luckers.append((pop[numb]))
        return luckers


    def begin_mutation(self, new_population):
        """
        Invokes mutating method
        """
        for new in new_population.population:
            new.mutate(self.mutation_rate)