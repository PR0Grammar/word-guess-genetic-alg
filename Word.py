import random, string

class Word:
    def __init__(self, word):
        self.chars = list(word)
        self.fitness = 0
    

    def get_fitness(self, target):
        fitness_lvl = 0
        for i in range(len(target)):
            if(target[i] == self.chars[i]):
                fitness_lvl += 1
        self.fitness = float(fitness_lvl) / len(target)

    def mutate(self, mutationRate):
        alleles = string.printable

        for i in range(len(self.chars)):
            if(random.random() < mutationRate):
                self.chars[i] = random.choice(alleles)

    def crossover(self, mate):
        childEncoding = ""
        midpoint = random.randint(0, len(self.chars) - 1)

        for i in range(len(self.chars)):
            if(i < midpoint):
                childEncoding += self.chars[i]
            else:
                childEncoding += mate.chars[i]
        
        return Word(childEncoding)

    def get_encoding(self):
        return ''.join(self.chars)