import csv

def Edgedatagenerate(data):
    csvfile = open('../data/csv/edges.csv', 'w', newline='')
    writer = csv.writer(csvfile, lineterminator='\n')
    for edge in data:
        writer.writerow(edge)
    csvfile.close()

def Nodedatagenerate(data):
    csvfile = open('../data/csv/nodes.csv', 'w', newline='')
    writer = csv.writer(csvfile, lineterminator='\n')
    for AS in data:
        writer.writerow([AS])
    csvfile.close()
