# ==========================================================
# SISTEMA PRINCIPAL — INTERFACE VIA TERMINAL
# ==========================================================

from nlp.predict import predict_sentiment
from fuzzy.fuzzy_system import evaluate_satisfaction

# ==========================================================
# 🔥 IMPORTAÇÃO DA OTIMIZAÇÃO (NOVO)
# ==========================================================

from optimization.simulated_annealing import simulated_annealing
import random


print("\n=== SISTEMA INTELIGENTE DE ATENDIMENTO ===\n")

while True:

    text = input("Digite a mensagem (ou 'sair'): ")

    if text.lower() == "sair":
        break

    wait_time = int(input("Tempo de espera: "))

    # ======================================================
    # CAMADA I — PLN
    # ======================================================

    sentiment, confidence = predict_sentiment(text)

    # ======================================================
    # CAMADA II — FUZZY
    # ======================================================

    score = evaluate_satisfaction(confidence, wait_time)

    # ======================================================
    # 🔥 CAMADA III — OTIMIZAÇÃO (SIMULATED ANNEALING)
    # ======================================================

    # Simulando múltiplos tickets com base na satisfação
    num_tickets = 6

    satisfactions = [
        max(10, min(100, score + random.randint(-10, 10)))
        for _ in range(num_tickets)
    ]

    # Rodando Simulated Annealing
    best_solution, best_score = simulated_annealing(satisfactions)

    # ======================================================
    # RESULTADOS
    # ======================================================

    print("\n--- RESULTADO ---")

    print("Sentimento:", sentiment)
    print("Confiança:", round(confidence, 2))
    print("Satisfação:", round(score, 2))

    # ======================================================
    # 🔥 RESULTADO DA OTIMIZAÇÃO
    # ======================================================

    print("\n--- OTIMIZAÇÃO DE ATENDIMENTO ---")

    print("Distribuição de tickets (atendentes):")
    print(best_solution)

    print("Score da otimização:", round(best_score, 2))

    print("-----------------\n")