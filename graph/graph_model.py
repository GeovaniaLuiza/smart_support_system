# ==========================================================
# TEORIA DOS GRAFOS — CAMADA DE REPRESENTAÇÃO
# ==========================================================
#
# Este módulo implementa uma representação em grafo
# do sistema de atendimento.
#
# Objetivo:
# Modelar a relação entre:
#
# - Tickets de atendimento
# - Atendentes disponíveis
#
# A modelagem em grafos permite representar possíveis
# conexões entre solicitações e recursos disponíveis.
#
# Conceitos aplicados:
# - Teoria dos Grafos
# - Grafos bipartidos
# - Representação do conhecimento
# - Alocação de recursos
#
# Bibliotecas utilizadas:
# - NetworkX → criação/manipulação do grafo
# - Matplotlib → visualização gráfica
#
# ==========================================================



# ==========================================================
# IMPORTAÇÃO DAS BIBLIOTECAS
# ==========================================================

# Biblioteca para criação e manipulação de grafos
import networkx as nx

# Biblioteca para visualização gráfica
import matplotlib.pyplot as plt



# ==========================================================
# FUNÇÃO DE CONSTRUÇÃO DO GRAFO
# ==========================================================
#
# Esta função cria um grafo bipartido.
#
# Um grafo bipartido possui dois conjuntos de nós:
#
# 1) Tickets (T)
# 2) Atendentes (A)
#
# As conexões representam possíveis alocações entre
# tickets e atendentes.
#
# ==========================================================

def build_graph(num_tickets, num_attendants):

    # ------------------------------------------------------
    # Criação do grafo vazio
    # ------------------------------------------------------

    G = nx.Graph()


    # ======================================================
    # CRIAÇÃO DOS NÓS DE TICKETS
    # ======================================================
    #
    # Cada ticket representa uma solicitação de cliente.
    #
    # Exemplo:
    # T0, T1, T2...
    #
    # bipartite=0 indica o primeiro conjunto do grafo.
    #
    # ======================================================

    for i in range(num_tickets):

        G.add_node(
            f"T{i}",
            bipartite=0
        )


    # ======================================================
    # CRIAÇÃO DOS NÓS DE ATENDENTES
    # ======================================================
    #
    # Cada atendente representa um recurso disponível
    # para atendimento.
    #
    # Exemplo:
    # A0, A1, A2...
    #
    # bipartite=1 indica o segundo conjunto do grafo.
    #
    # ======================================================

    for j in range(num_attendants):

        G.add_node(
            f"A{j}",
            bipartite=1
        )


    # ======================================================
    # CRIAÇÃO DAS ARESTAS
    # ======================================================
    #
    # Cada aresta representa uma possível conexão entre:
    #
    # Ticket ↔ Atendente
    #
    # Isso permite modelar cenários de:
    #
    # - escalonamento
    # - distribuição de tarefas
    # - alocação de recursos
    #
    # ======================================================

    for i in range(num_tickets):

        for j in range(num_attendants):

            G.add_edge(f"T{i}", f"A{j}")


    # ------------------------------------------------------
    # Retorna o grafo criado
    # ------------------------------------------------------

    return G



# ==========================================================
# FUNÇÃO DE VISUALIZAÇÃO DO GRAFO
# ==========================================================
#
# Esta função desenha o grafo criado utilizando
# representação visual.
#
# A visualização ajuda a compreender:
#
# - conectividade
# - distribuição de recursos
# - estrutura do problema
#
# ==========================================================

def draw_graph(G):

    # ------------------------------------------------------
    # Desenha o grafo
    # ------------------------------------------------------

    nx.draw(
        G,

        # Exibe os nomes dos nós
        with_labels=True,

        # Cor dos nós
        node_color='lightblue',

        # Tamanho visual dos nós
        node_size=2000,

        # Tamanho da fonte dos rótulos
        font_size=10
    )


    # ------------------------------------------------------
    # Exibe o grafo na tela
    # ------------------------------------------------------

    plt.show()



# ==========================================================
# APLICAÇÃO NO PROJETO
# ==========================================================
#
# Este módulo complementa o sistema inteligente ao
# representar a estrutura de atendimento através
# de grafos.
#
# Possíveis aplicações:
#
# - Distribuição inteligente de tickets
# - Balanceamento de carga
# - Escalonamento de atendimentos
# - Base para otimização com Simulated Annealing
#
# Relação com o trabalho:
#
# ✔ Representação do conhecimento
# ✔ Teoria dos grafos
# ✔ Alocação de recursos
# ✔ Busca combinatória
#
# ==========================================================