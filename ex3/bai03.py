def tao_tuple_tu_list(lst):
    return tuple(lst)

ilist = input("Nhap danh sach cac so cach nhau bang dau phay: ")
n = list(map(int, ilist.split(',')))

my_tuple = tao_tuple_tu_list(n)

print("tuple tu list", my_tuple)