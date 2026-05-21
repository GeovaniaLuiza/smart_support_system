# ==========================================================
# INTERFACE WEB — SISTEMA INTELIGENTE DE ATENDIMENTO
# ==========================================================

import streamlit as st
import random

from nlp.predict import predict_sentiment
from fuzzy.fuzzy_system import evaluate_satisfaction

# ==========================================================
# 🔥 CAMADA III — OTIMIZAÇÃO (SIMULATED ANNEALING)
# ==========================================================
from optimization.simulated_annealing import simulated_annealing


# ==========================================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================================

st.set_page_config(
    page_title="Sistema Inteligente de Atendimento",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Sistema Inteligente de Atendimento ao Cliente")

st.markdown("""
Este sistema analisa mensagens de clientes usando:

- PLN (Naive Bayes)
- Sistema Fuzzy (Mamdani)
- Simulated Annealing (Otimização)
""")


# ==========================================================
# ENTRADAS
# ==========================================================

texto = st.text_area("✍️ Digite a mensagem do cliente:")

tempo_espera = st.slider(
    "⏱️ Tempo de espera (minutos)",
    0, 60, 10
)


# ==========================================================
# BOTÃO PRINCIPAL
# ==========================================================

if st.button("Analisar"):

    if texto.strip() == "":
        st.warning("Digite uma mensagem.")

    else:

        # ==================================================
        # CAMADA I — PLN
        # ==================================================
        sentimento, confianca = predict_sentiment(texto)

        # ==================================================
        # CAMADA II — FUZZY
        # ==================================================
        satisfacao = evaluate_satisfaction(confianca, tempo_espera)

        # ==================================================
        # 🔥 CAMADA III — OTIMIZAÇÃO (S.A.)
        # ==================================================

        # Simula múltiplos tickets baseados na satisfação
        num_tickets = 6

        satisfactions = [
            max(10, min(100, satisfacao + random.randint(-10, 10)))
            for _ in range(num_tickets)
        ]

        # Executa Simulated Annealing
        best_solution, best_score = simulated_annealing(satisfactions)


        # ==================================================
        # RESULTADOS
        # ==================================================

        st.subheader("📊 Resultado")

        col1, col2, col3 = st.columns(3)

        col1.metric("Sentimento", sentimento)

        col2.metric("Confiança", f"{confianca:.2f}")

        col3.metric("Satisfação", f"{satisfacao:.2f}")


        # ==================================================
        # 🔥 RESULTADO DA OTIMIZAÇÃO
        # ==================================================

        st.subheader("⚙️ Otimização de Atendimento (S.A.)")

        st.write("Distribuição de tickets entre atendentes:")

        st.write("📌 Distribuição otimizada:")

        for i, att in enumerate(best_solution):
            st.write(f"Ticket {i} → Atendente {att}")

        st.metric("Score da Otimização", f"{best_score:.2f}")


        # ==================================================
        # INTERPRETAÇÃO
        # ==================================================

        st.subheader("🧠 Interpretação")

        if satisfacao >= 70:
            st.success("Cliente satisfeito 👍")

        elif satisfacao >= 40:
            st.warning("Cliente neutro 😐")

        else:
            st.error("Cliente insatisfeito 😡")