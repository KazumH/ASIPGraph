
import numpy as np
import colorsys
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
    node_size = 100
    node_alpha = 0.3
    node_text_size = 12
    edge_color = 'blue'
    edge_alpha = 0.3
    edge_tickness = 1
    edge_text_pos = 0.3
    text_font = 'sans-serif'

    nodelist1 = []
    nodelist2 = []
    nodelist3 = []
    nodelist4 = []

    G = nx.Graph()
#1番目のデータ
#ノードデータ
    print("Loading Node data...")
    nodefile = open("../data/csv/1/nodes.csv","r")
    reader = csv.reader(nodefile)
    for row in reader:
        nodelist1.append(row[0])

#エッジデータ
    print("Loading Edge data...")
    edgefile = open("../data/csv/1/edges.csv","r")
    reader = csv.reader(edgefile)
    for row in reader:
        G.add_edge(row[0], row[1], weight = int(row[2]), color = "yellow")

# 2番目のデータ
# ノードデータ
    print("Loading Node data...")
    nodefile = open("../data/csv/2/nodes.csv", "r")
    reader = csv.reader(nodefile)
    for row in reader:
        nodelist2.append(row[0])

# エッジデータ
    print("Loading Edge data...")
    edgefile = open("../data/csv/2/edges.csv", "r")
    reader = csv.reader(edgefile)
    for row in reader:
        G.add_edge(row[0], row[1], weight=int(row[2]), color="green")




# 3番目のデータ
# ノードデータ
    print("Loading Node data...")
    nodefile = open("../data/csv/3/nodes.csv", "r")
    reader = csv.reader(nodefile)
    for row in reader:
        nodelist3.append(row[0])

#エッジデータ
    print("Loading Edge data...")
    edgefile = open("../data/csv/3/edges.csv","r")
    reader = csv.reader(edgefile)
    for row in reader:
        G.add_edge(row[0], row[1], weight = int(row[2]), color = "skyblue")

# 4番目のデータ
# ノードデータ
    print("Loading Node data...")
    nodefile = open("../data/csv/4/nodes.csv", "r")
    reader = csv.reader(nodefile)
    for row in reader:
        nodelist4.append(row[0])

# エッジデータ
    print("Loading Edge data...")
    edgefile = open("../data/csv/4/edges.csv", "r")
    reader = csv.reader(edgefile)
    for row in reader:
        G.add_edge(row[0], row[1], weight=int(row[2]), color="violet")

#ノード設定
    nodes = np.unique(nodelist1 + nodelist2 + nodelist3 + nodelist4)
    G.add_nodes_from(nodes)


    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 100]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 100]
    ehuge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 1000]

# 原因ASノードにのみラベルを表示させる
    speciallabels = {}
    speciallabels["701"] = r"701"
    speciallabels["17557"] = r"17557"
    speciallabels["36561"] = r"36561"

    #グラフ描画
    print("Drawing Graph...")
    start_time = time.time()
    #ばねモデル(Fruchterman-Reingold)
    pos = nx.spring_layout(G)
    #ノード
    nx.draw_networkx_nodes(G, pos, nodelist=nodelist1,node_color="b",alpha=0.2, linewidths=0)
    nx.draw_networkx_nodes(G, pos, nodelist=nodelist2,node_color="g",alpha=0.4, linewidths=0)
    nx.draw_networkx_nodes(G, pos, nodelist=nodelist3,node_color="r",alpha=0.6, linewidths=0)
    nx.draw_networkx_nodes(G, pos, nodelist=nodelist4,node_color="y", linewidths=0)

    #エッジ
    nx.draw_networkx_edges(G, pos, edgelist=ehuge,width=10, edge_color="green")
    nx.draw_networkx_edges(G, pos, edgelist=elarge,width=2, alpha=0.5, style='dashed')
    #nx.draw_networkx_edges(G, pos, edgelist=esmall,width=1, alpha=0.5, style='dashed')
    #ラベル
    nx.draw_networkx_labels(G, pos, labels=speciallabels, font_size=9, font_family='sans-serif')


    elapsed_time = time.time() - start_time
    print("Drawn in " + str(elapsed_time) + "[sec].")

    plt.xticks([])
    plt.yticks([])
    plt.show()


