import sys
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
alllinks = [[]] #[]にするとnumpy.sortがうまく働かなくなる。data[0] = []となる
"""
class Prefix:
    def __init__(self, network, value, time. router, origin):
        self.prefix = network
        self.
"""

# 隣接行列
def adjacent():
        return 0

"""
class link:
    def __init__(self, t, from_AS, to_AS, hop):
        self.t = t
        self.fromasn = from_AS
        self.toasn = to_AS
        self.hops = hop
"""

def checkupdate(alldata):
    i = input("Please input Natural Number of Origin AS ")
    if i == "T":
        print("Earlist Time: " + earlist_time + ", " + "Latest Time: " + latest_time)
    elif i == "M":
        print("Monitors:")
        for j in range(0, 29):
            print("ID: " + str(j) + ", " + "IP Address: " + ip[j] + ", " + "AS Number: " + monitor_as[j])
    elif i in {"D", "I"}:
        print("Links:")
        for j in range(0, 100):
            print("ID: " + str(j) + ", " + "Type: " + types[j] + ", " + "From: " + fromases[j] + ", " + "To: " + toases[j])
    else:
        i2 = int(i)
        print("Datatype: " + types[i2])
        print("From_AS number is: " + fromases[i2])
        print("To_AS number is : " + toases[i2])

#リンクデータ
def readupdatedata():
    #-Mオプションで展開
    global alldata
    for line in open('../data/updates/YoutubePakistan(2008)/02241824', 'r'):
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
            #ASリンクの集計
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
            print("Data Load Error")
            exit(1)

    print("Dataset Load Success!")
    #print(prefixes)
    alluniqueprefixes = np.unique(prefixes)
    #print(alluniqueprefixes)
    print("The number of announced IP Prefixes:", len(prefixes))
    print("The number of unique IP Prefixes:", len(alluniqueprefixes))

    alluniqueASes = np.unique(allASes)
    print("The number of appeared ASes:", len(allASes))
    #print("All unique ASes: ", alluniqueASes)
    print("The number of unique ASes:", len(alluniqueASes))
    CSVGenerater.Nodedatagenerate(alluniqueASes)

    print("All links: ", alllinks)
    print("The number of appeared links:", len(alllinks))
    alluniquelinks = np.unique(alllinks)
    print("The number of unique links: ", len(alluniquelinks))
    linkdata = np.sort(alllinks)
    #del linkdata[0:1] 先頭の[]を消したい・・・

    #集計
    weightedlinkdata = weightcounter(linkdata)

    #CSVへ
    #CSVGenerater.Edgedatagenerate(linkdata)
    CSVGenerater.WeightedEdgedatagenerate(weightedlinkdata)

    #checkupdate(alldata)

def weightcounter(data):
    #weight = 1
    pointer = 1
    weighteddata = []
    while pointer < len(data):
        pointer, weighteddata = count(data, pointer, weighteddata)
    print("Weight Count Finished!!!")
    print(weighteddata)
    return weighteddata

def count(input, pointer, output):
    weight = 1

    for i in range(pointer, len(input)):
        #print(input[i], input[i+1])
        if i == len(input) - 1:
            if weight >= 1:
                newdata = input[i]
                newdata.append(weight)  # ["10026", "75292, 3]
                output.append(newdata)
                break
            else:
                exit(1)
        elif input[i] == input[i + 1]:
            #print("Same")
            weight += 1
            #print(weight)
        elif input[i] != input[i + 1]:
            #print("Wrong")
            newdata = input[i]
            newdata.append(weight)  # ["10026", "75292, 3]
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