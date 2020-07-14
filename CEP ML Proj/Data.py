import csv

csv.register_dialect('myDialect',
                     delimiter=';',
                     skipinitialspace=True,
                     quoting=csv.QUOTE_ALL)

smath= []  #dataset for math students
sport= []  #dataset for portugese students
attributelist=[]
intattributes=[2,6,7,12,13,14,23,24,25,26,27,28,29,30,31,32] #list of numeric attributes


#reading data from math file

with open('student-mat.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='myDialect')
    for row in reader:
        if row[0]=='school':
            row.append('G_ave')
            attributelist=row
        else:
            for i in intattributes:
                row[i]=int(row[i])
            mean=(int(row[30])+int(row[31])+int(row[32]))/3
            row.append(mean)
        smath.append(row) #creates a 2d list


#smaller datasets in dictionaries
mathdata={}
for i in range(len(attributelist)):
    attribute=[]
    for j in range(len(smath)):
        if j>0:
            attribute.append(smath[j][i])
    mathdata[attributelist[i]]=attribute
