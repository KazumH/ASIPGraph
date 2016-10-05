
import numpy as np
from matplotlib import pyplot as plt
plt.style.use('mystyle')

#import pygraphviz as pgv

import networkx as nx
import csv
import time

#CSVの重みつきエッジ、ノードデータからグラフ描画
def draw():
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
#ノードデータ
    print("Loading Node data...")
    nodefile = open("../data/csv/nodes.csv","r")
    reader = csv.reader(nodefile)
    for row in reader:
        G.add_node(row[0])
#エッジデータ
    print("Loading Edge data...")
    edgefile = open("../data/csv/edges.csv","r")
    reader = csv.reader(edgefile)
    for row in reader:
        G.add_edge(row[0], row[1], weight = int(row[2]))

#フィルタリング
    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 50]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 50]

#グラフ描画
    print("Drawing Graph...")
    start_time = time.time()
    #ばねモデル
    pos = nx.spring_layout(G)
    #ノード
    nx.draw_networkx_nodes(G, pos, node_size=150)
    #エッジ
    nx.draw_networkx_edges(G, pos, edgelist=elarge,width=8, edge_color='g')
    nx.draw_networkx_edges(G, pos, edgelist=esmall,width=3, alpha=0, edge_color='b', style='dashed')
    #ラベル
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
    elapsed_time = time.time() - start_time
    print("Drawn in " + str(elapsed_time) + "[sec].")

    plt.xticks([])
    plt.yticks([])
    plt.show()


