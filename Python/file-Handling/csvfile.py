import csv
f = open("second.csv",'a',newline="")
wo = csv.writer(f)
data = [['a', 'b', 'c', 'd', 'e',],[16,16,45,24,134,14,41,414,1414,141,],[34,234,243,2342,3434,234,234,23]]
wo.writerows(data)
f.close()


file = open("second.csv",'r')
re = csv.reader(file)
li= list(re)
for row in range(len(li)):
    print(len[row])
file.close()