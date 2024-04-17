import time
from numpy import asarray,exp,sqrt,cos,e,pi
from numpy.random import randn,rand,seed
import random

""" Generate a large number of 8-puzzles instances and solve them (where pos-
sible) by hill climbing (steepest-ascent and first-choice variants), hill climbing with ran-
dom restart, and simulated annealing. Measure the search cost and percentage of solved
problems and graph these against the optimal solution cost. Comment on your results. """


MAX_RESTARTS_ALLOWED = 5


def generate_random_8_instance_puzzle():
    """ Returns a 8-instance puzzle - of which may not be solvable """

    puzzle = list(range(1, 9))
    random.shuffle(puzzle)

    return puzzle


def ackley(v):
    x, y = v
    return -20.0 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2))) - exp(0.5 * (cos(2 * pi * x) + cos(2 * pi * y))) + e + 20

def in_bnds(point, bounds):
    inBounds = True
    for p in range(len(bounds)):
        if point[p] < bounds[p, 0] or point[p] > bounds[p, 1]:
            inBounds=False
    return inBounds


def random_restart(objective, bnds, n_iters, step_size, MAX_RESTARTS_ALLOWED):
    i = 0
    best_score = 0
    best_sol = None

    while i < MAX_RESTARTS_ALLOWED:
        temp_sol, temp_score = hillclimbing(objective, bnds, n_iters, step_size)
        if i == 0:
            best_score = temp_score
            best_sol = temp_sol

        if temp_score < best_score:
            best_score = temp_score
            best_sol = temp_sol

        time.sleep(1)
        i += 1
        print(i)

    return best_sol, best_score


def hillclimbing(objective, bnds, n_iters, step_size):
	# generate starting point
    sol = None
    while sol is None or not in_bnds(sol, bnds):
        sol = bnds[:, 0] + rand(len(bnds)) * (bnds[:, 1] - bnds[:, 0])

    # evaluate starting point
    sol_eval = objective(sol)


    # run the hill climb
    for i in range(n_iters):
        candidate = None
        while candidate is None or not in_bnds(candidate, bnds):
            candidate = sol + randn(len(bnds)) * step_size
        candidte_eval = objective(candidate)
		
        if candidte_eval <= sol_eval:
            sol, sol_eval = candidate, candidte_eval
            #print(f"{i} f({sol}) = {sol_eval}" )

    return [sol, sol_eval]


def run_standard():
    # seed the random number generator
    seed(1)
    #range to search within 
    bounds = asarray([[-5.0, 5.0], [-5.0, 5.0]])
    n_iter = 500
    # define the maximum step size
    step_size = 0.05

    best, score = hillclimbing(ackley, bounds, n_iter, step_size)
    print("Hill Climbing Complete!")
    print(f"f({best}) = {score}")

    print("\n Random Restart best values:\n")
    best_point, best_score = random_restart(ackley, bounds, n_iter, step_size, MAX_RESTARTS_ALLOWED)
    print("f({}{} = {})", best_point[0], best_point[1], best_score)

if __name__ == "__main__":
    run_standard()
