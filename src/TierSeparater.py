import numpy as np
import CSVGenerater

T1ASes = np.array([1, 174, 209, 286, 701, 702, 703, 1239, 1299, 2828, 2914, 3257, 3320, 3349, 3356, 5511, 6453, 6461, 6762, 7018, 12956])
T2ASes = T3ASes = T4ASes = T5ASes = np.empty((0, 1), int)

#peering
T1T1 = T2T2 = T3T3 = T4T4 = T5T5 = np.empty((0,2), int)
#Transit
T1T2 = T2T3 = T3T4 = T4T5 = np.empty((0,2), int)

def TierSeparate(data, type):
    print("-----------Tier Structure Separating-----------")
    #先にc2plinkを処理してTier2ASを決定
    #Tier1ASとc2p関係にあるASとそのリンクを抽出
    if type == -1:
        T1T2 = np.empty((0, 2), int)
        T2ASes = np.empty((0, 1), int)
        for provider in T1ASes:
            for link in data:
                if link[0] == provider:
                    T1T2 = np.append(T1T2, np.array([[provider, link[1]]]), axis=0)
                    T2ASes = np.append(T2ASes, link[1])
        print("Tier1->Tier2 p2c links: ")
        print(T1T2)
        print("The number of Tier1->Tier2 p2c links: {0}".format(T1T2.shape[0]))
        print("Tier2 ASes: ")
        print(T2ASes)
        print("The number of T2ASes: {0}".format(T2ASes.shape[0]))
        T2ASes = np.sort(np.unique(T2ASes))
        print("The number of unique T2ASes: {0}".format(T2ASes.shape[0]))
        print("Tier2 ASes: ")
        print(T2ASes)
        #CSVGenerater.Nodegdataenerater(T2ASes)
    else:
        print("Invalid Data! ")
        exit(1)

#未完成
def P2PExtract(linkdata, ASes, tier):
    print("-----------Extracting Tier {0} P2P links -----------".format(tier))
    T1T1 = np.empty((0, 2), int)
    #for fromAS in ASes:
    #    for toAS in ASes:
    #for link in linkdata:
    #    if link == np.array([[1, 11537]]):
    #        T1p2p = np.array([1, 11537])
    T1p2p = np.where(linkdata == np.array([[1, 11537]]))

    print(T1p2p)
    T1T1 = np.append(T1T1, T1p2p, axis=0)

    print(T1T1)

#リンクデータ内に存在する、from、to関係ない全ASのリスト
def ASExtract(linkdata):
    print("-----------Extracting ASes -----------")
    fromASes = np.empty((0, 1), int)
    toASes = np.empty((0, 1), int)
    for link in linkdata:
        fromASes = np.append(fromASes, link[0])
        toASes = np.append(toASes, link[1])

    fromASes = np.unique(fromASes)
    toASes = np.unique(toASes)
    allASes = np.append(fromASes, toASes)
    allASes = np.sort(np.unique(fromASes))
    print(allASes)
    print("There are {0} ASes(nodes) in this linkdata.".format(allASes.shape[0]))


