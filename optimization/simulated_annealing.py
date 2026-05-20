import random
import math

NUM_ATTENDANTS = 3
MAX_TICKETS_PER_ATTENDANT = 4

def objective(solution, satisfactions):

    score = 0

    attendant_load = {
        i: 0 for i in range(NUM_ATTENDANTS)
    }

    for i, attendant in enumerate(solution):

        attendant_load[attendant] += 1

        score += satisfactions[i]

    # Penalidade por sobrecarga
    penalty = 0

    for attendant, load in attendant_load.items():

        if load > MAX_TICKETS_PER_ATTENDANT:

            penalty += (load - MAX_TICKETS_PER_ATTENDANT) * 20

    return score - penalty

def random_neighbor(solution):

    neighbor = solution.copy()

    idx = random.randint(0, len(solution)-1)

    neighbor[idx] = random.randint(
        0,
        NUM_ATTENDANTS - 1
    )

    return neighbor

def simulated_annealing(satisfactions):

    n = len(satisfactions)

    current_solution = [
        random.randint(0, NUM_ATTENDANTS - 1)
        for _ in range(n)
    ]

    current_cost = objective(
        current_solution,
        satisfactions
    )

    best_solution = current_solution.copy()
    best_cost = current_cost

    temperature = 100

    cooling_rate = 0.95

    while temperature > 1:

        neighbor = random_neighbor(current_solution)

        neighbor_cost = objective(
            neighbor,
            satisfactions
        )

        delta = neighbor_cost - current_cost

        if delta > 0:

            current_solution = neighbor
            current_cost = neighbor_cost

        else:

            probability = math.exp(
                delta / temperature
            )

            if random.random() < probability:

                current_solution = neighbor
                current_cost = neighbor_cost

        if current_cost > best_cost:

            best_solution = current_solution.copy()
            best_cost = current_cost

        temperature *= cooling_rate

    return best_solution, best_cost