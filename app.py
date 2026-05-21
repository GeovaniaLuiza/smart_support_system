# ==========================================================
# SISTEMA PRINCIPAL — INTERFACE VIA TERMINAL
# ==========================================================
#
# Este módulo representa a interface principal
# do sistema inteligente de atendimento.
#
# Objetivo:
# Permitir interação entre usuário e sistema,
# integrando todas as camadas de IA desenvolvidas.
#
# Fluxo do sistema:
#
# Usuário → PLN → Sistema Fuzzy → Resultado
#
# O sistema:
#
# 1) Recebe uma mensagem textual
# 2) Analisa o sentimento com Naive Bayes
# 3) Calcula a satisfação usando lógica fuzzy
# 4) Exibe os resultados
#
# Conceitos aplicados:
#
# ✔ Inteligência Artificial
# ✔ Processamento de Linguagem Natural
# ✔ Naive Bayes
# ✔ Sistema de Inferência Fuzzy
# ✔ Tomada de decisão
#
# ==========================================================



# ==========================================================
# IMPORTAÇÃO DOS MÓDULOS DO PROJETO
# ==========================================================

# Função responsável pela classificação de sentimentos
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
# TÍTULO DO SISTEMA
# ==========================================================

print("\n=== SISTEMA INTELIGENTE DE ATENDIMENTO ===\n")



# ==========================================================
# LOOP PRINCIPAL DO SISTEMA
# ==========================================================
#
# O sistema permanece executando até que o usuário
# digite "sair".
#
# while True:
# cria um loop infinito controlado manualmente.
#
# ==========================================================

while True:


    # ------------------------------------------------------
    # ENTRADA DA MENSAGEM
    # ------------------------------------------------------
    #
    # O usuário informa uma mensagem textual.
    #
    # Exemplo:
    # "O atendimento foi excelente"
    #
    # ------------------------------------------------------

    text = input("Digite a mensagem (ou 'sair'): ")



    # ------------------------------------------------------
    # CONDIÇÃO DE ENCERRAMENTO
    # ------------------------------------------------------
    #
    # Se o usuário digitar "sair",
    # o sistema encerra a execução.
    #
    # lower():
    # evita problemas com letras maiúsculas.
    #
    # ------------------------------------------------------

    if text.lower() == "sair":
        break



    # ------------------------------------------------------
    # ENTRADA DO TEMPO DE ESPERA
    # ------------------------------------------------------
    #
    # Variável numérica utilizada pelo sistema fuzzy.
    #
    # int():
    # converte a entrada para número inteiro.
    #
    # ------------------------------------------------------

    wait_time = int(input("Tempo de espera: "))



    # ======================================================
    # CAMADA I — CLASSIFICAÇÃO DE SENTIMENTO
    # ======================================================
    #
    # A função predict_sentiment():
    #
    # - realiza o pré-processamento
    # - aplica o modelo Naive Bayes
    # - retorna:
    #
    # sentiment  -> classe prevista
    # confidence -> confiança da previsão
    #
    # ======================================================

    sentiment, confidence = predict_sentiment(text)



    # ======================================================
    # CAMADA II — INFERÊNCIA FUZZY
    # ======================================================
    #
    # O sistema fuzzy recebe:
    #
    # - confiança do Naive Bayes
    # - tempo de espera
    #
    # E calcula:
    #
    # → nível de satisfação
    #
    # ======================================================

    score = evaluate_satisfaction(confidence, wait_time)



    # ======================================================
    # EXIBIÇÃO DOS RESULTADOS
    # ======================================================
    #
    # O sistema apresenta:
    #
    # - sentimento identificado
    # - confiança da previsão
    # - satisfação inferida
    #
    # ======================================================

    print("\n--- RESULTADO ---")


    # ------------------------------------------------------
    # Classe prevista pelo Naive Bayes
    # ------------------------------------------------------

    print("Sentimento:", sentiment)


    # ------------------------------------------------------
    # Confiança probabilística da previsão
    #
    # round(..., 2):
    # exibe apenas 2 casas decimais.
    # ------------------------------------------------------

    print("Confiança:", round(confidence, 2))


    # ------------------------------------------------------
    # Resultado do sistema fuzzy
    # ------------------------------------------------------

    print("Satisfação:", round(score, 2))


    print("-----------------\n")



# ==========================================================
# IMPORTÂNCIA NO PROJETO
# ==========================================================
#
# Este módulo integra todas as camadas do sistema
# inteligente.
#
# Ele representa a execução prática da solução,
# conectando:
#
# ✔ PLN
# ✔ Naive Bayes
# ✔ Sistema Fuzzy
# ✔ Tomada de decisão
#
# Fluxo completo:
#
# Texto do usuário
#        ↓
# Pré-processamento
#        ↓
# Naive Bayes
#        ↓
# Confiança da previsão
#        ↓
# Sistema Fuzzy
#        ↓
# Nível de satisfação
#
# ==========================================================