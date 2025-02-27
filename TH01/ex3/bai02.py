def dao_nguoc_list(lst):
    return lst[::-1]

ilist = input("Nhap danh sach cac so cach nhau bang dau phay: ")
n = list(map(int, ilist.split(',')))

list_dn = dao_nguoc_list(n)

print("list sau khi dao nguoc", list_dn)