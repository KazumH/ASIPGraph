import sys
import os
import numpy as np
import CSVGenerater

a = []
links = []
prefixes = []
fromases = []
toases = []
earlist_time = 0
latest_time = 0
ip = []
monitor_as = []
ASes = np.empty((0, 1), int)
allASes = []


firstfile = 200802241824
lastfile = 200802241909
filenum = 4

#dir = "../data/updates/YoutubePakistan/"

#15分刻みのファイルのみに対応、bgpdumpの*.bz2ファイルの読み込みに多分使う
def bz2filelisting(first, last, num):
    namelist = []
    for i in range(num):
        if (first + i * 15) % 100 > 59: # 1869だと読み込めないので1909にする
            return namelist
        else:
            print("Data Load Error")
            exit(1)
    return namelist
#import osで一気にディレクトリ内全部を引っ張ってくるのが賢いのか・・・。復元した生データの読み込みに使う
def rawfilelisting(dir):
    files = os.listdir(dir)
    print(files)
    return files


"""
class Prefix:
    def __init__(self, network, value, time. router, origin):
        self.prefix = network
        self.
"""


"""
class link:
    def __init__(self, t, from_AS, to_AS, hop):
        self.t = t
        self.fromasn = from_AS
        self.toasn = to_AS
        self.hops = hop
"""


#アプデデータ読み込み
def readupdatedata(filelist):
    #-Mオプションで展開

    num_of_files = len(filelist)
    for fileindex in range(num_of_files):
        alllinks = [[]]  # []にするとnumpy.sortがうまく働かなくなる。data[0] = []となる、
        print("Reading ", filelist[fileindex] )
        for line in open("../data/updates/YoutubePakistan/%s" % filelist[fileindex], "r"):
            #if line[0] == "#":
            #    continue

            word = line.split("|")
            #word[0]="BGP4MP" word[1]= 02/24/08 word[2]= "A" or "W", word[3]= ルータのIPアドレス word[4]=アナウンスしたAS word[5]= IPプリフィックス word[6]= ASパス(最右がオリジン)
            """
            Pythonでは、switch文が使えない
            if, elifを使うが、条件に
            if str in {"a", "b"}:
                文...
            elif str in {"c", "d", "e"}:
                文...
            とやると、可読性上がる
            """
            #アナウンス
            if word[2] == "A":
                ip = word[5].split("/")
                prefixes.append(word[5]) # 131.112.0.0/16
                prefix_value = ip[1] # 16
                time = word[1] #月/日/年
                #timestamp = int(time.mktime( datetime.strptime(dtime,"%Y-%m-%d %H:%M:%S").timetuple()))
                router = word[3]
                receive_AS = word[4]
                ASpath = word[6] # [13 11 290]
                origin = ASpath[-1] # 290

                # パス内のASすべて抽出し、全ASリストへ集計
                ASlist = ASpath.split(" ")
                for AS in ASlist:
                    allASes.append(int(AS))

                #リンクデータの集計
                for i in range(len(ASlist) - 1):
                    if ASlist[i] != ASlist[i+1]:
                        alllinks.append([ASlist[i], ASlist[i+1]])
                    else:
                        continue

            #取り消し
            elif word[2] == "W":
                ip = word[5].split("/")
                prefixes.append(word[5].rstrip("\n")) # 131.112.0.0/16
                prefix_value = ip[1] # 16
                time = word[1] #月/日/年
                #timestamp = int(time.mktime( datetime.strptime(dtime,"%Y-%m-%d %H:%M:%S").timetuple()))
                router = word[3]
                receive_AS = word[4]
            else:
                print("----------------------Data Load Error----------------------")
                exit(1)

        print("----------------------Dataset Load Success!----------------------")
#プリフィックス
        #print(prefixes)
        alluniqueprefixes = np.unique(prefixes)
        #print(alluniqueprefixes)
        #print("The number of announced IP Prefixes:", len(prefixes))
        #print("The number of unique IP Prefixes:", len(alluniqueprefixes))
