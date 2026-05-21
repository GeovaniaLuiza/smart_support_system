# ==========================================================
# OTIMIZAÇÃO ESTOCÁSTICA — SIMULATED ANNEALING
# ==========================================================
#
# Este módulo implementa o algoritmo meta-heurístico
# Simulated Annealing (Recozimento Simulado).
#
# Objetivo:
# Resolver o problema de alocação de tickets
# para atendentes de forma otimizada.
#
# O algoritmo busca:
#
# ✔ Maximizar satisfação dos clientes
# ✔ Evitar sobrecarga de atendentes
# ✔ Melhorar distribuição de tarefas
#
# Conceitos aplicados:
#
# - Otimização Estocástica
# - Meta-heurísticas
# - Busca combinatória
# - Escalonamento de tarefas
# - Alocação de recursos
#
# ==========================================================



# ==========================================================
# IMPORTAÇÃO DAS BIBLIOTECAS
# ==========================================================

# Biblioteca para geração de números aleatórios
import random

# Biblioteca matemática
#
# Utilizada na função exponencial do algoritmo.
#
import math



# ==========================================================
# CONFIGURAÇÕES DO SISTEMA
# ==========================================================

# Número total de atendentes disponíveis
NUM_ATTENDANTS = 3


# Número máximo de tickets permitidos
# para cada atendente
MAX_TICKETS_PER_ATTENDANT = 4



# ==========================================================
# FUNÇÃO OBJETIVO
# ==========================================================
#
# A função objetivo mede a qualidade de uma solução.
#
# Entrada:
# - solution -> distribuição de tickets
# - satisfactions -> satisfação dos clientes
#
# Objetivo:
# Maximizar satisfação e minimizar sobrecarga.
#
# ==========================================================

def objective(solution, satisfactions):


    # ------------------------------------------------------
    # Variável de pontuação da solução
    # ------------------------------------------------------

    score = 0



    # ------------------------------------------------------
    # Controle da quantidade de tickets
    # por atendente
    # ------------------------------------------------------

    attendant_load = {
        i: 0 for i in range(NUM_ATTENDANTS)
    }



    # ======================================================
    # PROCESSAMENTO DA SOLUÇÃO
    # ======================================================
    #
    # solution:
    # lista onde cada posição representa:
    #
    # ticket -> atendente responsável
    #
    # Exemplo:
    #
    # [0, 1, 2, 0]
    #
    # significa:
    #
    # ticket 0 →