def xoaPhanTu(dic, k):
    if k in dic:
        del dic[k]
        return True
    else:
        return False
    
myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

keyToDel = 'b'
rs = xoaPhanTu(myDict, keyToDel)
if rs:
    print("Phan tu xoa duoc xoa tu Dictionary", myDict)
else:
    print("Khong tim thay phan tu can xoa trong Dictionary")