#AS(ノード)
        alluniqueASes = np.unique(allASes)
        #print("The number of appeared ASes:", len(allASes))
        #print("All unique ASes: ", alluniqueASes)
        #print("The number of unique ASes:", len(alluniqueASes))
#リンク(エッジ)
        #print("All links: ", alllinks)
        #print("The number of appeared links:", len(alllinks))
        alluniquelinks = np.unique(alllinks)
        #print("The number of unique links: ", len(alluniquelinks))
        linkdata = np.sort(alllinks)
        #del linkdata[0:1] 先頭の[]を消したい・・・

        # エッジの重み集計
        weightedlinkdata = weightcounter(linkdata)

        #CSVに書き込む
        dirnum = fileindex + 1

        #重みなし(集計前)の全エッジ
        #CSVGenerater.Edgedatagenerate(dirnum, linkdata)
        #ノード(AS)
        CSVGenerater.Nodedatagenerate(dirnum, alluniqueASes)
        #リンク(重みつき)
        CSVGenerater.WeightedEdgedatagenerate(dirnum, weightedlinkdata)

#ファイル1つ分のデータのみ対応
def weightcounter(data):
    pointer = 1
    weighteddata = []
    print("----------------------Counting weight of edges...----------------------")
    print(data)
    while pointer < len(data):
        pointer, weighteddata = count(data, pointer, weighteddata)
    print("----------------------Finished!!!----------------------")
    print(weighteddata)
    return weighteddata

def count(input, pointer, output):
    weight = 1
    for j in range(pointer, len(input)):
        #最終行のリンク
        if j == len(input) - 1:
            if weight >= 1:
                newdata = input[j]
                newdata.append(weight)  # ["10026", "75292, 3]
                output.append(newdata)
                break
            else:
                exit(1)

        elif input[j] == input[(j + 1)]:
            #print(input[j], input[(j + 1)])
            #print("Same")
            weight += 1
            #print(weight)

        elif input[j] != input[(j + 1)]:
            #print(input[j], input[j + 1])
            #print("Wrong")
            newdata = input[j] # ["10026", "75292"]
            #print("Edgedata:", newdata)
            newdata.append(weight)  # ["10026", "75292", 3]
            #print("Newdata:", newdata)
            output.append(newdata)
            break

        else:
            exit(1)

    nextpointer = pointer + weight
    #print(nextpointer)
    #print(output)
    #再起は1000回まで。
    #count(input, nextpointer, output)  <- NG
    return nextpointer, output

    #print(output)

    #del data[0:weight]  # 頭weight分消す
    #nextdata = data
    #if data == []:
    #    return []
    #return newdata + weightcounter(nextdata)

#データチェックインターフェース
def checkrel():
    i = input("Please input p2p or c2p or p2c: ")
    if i == "all":
        global alldata
        alldata = linkdata[:, 0:2]
        #DrawGraph.draw(alldata)
    if i == "p2p":
        global p2pdata
        linktype = linkdata[:,2]
        p2pdata = linkdata[linktype == 0, :]
        p2p = p2pdata[:,0:2]
        print("Peer-to-Peer Links List: ")
        print("There are {0} p2p Links.".format(p2p.shape[0]))
        TierSeparater.P2PExtract(p2p, T1ASes, 1)
        #DrawGraph.draw(p2p)
    elif i in {"p2c", "c2p"}:
        global c2pdata
        linktype = linkdata[:,2]
        c2pdata = linkdata[linktype == -1, :]
        c2p = c2pdata[:,0:2]
        print("Customer-to-Provider(Provider-to-Customer) Links List: ")
        print("There are {0} c2p links.".format(c2p.shape[0]))
        TierSeparater.TierSeparate(c2p, -1)
        #DrawGraph.draw(c2p)
    elif i == "q":
        print("Finish")
        exit(0)
    else:
        print("Invalid Input!! Error!")
        exit(1)