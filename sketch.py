from population import Pupulation

def loop():
    pop = Pupulation(5000)
    pop.create_population()
    for p in pop.population:
        print(p.word)
    pop.fitnesse()
    pop = pop.evolve()
    pop.fitnesse()
    while True:
        pop.add_few_words(2)
        pop = pop.evolve()
        pop.fitnesse()
        for p in pop.population:
            print(p)
            if p.word=="word":
                exit(0)




if __name__ == '__main__':
    loop()