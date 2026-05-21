# ==========================================================
# CAMADA I — PROCESSAMENTO DE LINGUAGEM NATURAL (PLN)
# ==========================================================
#
# Este módulo é responsável pela predição de sentimentos
# utilizando um classificador Naive Bayes treinado
# previamente.
#
# Objetivo:
# Classificar mensagens de clientes em:
#
# - Positivo
# - Negativo
# - Neutro
#
# O modelo utiliza técnicas de PLN para transformar
# texto não estruturado em dados processáveis.
#
# Conceitos aplicados:
# - Processamento de Linguagem Natural (PLN)
# - Pré-processamento textual
# - Machine Learning
# - Classificação supervisionada
# - Naive Bayes
#
# ==========================================================



# ==========================================================
# IMPORTAÇÃO DAS BIBLIOTECAS
# ==========================================================

# Biblioteca utilizada para carregar o modelo treinado
import pickle


# Função responsável pelo pré-processamento textual
#
# Etapas realizadas:
# - tokenização
# - remoção de stop words
# - stemming/lemmatização
# - limpeza textual
#
from nlp.preprocess import preprocess_text



# ==========================================================
# CARREGAMENTO DO MODELO TREINADO
# ==========================================================
#
# O modelo foi treinado previamente utilizando um
# dataset de sentimentos.
#
# O arquivo sentiment_model.pkl armazena:
#
# - modelo Naive Bayes treinado
# - parâmetros aprendidos
#
# O modelo é carregado em memória para realizar
# novas previsões.
#
# ==========================================================

with open("nlp/sentiment_model.pkl", "rb") as f:

    model = pickle.load(f)



# ==========================================================
# FUNÇÃO DE PREDIÇÃO DE SENTIMENTO
# ==========================================================
#
# Entrada:
# - texto digitado pelo usuário
#
# Saída:
# - classe do sentimento
# - confiança/probabilidade da previsão
#
# Fluxo da função:
#
# 1) Pré-processamento do texto
# 2) Vetorização implícita no modelo
# 3) Classificação com Naive Bayes
# 4) Cálculo das probabilidades
#
# ==========================================================

def predict_sentiment(text):


    # ------------------------------------------------------
    # ETAPA 1 — PRÉ-PROCESSAMENTO
    # ------------------------------------------------------
    #
    # O texto é tratado para remover ruídos e melhorar
    # a qualidade da classificação.
    #
    # Exemplos de processamento:
    # - conversão para minúsculas
    # - remoção de pontuação
    # - remoção de stop words
    # - stemming
    #
    # ------------------------------------------------------

    processed = preprocess_text(text)



    # ------------------------------------------------------
    # ETAPA 2 — CLASSIFICAÇÃO
    # ------------------------------------------------------
    #
    # O modelo Naive Bayes prevê a classe do sentimento.
    #
    # Possíveis saídas:
    # - positivo
    # - negativo
    # - neutro
    #
    # [0] é utilizado porque a previsão retorna uma lista.
    #
    # ------------------------------------------------------

    prediction = model.predict([processed])[0]



    # ------------------------------------------------------
    # ETAPA 3 — PROBABILIDADES
    # ------------------------------------------------------
    #
    # O modelo calcula a probabilidade de cada classe.
    #
    # Exemplo:
    #
    # [0.10, 0.80, 0.10]
    #
    # indicando:
    # 10% negativo
    # 80% positivo
    # 10% neutro
    #
    # ------------------------------------------------------

    probabilities = model.predict_proba([processed])[0]



    # ------------------------------------------------------
    # ETAPA 4 — CONFIANÇA DA PREVISÃO
    # ------------------------------------------------------
    #
    # Seleciona a maior probabilidade dentre as classes.
    #
    # Esse valor será utilizado posteriormente
    # pelo sistema fuzzy.
    #
    # ------------------------------------------------------

    confidence = max(probabilities)



    # ------------------------------------------------------
    # RETORNO DA FUNÇÃO
    # ------------------------------------------------------
    #
    # prediction -> sentimento previsto
    # confidence -> nível de confiança da previsão
    #
    # ------------------------------------------------------

    return prediction, confidence



# ==========================================================
# INTEGRAÇÃO COM O PROJETO
# ==========================================================
#
# Esta camada representa a fase de percepção do sistema
# inteligente.
#
# O classificador Naive Bayes interpreta mensagens
# textuais e transforma linguagem natural em informações
# estruturadas.
#
# A saída desta etapa alimenta:
#
# → Sistema de Inferência Fuzzy
#
# permitindo a tomada de decisão inteligente.
#
# Relação com os tópicos do trabalho:
#
# ✔ Introdução à IA
# ✔ PLN
# ✔ Classificação supervisionada
# ✔ Naive Bayes
# ✔ Tratamento de texto não estruturado
#
# ==========================================================