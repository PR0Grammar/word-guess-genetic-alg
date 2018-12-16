from Word import Word
import random, string, sys

class NaturalSelect:
    def __init__(self, goal = None):
        self.population = []
        self.goal = goal
        self.highest_fitness = 0
        self.generations = 0
        self.fittest_gene = None

        self.get_random_goal()
        self.get_init_population()
        self.get_population_fitness()

    def get_random_goal(self):
        if(self.goal is not None):
            return

        gene = ""
        alleles = string.printable
        for i in range(18):
            gene += random.choice(alleles)
        
        self.goal = gene

    def get_init_population(self):
        if(len(self.goal) == 0):
            print("No goal set.")
            return

        alleles = string.printable
        for i in range(1000):
            gene = ""
            for j in range(len(self.goal)):
                gene += random.choice(alleles)
            self.population.append(Word(gene))
        
        self.generations += 1
    
    def get_population_fitness(self):
        new_gen_fitness = -1
        fittest_gene = None
        for gene in self.population:
            gene.get_fitness(self.goal)
            if(gene.fitness > new_gen_fitness):
                new_gen_fitness = gene.fitness
                fittest_gene = gene
        self.highest_fitness = new_gen_fitness
        self.fittest_gene = fittest_gene
    

    def next_gen(self):
        childs = []
        matingPool = []
        mutateRate = 0.01

        for gene in self.population:
            for i in range(int(gene.fitness * 100)):
                matingPool.append(gene)
        
        for i in range(len(self.population)):
            parentOne = matingPool[random.randint(0, len(matingPool) - 1)]
            parentTwo = matingPool[random.randint(0, len(matingPool) - 1)]

            child = parentOne.crossover(parentTwo)
            child.mutate(mutateRate)

            childs.append(child)

        self.population = childs
        self.generations += 1
        


    def fittest_found(self):
        return self.highest_fitness == 1.0

    def get_fittest_gene(self):
        return self.fittest_gene.get_encoding()

    def get_total_gene_count(self):
        return self.generations * 1000


def main():
    simulation = None

    if(len(sys.argv) > 1):
        simulation = NaturalSelect(sys.argv[1])
    else:
        simulation = NaturalSelect()

    while not simulation.fittest_found():
        simulation.next_gen()
        simulation.get_population_fitness()
        print(simulation.get_fittest_gene())
    
    print('GOAL: ' + simulation.goal)
    print('GENERATION COUNT: ' + str(simulation.generations))
    print('TOTAL GENES CREATED: ' + str(simulation.get_total_gene_count()))
    

if __name__ == '__main__':
    main()