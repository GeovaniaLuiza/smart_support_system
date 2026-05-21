# ==========================================================
# SISTEMA DE INFERÊNCIA FUZZY — CAMADA II
# ==========================================================
#
# Este módulo implementa um Sistema de Inferência Fuzzy
# do tipo Mamdani utilizando a biblioteca scikit-fuzzy.
#
# Objetivo:
# Tratar a incerteza presente no processo de análise
# de satisfação do cliente.
#
# O sistema recebe:
#
# 1) Probabilidade/confiança do classificador Naive Bayes
# 2) Tempo de espera do atendimento
#
# E retorna:
#
# -> Nível de satisfação do cliente
#
# Conceitos aplicados:
# - Lógica Fuzzy
# - Funções de pertinência
# - Regras linguísticas
# - Inferência Mamdani
# - Defuzzificação
#
# ==========================================================


# ==========================================================
# IMPORTAÇÃO DAS BIBLIOTECAS
# ==========================================================

# Biblioteca para operações matemáticas
import numpy as np

# Biblioteca principal de lógica fuzzy
import skfuzzy as fuzz

# Módulo de controle fuzzy
from skfuzzy import control as ctrl



# ==========================================================
# DEFINIÇÃO DAS VARIÁVEIS FUZZY
# ==========================================================
#
# Antecedent  -> variáveis de entrada
# Consequent  -> variável de saída
#
# ==========================================================


# ----------------------------------------------------------
# Variável fuzzy:
# Probabilidade do sentimento detectado pelo Naive Bayes
#
# Intervalo:
# 0 até 1
#
# Exemplo:
# 0.9 = alta confiança
# 0.2 = baixa confiança
# ----------------------------------------------------------

sentiment_prob = ctrl.Antecedent(
    np.arange(0, 1.01, 0.01),
    'sentiment_prob'
)


# ----------------------------------------------------------
# Variável fuzzy:
# Tempo de espera do cliente
#
# Intervalo:
# 0 até 60 minutos
# ----------------------------------------------------------

wait_time = ctrl.Antecedent(
    np.arange(0, 61, 1),
    'wait_time'
)


# ----------------------------------------------------------
# Variável fuzzy de saída:
# Nível de satisfação do cliente
#
# Intervalo:
# 0 até 100
# ----------------------------------------------------------

satisfaction = ctrl.Consequent(
    np.arange(0, 101, 1),
    'satisfaction'
)



# ==========================================================
# FUNÇÕES DE PERTINÊNCIA
# ==========================================================
#
# As funções de pertinência representam conjuntos fuzzy.
#
# Foi utilizada a função triangular (trimf),
# bastante comum em sistemas Mamdani.
#
# ==========================================================



# ==========================================================
# FUNÇÕES DE PERTINÊNCIA
# PARA A PROBABILIDADE DE SENTIMENTO
# ==========================================================

# ----------------------------------------------------------
# Baixa probabilidade
#
# Quanto mais próximo de 0,
# maior o grau de pertinência em "low"
# ----------------------------------------------------------

sentiment_prob['low'] = fuzz.trimf(
    sentiment_prob.universe,
    [0, 0, 0.5]
)

# ----------------------------------------------------------
# Média probabilidade
# ----------------------------------------------------------

sentiment_prob['medium'] = fuzz.trimf(
    sentiment_prob.universe,
    [0.3, 0.5, 0.7]
)

# ----------------------------------------------------------
# Alta probabilidade
#
# Valores próximos de 1 possuem maior pertinência
# ----------------------------------------------------------

sentiment_prob['high'] = fuzz.trimf(
    sentiment_prob.universe,
    [0.5, 1, 1]
)



# ==========================================================
# FUNÇÕES DE PERTINÊNCIA
# PARA O TEMPO DE ESPERA
# ==========================================================

# ----------------------------------------------------------
# Tempo curto
# ----------------------------------------------------------

wait_time['short'] = fuzz.trimf(
    wait_time.universe,
    [0, 0, 20]
)

# ----------------------------------------------------------
# Tempo médio
# ----------------------------------------------------------

wait_time['medium'] = fuzz.trimf(
    wait_time.universe,
    [10, 30, 50]
)

