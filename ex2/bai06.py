input_str = input("nhap X,Y: ")
dimensions = [int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multulist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multulist[row][col]= row*col
print(multulist)