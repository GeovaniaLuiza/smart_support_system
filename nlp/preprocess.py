# ==========================================================
# PRÉ-PROCESSAMENTO DE TEXTO — CAMADA PLN
# ==========================================================
#
# Este módulo é responsável pelo pré-processamento
# das mensagens textuais utilizadas pelo sistema.
#
# Objetivo:
# Transformar texto não estruturado em uma forma
# adequada para o modelo de Machine Learning.
#
# O pré-processamento melhora:
#
# - qualidade da classificação
# - redução de ruídos
# - desempenho do Naive Bayes
#
# Técnicas aplicadas:
#
# ✔ Conversão para minúsculas
# ✔ Limpeza textual com Regex
# ✔ Tokenização
# ✔ Remoção de stop words
# ✔ Stemming
#
# ==========================================================



# ==========================================================
# IMPORTAÇÃO DAS BIBLIOTECAS
# ==========================================================

# Biblioteca para expressões regulares
#
# Utilizada para limpeza textual.
#
import re


# Biblioteca de PLN
import nltk


# Lista de stop words da NLTK
#
# Stop words são palavras muito frequentes
# que normalmente não agregam significado.
#
# Exemplos:
# "de", "a", "o", "e"
#
from nltk.corpus import stopwords


# Stemmer para português
#
# Responsável por reduzir palavras ao radical.
#
# Exemplo:
# "comprando" -> "compr"
#
from nltk.stem import RSLPStemmer



# ==========================================================
# DOWNLOAD DOS RECURSOS DA NLTK
# ==========================================================
#
# Faz o download das stop words em português.
#
# Necessário apenas na primeira execução.
#
# ==========================================================

nltk.download('stopwords')



# ==========================================================
# DEFINIÇÃO DAS STOP WORDS
# ==========================================================
#
# Conjunto de palavras irrelevantes para análise.
#
# Utilizar "set" melhora o desempenho da busca.
#
# ==========================================================

stop_words = set(stopwords.words('portuguese'))



# ==========================================================
# STEMMER
# ==========================================================
#
# O RSLPStemmer é um algoritmo de stemming
# específico para língua portuguesa.
#
# Objetivo:
# reduzir palavras para seu radical.
#
# ==========================================================

stemmer = RSLPStemmer()



# ==========================================================
# FUNÇÃO DE PRÉ-PROCESSAMENTO
# ==========================================================
#
# Entrada:
# - texto bruto digitado pelo usuário
#
# Saída:
# - texto limpo e processado
#
# Etapas executadas:
#
# 1) Conversão para minúsculas
# 2) Remoção de caracteres especiais
# 3) Tokenização
# 4) Remoção de stop words
# 5) Stemming
#
# ==========================================================

def preprocess_text(text):


    # ------------------------------------------------------
    # ETAPA 1 — CONVERSÃO PARA MINÚSCULAS
    # ------------------------------------------------------
    #
    # Padroniza o texto para evitar diferenças entre:
    #
    # "Bom"
    # "bom"
    #
    # ------------------------------------------------------

    text = text.lower()



    # ------------------------------------------------------
    # ETAPA 2 — LIMPEZA TEXTUAL
    # ------------------------------------------------------
    #
    # Remove:
    # - números
    # - pontuações
    # - caracteres especiais
    #
    # Mantendo apenas:
    # - letras
    # - espaços
    #
    # Regex utilizada:
    #
    # [^a-zà-ú\s]
    #
    # Significa:
    # remover tudo que NÃO for:
    # - letras
    # - caracteres acentuados
    # - espaço
    #
    # ------------------------------------------------------

    text = re.sub(r'[^a-zà-ú\s]', '', text)



    # ------------------------------------------------------
    # ETAPA 3 — TOKENIZAÇÃO
    # ------------------------------------------------------
    #
    # Divide o texto em palavras individuais.
    #
    # Exemplo:
    #
    # "atendimento muito bom"
    #
    # →
    #
    # ["atendimento", "muito", "bom"]
    #
    # ------------------------------------------------------

    tokens = text.split()



    # ------------------------------------------------------
    # ETAPA 4 — REMOÇÃO DE STOP WORDS
    # ------------------------------------------------------
    #
    # Remove palavras pouco relevantes para
    # análise de sentimentos.
    #
    # Exemplo:
    #
    # "o", "de", "para", "com"
    #
    # ------------------------------------------------------

    tokens = [t for t in tokens if t not in stop_words]



    # ------------------------------------------------------
    # ETAPA 5 — STEMMING
    # ------------------------------------------------------
    #
    # Reduz as palavras ao seu radical.
    #
    # Objetivo:
    # reduzir dimensionalidade e melhorar
    # generalização do modelo.
    #
    # Exemplo:
    #
    # "comprando"
    # "comprou"
    # "comprar"
    #
    # →
    #
    # "compr"
    #
    # ------------------------------------------------------

    tokens = [stemmer.stem(t) for t in tokens]



    # ------------------------------------------------------
    # ETAPA FINAL — RECONSTRUÇÃO DO TEXTO
    # ------------------------------------------------------
    #
    # Junta novamente os tokens processados
    # em uma única string.
    #
    # ------------------------------------------------------

    return " ".join(tokens)



# ==========================================================
# IMPORTÂNCIA NO PROJETO
# ==========================================================
#
# O pré-processamento é uma das etapas mais importantes
# do PLN, pois reduz ruídos e melhora a qualidade da
# classificação feita pelo Naive Bayes.
#
# Esta camada permite ao sistema:
#
# ✔ interpretar linguagem natural
# ✔ processar texto não estruturado
# ✔ melhorar a precisão da IA
#
# Relação com o trabalho:
#
# ✔ PLN
# ✔ Pré-processamento textual
# ✔ Tokenização
# ✔ Stop words
# ✔ Stemming
# ✔ Inteligência Artificial
#
# ==========================================================