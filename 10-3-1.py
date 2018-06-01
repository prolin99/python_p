import csv
f = open('3.csv', 'rt')
reader =  csv.DictReader(f,fieldnames=['a','b','c','d','e'])
for row in reader :
    print(row)
    print(row['a'])
f.close()

    #for row in reader:
    #    print(row)
    #    for cell in row:
    #        print( cell)
