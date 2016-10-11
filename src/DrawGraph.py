
import numpy as np
import colorsys
from matplotlib import pyplot as plt
plt.style.use('mystyle')

#import pygraphviz as pgv

import networkx as nx
import csv
import time


# 複数CSVデータまとめて読み込む(現時点ではまだdraw()に組み込んだまま
def graphdata(datanum):
    G = nx.Graph()
    for i in range(datanum):  # i = 0 ~ 3
        # ノードデータ
        dirnum = i + 1
        nodelist = []
        edgelist = []
        print("Loading ../data/csv/%d/nodes.csv Node data..." % dirnum)
        nodefile = open("../data/csv/%d/nodes.csv" % dirnum, "r")
        reader = csv.reader(nodefile)
        for row in reader:
            nodelist.append(row[0])

        list_of_nodelist.append(nodelist)
        print(list_of_nodelist)
        # エッジデータ
        print("Loading ../data/csv/%d/edges.csv Edge data..." % dirnum)
        edgefile = open("../data/csv/%d/edges.csv" % dirnum, "r")
        reader = csv.reader(edgefile)
        for row in reader:
            G.add_edge(row[0], row[1], weight=int(row[2]), color="yellow")

#CSVの重みつきエッジ、ノードデータからグラフ描画
def draw(num_of_files):
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

    list_of_nodelist = []
    list_of_edgelist = []

    G = nx.Graph()
#CSVファイル読み込み
    for i in range(num_of_files):  # i = 0 ~ 3
        # ノードリストのリストを作る
        dirnum = i + 1
        nodelist = []
        edgelist = []
        print("Loading ../data/csv/%d/nodes.csv Node data..." % dirnum)
        nodefile = open("../data/csv/%d/nodes.csv" % dirnum, "r")
        reader = csv.reader(nodefile)
        for row in reader:
            nodelist.append(row[0])
        list_of_nodelist.append(nodelist)

        # 1ファイルずつエッジデータを読む。重複したらまずい気が。。
        #print("Loading ../data/csv/%d/edges.csv Edge data..." % dirnum)
        #edgefile = open("../data/csv/%d/edges.csv" % dirnum, "r")
        #reader = csv.reader(edgefile)
        #for row in reader:
        #    G.add_edge(row[0], row[1], weight=int(row[2]))  # iごとに色が変わるようにする

    #時間窓全体分を集計したエッジデータ読み込み
    print("Loading ../data/csv/overall/overalledges.csv Edge data...")
    edgefile = open("../data/csv/overall/overalledges.csv", "r")
    reader = csv.reader(edgefile)
    for row in reader:
        G.add_edge(row[0], row[1], weight=int(row[2]))  # iごとに色が変わるようにする

    nodeset1 = set(list_of_nodelist[0]) #{'1', '2', '3'}
    nodeset2 = set(list_of_nodelist[1]) #{'2', '3', '4'}
    nodeset3 = set(list_of_nodelist[2]) #{'3', '4', '5'}
    nodeset4 = set(list_of_nodelist[3]) #{'4', '5', '6'}

    mergeset1_2 = nodeset1 | nodeset2 # {'1', '2', '3', '4'}
    mergeset1_2_3 = mergeset1_2 | nodeset3 # {'1', '2', '3', '4', '5'}
    mergeset1_2_3_4 = mergeset1_2_3 | nodeset4 # {'1', '2', '3', '4', '5', '6'}

    newnodeset2 = mergeset1_2 ^ nodeset1 #{'4'}
    newnodeset3 = mergeset1_2_3 ^ mergeset1_2 #{'5'}
    newnodeset4 = mergeset1_2_3_4 ^ mergeset1_2_3 #{'6'}

    newnodelist1 = list(nodeset1)
    newnodelist2 = list(newnodeset2)
    newnodelist3 = list(newnodeset3)
    newnodelist4 = list(newnodeset4)

#フィルタリング
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
    #ノード(色は色相360度をノード種類数で割った値ずつずらしていく 0, 90, 180, 270といった感じ) hsv(0,100,100), hsv(90,100,100)
    nx.draw_networkx_nodes(G, pos, nodelist=newnodelist1,node_color="#ff0000", alpha=0.5, linewidths=0) #四角にするにはnode_shape='s'
    nx.draw_networkx_nodes(G, pos, nodelist=newnodelist2,node_color="#7fff00", alpha=0.5, linewidths=0)
    nx.draw_networkx_nodes(G, pos, nodelist=newnodelist3,node_color="#00ffff", alpha=0.5, linewidths=0)
    nx.draw_networkx_nodes(G, pos, nodelist=newnodelist4,node_color="#7f00ff", alpha=0.5, linewidths=0)

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


