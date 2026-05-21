# ==========================================================
# INTERFACE WEB — SISTEMA INTELIGENTE DE ATENDIMENTO
# ==========================================================
#
# Este módulo implementa a interface gráfica do sistema
# utilizando Streamlit.
#
# Objetivo:
# Permitir interação amigável entre usuário e sistema
# inteligente através de uma aplicação web.
#
# O sistema integra:
#
# ✔ PLN com Naive Bayes
# ✔ Sistema de Inferência Fuzzy
# ✔ Tomada de decisão inteligente
#
# Fluxo do sistema:
#
# Usuário
#    ↓
# Mensagem textual
#    ↓
# Classificação de sentimento
#    ↓
# Inferência fuzzy
#    ↓
# Nível de satisfação
#
# ==========================================================



# ==========================================================
# IMPORTAÇÃO DAS BIBLIOTECAS
# ==========================================================

# Biblioteca responsável pela interface web
import streamlit as st


# Função responsável pela análise de sentimentos
#
# Camada I — PLN
#
from nlp.predict import predict_sentiment


# Função responsável pela inferência fuzzy
#
# Camada II — Sistema Fuzzy
#
from fuzzy.fuzzy_system import evaluate_satisfaction



# ==========================================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================================
#
# Define:
# - título da aba
# - ícone
# - layout
#
# ==========================================================

st.set_page_config(
    page_title="Sistema Inteligente de Atendimento",
    page_icon="🤖",
    layout="centered"
)



# ==========================================================
# TÍTULO PRINCIPAL
# ==========================================================

st.title("🤖 Sistema Inteligente de Atendimento ao Cliente")



# ==========================================================
# DESCRIÇÃO DO SISTEMA
# ==========================================================
#
# Explica as tecnologias utilizadas no projeto.
#
# ==========================================================

st.markdown("""
Este sistema analisa mensagens de clientes usando:

- PLN (Naive Bayes)
- Sistema Fuzzy (Mamdani)
- Inferência de satisfação
""")



# ==========================================================
# ENTRADAS DO USUÁRIO
# ==========================================================
#
# Nesta seção o usuário fornece os dados necessários
# para análise.
#
# ==========================================================



# ----------------------------------------------------------
# CAMPO DE TEXTO
# ----------------------------------------------------------
#
# O usuário digita uma mensagem textual.
#
# Exemplo:
# "O atendimento foi excelente"
#
# text_area():
# cria uma caixa de texto multilinha.
#
# ----------------------------------------------------------

texto = st.text_area("✍️ Digite a mensagem do cliente:")



# ----------------------------------------------------------
# SLIDER DO TEMPO DE ESPERA
# ----------------------------------------------------------
#
# Entrada numérica utilizada pelo sistema fuzzy.
#
# Intervalo:
# 0 até 60 minutos
#
# slider():
# cria uma barra deslizante interativa.
#
# ----------------------------------------------------------

tempo_espera = st.slider(
    "⏱️ Tempo de espera (minutos)",
    0, 60, 10
)



# ==========================================================
# BOTÃO DE EXECUÇÃO
# ==========================================================
#
# Quando o usuário clicar em "Analisar",
# o sistema executará todas as camadas de IA.
#
# ==========================================================

if st.button("Analisar"):



    # ------------------------------------------------------
    # VALIDAÇÃO DA ENTRADA
    # ------------------------------------------------------
    #
    # Verifica se o usuário digitou algum texto.
    #
    # strip():
    # remove espaços vazios.
    #
    # ------------------------------------------------------

    if texto.strip() == "":

        st.warning("Digite uma mensagem.")



    else:


        # ==================================================
        # CAMADA I — PLN + NAIVE BAYES
        # ==================================================
        #
        # A função predict_sentiment():
        #
        # 1) pré-processa o texto
        # 2) aplica TF-IDF
        # 3) utiliza Naive Bayes
        # 4) retorna:
        #
        # sentimento
        # confiança
        #
        # ==================================================

        sentimento, confianca = predict_sentiment(texto)



        # ==================================================
        # CAMADA II — SISTEMA FUZZY
        # ==================================================
        #
        # O sistema fuzzy recebe:
        #
        # - confiança do classificador
        # - tempo de espera
        #
        # E realiza:
        #
        # ✔ fuzzificação
        # ✔ aplicação das regras fuzzy
        # ✔ inferência Mamdani
        # ✔ defuzzificação
        #
        # Retornando:
        #
        # → nível de satisfação
        #
        # ==================================================

        satisfacao = evaluate_satisfaction(
            confianca,
            tempo_espera
        )



        # ==================================================
        # RESULTADOS
        # ==================================================
        #
        # Exibição das informações calculadas.
        #
        # ==================================================

        st.subheader("📊 Resultado")



        # --------------------------------------------------
        # Organização em colunas
        # --------------------------------------------------

        col1, col2, col3 = st.columns(3)



        # --------------------------------------------------
        # Resultado da classificação
        # --------------------------------------------------

        col1.metric("Sentimento", sentimento)



        # --------------------------------------------------
        # Confiança probabilística
        # --------------------------------------------------

        col2.metric(
            "Confiança",
            f"{confianca:.2f}"
        )



        # --------------------------------------------------
        # Resultado fuzzy
        # --------------------------------------------------

        col3.metric(
            "Satisfação",
            f"{satisfacao:.2f}"
        )



        # ==================================================
        # INTERPRETAÇÃO DOS RESULTADOS
        # ==================================================
        #
        # O sistema converte o valor numérico de satisfação
        # em uma interpretação textual.
        #
        # Regras:
        #
        # ≥ 70 → satisfeito
        # ≥ 40 → neutro
        # < 40 → insatisfeito
        #
        # ==================================================

        st.subheader("🧠 Interpretação")



        # --------------------------------------------------
        # Cliente satisfeito
        # --------------------------------------------------

        if satisfacao >= 70:

            st.success("Cliente satisfeito 👍")



        # --------------------------------------------------
        # Cliente neutro
        # --------------------------------------------------

        elif satisfacao >= 40:

            st.warning("Cliente neutro 😐")



        # --------------------------------------------------
        # Cliente insatisfeito
        # --------------------------------------------------

        else:

            st.error("Cliente insatisfeito 😡")



# ==========================================================
# IMPORTÂNCIA NO PROJETO
# ==========================================================
#
# Este módulo representa a interface final do sistema.
#
# Ele conecta todas as camadas desenvolvidas:
#
# ✔ Interface Homem-Máquina
# ✔ PLN
# ✔ Naive Bayes
# ✔ Sistema Fuzzy
# ✔ Tomada de decisão
#
# Benefícios:
#
# - facilidade de uso
# - visualização em tempo real
# - interação intuitiva
#
# Relação com o trabalho:
#
# ✔ Inteligência Artificial
# ✔ PLN
# ✔ Inferência Fuzzy
# ✔ Sistemas Inteligentes
# ✔ Tratamento de incerteza
#
# ==========================================================