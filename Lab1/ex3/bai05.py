def demSoLanXuatHien(lst):
    cDict = {}
    for i in lst:
        if i in cDict:
            cDict[i] += 1
        else:
            cDict[i] = 1

    return cDict

iString = input("Nhap danh sach cac tu, cach nhau bang dau cach: ")
wordLs = iString.split()

soLanXuatHien = demSoLanXuatHien(wordLs)

print("so lan xuat hien cua cac phan tu: ", soLanXuatHien)