import csv

#data[0] = []で、なぜか消せないのでdata[1]から
def Edgedatagenerate(num, data):
    print("Writing in data/csv/%d/nonweightededges.csv" % num)
    csvfile = open('../data/csv/%d/nonweightededges.csv' % num, 'w', newline='')
    writer = csv.writer(csvfile, lineterminator='\n')
    for i in range(1, len(data)):
        writer.writerow(data[i])
    csvfile.close()

def WeightedEdgedatagenerate(num, data):
    print("Writing in data/csv/%d/edges.csv" % num)
    csvfile = open('../data/csv/%d/edges.csv' % num, 'w', newline='')
    writer = csv.writer(csvfile, lineterminator='\n')
    for i in range(0, len(data)):
        writer.writerow(data[i])
    csvfile.close()

def Nodedatagenerate(num, data):
    print("Writing in data/csv/%d/nodes.csv" % num)
    csvfile = open('../data/csv/%d/nodes.csv' % num, 'w', newline='')
    writer = csv.writer(csvfile, lineterminator='\n')
    for AS in data:
        writer.writerow([AS])
    csvfile.close()

def OverallEdgedatagenerate(data):
    print("Writing in data/csv/overall/overalledges.csv")
    csvfile = open('../data/csv/overall/overalledges.csv', 'w', newline='')
    writer = csv.writer(csvfile, lineterminator='\n')
    for i in range(1, len(data)):
        writer.writerow(data[i])
    csvfile.close()