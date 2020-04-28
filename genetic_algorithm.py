import sys
import math
import random

POP_SIZE = 100
MUTATION_RATE = 0.01
TARGET = "HELLO WORLD"

def get_random_char():
    num = random.randint(64, 90)
    if (num == 64):
        num = 32
    return chr(num)

def get_random_string(length):
    string = ""
    for i in range(length):        
        string += get_random_char()
    return string

def mutate(string):
    mutated_string = ""
    for i in range(len(string)):
        if (random.uniform(0, 1) < MUTATION_RATE):
            mutated_string += get_random_char()
        else:
            mutated_string += string[i]
    return mutated_string

def get_fitness_score(elem):
    score = 0
    for i in range(len(elem)):
        if (elem[i] == TARGET[i]):
            score += 1
    score *= score
    return score

def init_pop():
    pop = []
    for i in range(POP_SIZE):
        string = get_random_string(len(TARGET))
        string = mutate(string)
        elem = [string]
        elem.append(get_fitness_score(string))
        pop.append(elem)
    return pop

def pick_parent(pop):
    score = 0
    accept = 0
    for elem in pop:
        score += elem[1]
    if score < 1:
        exit("no element in population is fit enough")
    while accept == 0:
        parent = pop[random.randint(0, len(pop) - 1)]
        acceptance = random.randint(0, score)
        if acceptance < parent[1]:
            accept = 1
    return parent
    
def new_generation(pop):
    new_pop = []
    while (len(new_pop) != POP_SIZE):
        p1 = pick_parent(pop)
        p2 = pick_parent(pop)
        child = ""
        for i in range (0, len(p1[0])):
            child += p1[0][i] if random.randint(1, 2) == 1 else p2[0][i]
        child = mutate(child)
        print(child)
        if (child == TARGET):
            print("\nLadies and gents, it took us " + str(gen_count) + " generations but...")
            exit("We gotem")
        new_pop.append([child, get_fitness_score(child)])
    return new_pop

pop = init_pop()
gen_count = 1
while True:
    gen_count += 1
    print("Starting reproduction of gen " + str(gen_count))
    pop = new_generation(pop)