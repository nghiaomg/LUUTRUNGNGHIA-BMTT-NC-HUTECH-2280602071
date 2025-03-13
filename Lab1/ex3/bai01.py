def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num %2 == 0:
            tong += num
    return tong

input_list = input("nhap danh sach cac so, cac nhau bang dau phay: ")
n = list(map(int, input_list.split(',')))

tc = tinh_tong_so_chan(n);

print("Tong so chan trong list la: ", tc)

