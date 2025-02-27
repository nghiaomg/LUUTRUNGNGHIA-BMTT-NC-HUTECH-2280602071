def truyCapPhanTu(tupleData):
    firstElement = tupleData[0]
    lastElement = tupleData[-1]
    return firstElement, lastElement

iTuple = eval(input("Nhap Tuple, vi du (1,2,3): "))
f, l = truyCapPhanTu(iTuple)

print("Phan tu dau tien: ", f)
print("Phan tu cuoi cung: ", l)