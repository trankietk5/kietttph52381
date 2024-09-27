def hienThi():
    print("Đã chọn chương trình: Hiển thị danh sách")
def timKiem():
    print("Đã chọn chương trình: Tìm kiếm ")
def themMoi():
    print("Đã chọn chương trình: Thêm mới")
def capNhat():
    print("Đã chọn chương trình: Cập nhật")
def xoa():
    print("Đã chọn chương trình: Xóa")
def sapXep():
    print("Đã chọn chương trình: Sắp xếp")
def phanTrang():
    print("Đã chọn chương trình: Phân trang")
def xemChiTiet():
    print("Đã chọn chương trình: Xem chi tiết")
def xuatDuLieu():
    print("Đã chọn chương trình: Xuất dữ liệu")
def phucHoiDuLieu():
    print("Đã chọn chương trình: Phục hồi dữ liệu")


def show_menu():
    while True:
        print("\n --------- QUẢN LÝ MÔN HỌC ----------")
        print("1. Hiển thị danh sách")
        print("2. Tìm kiếm hoặc lọc")
        print("3. Thêm mới ")
        print("4. Cập nhật")
        print("5. Xóa")
        print("6. Sắp xếp")
        print("7. Phân trang")
        print("8. Xem chi tiết")
        print("9. Xuất dữ liệu")
        print("10. Phục hồi dữ liệu")
        print("0. Thoát")

        try:
            chon = int(input("Mời nhập chương trình: "))
            
            if chon == 1:
                hienThi()
                
            elif chon == 2:
                timKiem()
                
            elif chon == 3:
                themMoi()

            elif chon == 4:
                capNhat()

            elif chon == 5:
                 xoa()

            elif chon == 6:
                sapXep()   

            elif chon == 7:
                 phanTrang()

            elif chon ==8:
                 xemChiTiet()

            elif chon == 9:
                 xuatDuLieu()

            elif chon == 10:
                 phucHoiDuLieu()
           
            elif chon == 0:
                print("Đã thoát chương trình")
                break
            else:
                print("Lựa chọn không hợp lệ, vui lòng thử lại.")
                
        except ValueError:
            print("Lựa chọn không hợp lệ, không được nhập ký tự, vui lòng thử lại đúng yêu cầu(1-5)")


show_menu()