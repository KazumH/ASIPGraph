import csv

#data[0] = []で、なぜか消せないのでdata[1]から
def Edgedatagenerate(data):
    csvfile = open('../data/csv/edges.csv', 'w', newline='')
    writer = csv.writer(csvfile, lineterminator='\n')
    for i in range(1, len(data)):
        writer.writerow(data[i])
    csvfile.close()

def WeightedEdgedatagenerate(data):
    csvfile = open('../data/csv/weightededges.csv', 'w', newline='')
    writer = csv.writer(csvfile, lineterminator='\n')
    for i in range(0, len(data)):
        writer.writerow(data[i])
    csvfile.close()

def Nodedatagenerate(data):
    csvfile = open('../data/csv/nodes.csv', 'w', newline='')
    writer = csv.writer(csvfile, lineterminator='\n')
    for AS in data:
        writer.writerow([AS])
    csvfile.close()
