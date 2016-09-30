
import numpy as np
from matplotlib import pyplot as plt
#import pygraphviz as pgv
#import networkx as nx
import time

T1ASes = [1, 174, 209, 286, 701, 702, 703, 1239, 1299, 2828, 2914, 3257, 3320, 3349, 3356, 5511, 6453, 6461, 6762, 7018, 12956]


def draw(data):
    labels = None
    graph_layout = 'shell'
    node_size = 1600
    node_color = 'red'
    node_alpha = 0.3
    node_text_size = 12
    edge_color = 'blue'
    edge_alpha = 0.3
    edge_tickness = 1
    edge_text_pos = 0.3
    text_font = 'sans-serif'

    G = nx.Graph()
    print(data)
    print(G.number_of_edges())
    print("Drawing Graph...")


    #CSVGenerater.Edgedatagenerate(data)

    #Tier1のASノード
    G.add_nodes_from(T1ASes)
    #リンク
    for edge in data:
        G.add_edge(edge[0], edge[1])

    #Tier1ASのラベル
    labels={}
    for i in T1ASes:
        labels[i]=str(i)

#グラフ描画
    start_time = time.time()
    nx.draw_networkx_nodes(G, nx.fruchterman_reingold_layout(G), node_size=20, nodelist=T1ASes ,alpha=node_alpha,node_color='red')
    nx.draw_networkx_edges(G, nx.fruchterman_reingold_layout(G), width=edge_tickness, alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(G, nx.fruchterman_reingold_layout(G), labels, font_size=8)
    elapsed_time = time.time() - start_time
    print("Drew in " + str(elapsed_time) + "[sec].")

    plt.xticks([])
    plt.yticks([])
    plt.show()



