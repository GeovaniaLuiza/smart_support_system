# ==========================================================
# OTIMIZAÇÃO ESTOCÁSTICA — SIMULATED ANNEALING
# ==========================================================
#
# Este módulo implementa o algoritmo Simulated Annealing
# aplicado à otimização da alocação de tickets.
#
# Agora o sistema é integrado ao resultado do Fuzzy,
# utilizando satisfactions reais geradas pelo sistema.
#
# ==========================================================

import random
import math


# ==========================================================
# CONFIGURAÇÕES DO SISTEMA
# ==========================================================

NUM_ATTENDANTS = 3
MAX_TICKETS_PER_ATTENDANT = 4


# ==========================================================
# FUNÇÃO OBJETIVO (MELHORADA)
# ==========================================================
#
# Agora a função considera:
#
# ✔ satisfação real dos tickets
# ✔ penalização por sobrecarga
# ✔ equilíbrio de carga entre atendentes
#
# ==========================================================

def objective(solution, satisfactions):

    score = 0

    attendant_load = {i: 0 for i in range(NUM_ATTENDANTS)}

    # ------------------------------------------------------
    # Soma satisfação e conta carga por atendente
    # ------------------------------------------------------

    for i, attendant in enumerate(solution):

        attendant_load[attendant] += 1
        score += satisfactions[i]

    # ------------------------------------------------------
    # Penalidade por sobrecarga
    # ------------------------------------------------------

    penalty = 0

    for attendant, load in attendant_load.items():

        if load > MAX_TICKETS_PER_ATTENDANT:

            penalty += (load - MAX_TICKETS_PER_ATTENDANT) * 25

    # ------------------------------------------------------
    # Penalidade adicional por desbalanceamento
    # ------------------------------------------------------

    loads = list(attendant_load.values())
    imbalance = max(loads) - min(loads)

    penalty += imbalance * 5

    return score - penalty


# ==========================================================
# GERAÇÃO DE VIZINHO (EXPLORAÇÃO LOCAL)
# ==========================================================

def random_neighbor(solution):

    neighbor = solution.copy()

    idx = random.randint(0, len(solution) - 1)

    neighbor[idx] = random.randint(0, NUM_ATTENDANTS - 1)

    return neighbor


# ==========================================================
# ALGORITMO SIMULATED ANNEALING
# ==========================================================
#
# Agora adaptado para integração com:
#
# ✔ Streamlit
# ✔ Sistema Fuzzy
# ✔ Satisfação real dos clientes
#
# ==========================================================

def simulated_annealing(satisfactions):

    n = len(satisfactions)

    # ------------------------------------------------------
    # Solução inicial aleatória
    # ------------------------------------------------------

    current_solution = [
        random.randint(0, NUM_ATTENDANTS - 1)
        for _ in range(n)
    ]

    current_cost = objective(current_solution, satisfactions)

    best_solution = current_solution.copy()
    best_cost = current_cost


    # ------------------------------------------------------
    # Parâmetros do algoritmo
    # ------------------------------------------------------

    temperature = 120
    cooling_rate = 0.94


    # ======================================================
    # LOOP PRINCIPAL DO SA
    # ======================================================

    while temperature > 1:

        neighbor = random_neighbor(current_solution)

        neighbor_cost = objective(neighbor, satisfactions)

        delta = neighbor_cost - current_cost


        # --------------------------------------------------
        # Regra de aceitação
        # --------------------------------------------------

        if delta > 0:

            current_solution = neighbor
            current_cost = neighbor_cost

        else:

            probability = math.exp(delta / temperature)

            if random.random() < probability:

                current_solution = neighbor
                current_cost = neighbor_cost


        # --------------------------------------------------
        # Atualiza melhor solução
        # --------------------------------------------------

        if current_cost > best_cost:

            best_solution = current_solution.copy()
            best_cost = current_cost


        # --------------------------------------------------
        # Resfriamento
        # --------------------------------------------------

        temperature *= cooling_rate


    return best_solution, best_cost