# ----------------------------------------------------------
# Tempo longo
# ----------------------------------------------------------

wait_time['long'] = fuzz.trimf(
    wait_time.universe,
    [40, 60, 60]
)



# ==========================================================
# FUNÇÕES DE PERTINÊNCIA
# PARA SATISFAÇÃO
# ==========================================================

# ----------------------------------------------------------
# Baixa satisfação
# ----------------------------------------------------------

satisfaction['low'] = fuzz.trimf(
    satisfaction.universe,
    [0, 0, 40]
)

# ----------------------------------------------------------
# Média satisfação
# ----------------------------------------------------------

satisfaction['medium'] = fuzz.trimf(
    satisfaction.universe,
    [30, 50, 70]
)

# ----------------------------------------------------------
# Alta satisfação
# ----------------------------------------------------------

satisfaction['high'] = fuzz.trimf(
    satisfaction.universe,
    [60, 100, 100]
)



# ==========================================================
# REGRAS FUZZY
# ==========================================================
#
# As regras representam conhecimento especialista.
#
# Estrutura:
#
# SE condição ENTÃO ação
#
# Operadores utilizados:
#
# &  -> AND
# |  -> OR
#
# ==========================================================


# ----------------------------------------------------------
# REGRA 1
#
# SE:
#   probabilidade do sentimento é alta
#   E tempo de espera é curto
#
# ENTÃO:
#   satisfação é alta
# ----------------------------------------------------------

rule1 = ctrl.Rule(
    sentiment_prob['high'] & wait_time['short'],
    satisfaction['high']
)


# ----------------------------------------------------------
# REGRA 2
#
# SE:
#   probabilidade é média
#   E tempo de espera é médio
#
# ENTÃO:
#   satisfação é média
# ----------------------------------------------------------

rule2 = ctrl.Rule(
    sentiment_prob['medium'] & wait_time['medium'],
    satisfaction['medium']
)


# ----------------------------------------------------------
# REGRA 3
#
# SE:
#   probabilidade é baixa
#   OU tempo de espera é longo
#
# ENTÃO:
#   satisfação é baixa
# ----------------------------------------------------------

rule3 = ctrl.Rule(
    sentiment_prob['low'] | wait_time['long'],
    satisfaction['low']
)



# ==========================================================
# CRIAÇÃO DO SISTEMA FUZZY MAMDANI
# ==========================================================
#
# O sistema Mamdani é composto por:
#
# - Variáveis fuzzy
# - Funções de pertinência
# - Regras fuzzy
#
# ==========================================================

control_system = ctrl.ControlSystem([
    rule1,
    rule2,
    rule3
])



# ==========================================================
# SIMULAÇÃO DO SISTEMA
# ==========================================================
#
# Responsável por:
#
# - Receber entradas
# - Aplicar inferência fuzzy
# - Realizar defuzzificação
# - Gerar saída numérica final
#
# ==========================================================

simulation = ctrl.ControlSystemSimulation(control_system)



# ==========================================================
# FUNÇÃO PRINCIPAL DO SISTEMA FUZZY
# ==========================================================
#
# Entrada:
# - probability -> confiança do Naive Bayes
# - waiting -> tempo de espera
#
# Saída:
# - nível numérico de satisfação
#
# ==========================================================

def evaluate_satisfaction(probability, waiting):

    # ------------------------------------------------------
    # Entrada 1:
    # Confiança/probabilidade do sentimento
    # ------------------------------------------------------

    simulation.input['sentiment_prob'] = probability


    # ------------------------------------------------------
    # Entrada 2:
    # Tempo de espera do cliente
    # ------------------------------------------------------

    simulation.input['wait_time'] = waiting


    # ------------------------------------------------------
    # Execução da inferência fuzzy
    #
    # Etapas:
    # 1) Fuzzificação
    # 2) Aplicação das regras
    # 3) Agregação
    # 4) Defuzzificação
    # ------------------------------------------------------

    simulation.compute()


    # ------------------------------------------------------
    # Retorna o valor final de satisfação
    # ------------------------------------------------------

    return simulation.output['satisfaction']