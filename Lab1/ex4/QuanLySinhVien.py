from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        maxId = 1
        if(self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if(maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1 
        return maxId


    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()


    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh: ")
        major = input("Nhap chuyen nganh: ")
        diemTB = float(input("Nhap diem TB: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv: SinhVien = self.findById(ID)
        if sv is not None:
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh: ")
            major = input("Nhap chuyen nganh: ")
            diemTB = float(input("Nhap diem TB: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print(f"Sinh vien co Id = {ID} khong ton tai.")


    def sortByID(self):
        self.listSinhVien.sort(key = lambda x : x._id, reverse=False)

    def sortByName(self):
        self.listSinhVien.sort(key = lambda x : x._name, reverse=False)


    def sortByDiemTB(self):
        self.listSinhVien.sort(key = lambda x : x._diemTB, reverse=False)

    def findById(self, ID):
        searchResult = None
        if(self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if(sv._id == ID):
                    searchResult = sv
        return searchResult

    def findByName(self, keyword):
        listSV = []
        if(self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV

    def deleteById(self, ID):
        isDeleted = False
        sv = self.findById(ID)
        if(sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
    
    def xepLoaiHocLuc(self, sv:SinhVien):
        if(sv._diemTB >= 8):
            sv._hocLuc = "Gioi"
        elif(sv._diemTB >= 6.5):
            sv._hocLuc = "Kha"
        elif(sv._diemTB >= 5):
            sv._hocLuc = "Trung Binh"
        else:
            sv._hocLuc = "Yeu"

    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8}".format("ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))
        
        if listSV.__len__() > 0:
            for sv in listSV:
                sv_id = sv._id if sv._id is not None else "N/A"
                sv_name = sv._name if sv._name is not None else "N/A"
                sv_sex = sv._sex if sv._sex is not None else "N/A"
                sv_major = sv._major if sv._major is not None else "N/A"
                sv_diemTB = sv._diemTB if sv._diemTB is not None else "N/A"
                sv_hocLuc = sv._hocLuc if sv._hocLuc is not None else "Chua Xep Loai"  # Default for hocLuc

                print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8}".format(sv_id, sv_name, sv_sex, sv_major, sv_diemTB, sv_hocLuc))

        print("\n")



    def getListSinhVien(self):
        return self.listSinhVien
