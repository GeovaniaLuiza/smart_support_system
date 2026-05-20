import streamlit as st

from nlp.predict import predict_sentiment
from fuzzy.fuzzy_system import evaluate_satisfaction

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
- Inferência de satisfação
""")

# -------------------------
# ENTRADAS
# -------------------------

texto = st.text_area("✍️ Digite a mensagem do cliente:")

tempo_espera = st.slider(
    "⏱️ Tempo de espera (minutos)",
    0, 60, 10
)

# -------------------------
# BOTÃO
# -------------------------

if st.button("Analisar"):

    if texto.strip() == "":
        st.warning("Digite uma mensagem.")
    else:

        sentimento, confianca = predict_sentiment(texto)

        satisfacao = evaluate_satisfaction(confianca, tempo_espera)

        # -------------------------
        # RESULTADOS
        # -------------------------

        st.subheader("📊 Resultado")

        col1, col2, col3 = st.columns(3)

        col1.metric("Sentimento", sentimento)
        col2.metric("Confiança", f"{confianca:.2f}")
        col3.metric("Satisfação", f"{satisfacao:.2f}")

        # -------------------------
        # INTERPRETAÇÃO
        # -------------------------

        st.subheader("🧠 Interpretação")

        if satisfacao >= 70:
            st.success("Cliente satisfeito 👍")
        elif satisfacao >= 40:
            st.warning("Cliente neutro 😐")
        else:
            st.error("Cliente insatisfeito 😡")