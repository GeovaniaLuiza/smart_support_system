import networkx as nx
import matplotlib.pyplot as plt

def build_graph(num_tickets, num_attendants):

    G = nx.Graph()

    # Nós de tickets
    for i in range(num_tickets):

        G.add_node(
            f"T{i}",
            bipartite=0
        )

    # Nós de atendentes
    for j in range(num_attendants):

        G.add_node(
            f"A{j}",
            bipartite=1
        )

    # Conexões possíveis
    for i in range(num_tickets):

        for j in range(num_attendants):

            G.add_edge(f"T{i}", f"A{j}")

    return G

def draw_graph(G):

    nx.draw(
        G,
        with_labels=True,
        node_color='lightblue',
        node_size=2000,
        font_size=10
    )

    plt.show()