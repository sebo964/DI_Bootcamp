# This challenge is about Biology that will put emphasis on your knowledge of classes, inheritance and polymorphism.

# Build a DNA object. DNA is composed of chromosomes which is itself composed of Genes.
# A Gene is a single value 0 or 1, it can mutate (flip).
# A Chromosome is a series of 10 Genes. It also can mutate, meaning a random number of genes can randomly flip (1/2 chance to flip).
# A DNA is a series of 10 chromosomes, and it can also mutate the same way Chromosomes can mutate.

# Implement these classes as you see fit.

# Create a new class called Organism that accepts a DNA object and an environment parameter that sets the probability for its DNA to mutate.

# Instantiate a number of Organism and let them mutate until one gets to a DNA which is only made of 1s. Then stop and record the number of generations (iterations) it took.
# Write your results in you personal biology research notebook and tell us your conclusion :).

import random


class Gene:
    def __init__(self, value=0):
        self.value = value

    def mutate(self):
        mutation = random.randint(0, 1)
        if mutation == 1:
            self.value = 1
        else:
            self.value = 0


class Chromosome:
    def __init__(self):
        self.genes = [Gene() for i in range(10)]

    def mutate(self):
        for gene in self.genes:
            if random.randint(0, 1) < 1:
                gene.mutate()


class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for i in range(10)]

    def mutate(self):
        for chromosome in self.chromosomes:
            if random.randint(0, 1) < 1:
                chromosome.mutate()


class Organism:
    def __init__(self, dna, mutation_prob):
        self.dna = dna
        self.mutation_prob = mutation_prob
        self.generations = 0

    def mutate(self):
        if random.randint(0, 1) >= self.mutation_prob:
            self.dna.mutate()
        self.generations += 1

    def is_perfect(self):
        for chromosome in self.dna.chromosomes:
            for gene in chromosome.genes:
                if gene.value == 0:
                    return False
        return True


# Instantiate a number of Organism and let them mutate until one gets to a DNA which is only made of 1s.
organisms = Organism(DNA(), 1)

while not organisms.is_perfect():
    organisms.mutate()

# Then stop and record the number of generations (iterations) it took.
print(f"It took", {organisms.generations}, "generations to reach perfection.")
