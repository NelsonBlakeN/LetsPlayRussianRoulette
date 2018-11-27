#!/usr/bin/env python3

# HYPOTHESIS
# Play russian roulette with two people.
# If the cylinder is not respun between shots, the odds are 50/50
# If the cylinder is respun between shots, the second person has the better odds of surviving.

import sys
from random import randint


def spin(revolver):
    # Reset revolver
    for b in revolver:
        b = 0

    # Add bullet randomly
    bullet = randint(0, 5)
    revolver[bullet] = 1

def simulate(respin=False):
    # Init revolver
    revolver = [0] * 6

    # Initial revolver spin
    spin(revolver)

    # Start the game
    shot_person_1 = revolver.pop()
    shot_person_2 = revolver.pop()
    while not shot_person_1 and not shot_person_2:
        # While neither person has been shot, shoot again
        if respin:
            # If required, respin.
            revolver = [0] * 6
            spin(revolver)
        shot_person_1 = revolver.pop()

        if respin and not shot_person_1:
            # If required, respin.
            revolver = [0] * 6
            spin(revolver)
        shot_person_2 = revolver.pop()

    return shot_person_1, shot_person_2

def sum_results(results, total):
    total[0] += results[0]
    total[1] += results[1]

if __name__ == "__main__":
    n = None
    if len(sys.argv) is 2:
        n = int(sys.argv[1])
    else:
        n = int(input("Number of simulations: "))
    no_respin_results = [0, 0]
    respin_results = [0, 0]

    for i in range(n):
        # Simulate without respin
        sim_results = simulate(respin=False)
        sum_results(sim_results, no_respin_results)

        # Simulate with respin
        sim_results = simulate(respin=True)
        sum_results(sim_results, respin_results)

    # Calculate probability
    no_respin_chances = [no_respin_results[0]/float(n), no_respin_results[1]/float(n)]
    respin_chances = [respin_results[0]/float(n), respin_results[1]/float(n)]

    print("+---------------------+")
    print("| RESULTS - NO RESPIN |")
    print("+--------+------------+")
    print("| Person |   Chance   |")
    print("|    1   |   {:.2%}   |".format(no_respin_chances[0]))
    print("|    2   |   {:.2%}   |".format(no_respin_chances[1]))
    print("+---------------------+")

    print("+---------------------+")
    print("|   RESULTS - RESPIN  |")
    print("+--------+------------+")
    print("| Person |   Chance   |")
    print("|    1   |   {:.2%}   |".format(respin_chances[0]))
    print("|    2   |   {:.2%}   |".format(respin_chances[1]))
    print("+---------------------+")
