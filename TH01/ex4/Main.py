from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while(True):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("\n**************************************************")
    print("\n** 1. THEM SINH VIEN                            **")
    print("\n** 2.  Cap nhat thong tin sinh vien voi id      **")
    print("\n** 3.  Xoa sinh vien voi id                     **")
    print("\n** 4.  Tim kiem sinh vien theo ten              **")
    print("\n** 5.  Sap xep theo diem TB                     **")
    print("\n** 6.  Sap xep theo chuyen nganh                **")
    print("\n** 7.  Hien thi danh sach sinh vien             **")
    print("\n** 0.  Thoat                                    **")
    print("\n**************************************************")

    key = int(input("Nhap tuy chon"))
    if key == 1:
        print("\n1 Them sinh vien.")
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong!")
    
    elif key == 2:
        if(qlsv.soLuongSinhVien() > 0):
            print("\n2 Cap nhat thong tin sinh vien.")
            print("\nNhap Id: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh sach sinh vien trong")

    elif key == 3:
        if(qlsv.soLuongSinhVien() > 0):
            print("\n3 Xoa sinh vien.")
            print("\nNhap Id: ")
            ID = int(input())
            if(qlsv.deleteById(ID)):
                print("\nSinh vien co id = ", ID, " da bi xoa")
        else:
            print("\nDanh sach sinh vien trong")

    elif key == 4:
        if(qlsv.soLuongSinhVien() > 0):
            print("\n4 Tim kiem theo ten.")
            print("\nNhap Ten: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sach sinh vien trong")

    elif key == 5:

        if(qlsv.soLuongSinhVien() > 0):
            print("\n5 Sap xep sinh vien theo diem trung binh (GPA).")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong")

    elif key == 6:

        if(qlsv.soLuongSinhVien() > 0):
            print("\n6 Sap xep sinh vien theo diem ten.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong")

    elif key == 7:

        if(qlsv.soLuongSinhVien() > 0):
            print("\n7 Hien thi danh sach sinh vien")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong")
    elif key == 0:
        print("\nBan da thoat chuong trinh")
        break
    else:
        print("\nKhong co chuc nang nay")
        print("\nHay chon chuc nang trong menu")
        

