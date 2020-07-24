# dice-rolling program
# throw dice to get a random output
# often throw 2, who knows?
# dice are fair if every number is equally likely
# dice: cubes with dots, representing numbers 1-6
import random
import math
import matplotlib.pyplot as plt

# input: number of sides on a die
# a function which outputs an integer 1-6
def generate_random(num_sides):
    return random.randint(1, num_sides)

# input: number of dice to roll, number of sides per die
# output: outcome of the rolls
def roll(num_dice=1, num_sides=6):
    outcome = [ ]
    for i in range(num_dice):
        outcome.append( generate_random(num_sides) )
    return outcome

def stdev(data):
    mean = sum(data)/len(data)
    mse = [(x - mean)**2 for x in data]
    return math.sqrt(sum(mse) / len(data))

# compute standard deviation of dice and plot error bars
def fairness(num_tests=1000000, num_sides=6):
    outcomes = [roll(num_tests, num_sides).count(x) for x in range(1, num_sides+1)]

    sd = stdev(outcomes)

    fig, ax = plt.subplots()
    ax.bar(x=range(1, len(outcomes) +1), yerr=sd, height=outcomes, align='center', alpha=0.5, ecolor='black', capsize=10)
    ax.set_xlabel("Side")
    ax.set_ylabel("# outcomes")
    ax.set_xticks(range(1, len(outcomes) + 1))
    ax.set_xticklabels(range(1, len(outcomes) + 1))
    ax.set_title("Fairness")

    plt.tight_layout()
    plt.show()

    return sd