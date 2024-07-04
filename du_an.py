# Khởi tạo các biến toàn cục
namenv = []
timenv = []
frequency = {}
register = []

def dangki():  # Đăng kí thông tin
    while True:
        print("************** \\_/  *************")
        print("*************  0 0   *************")
        print("************* >( )<  *************")
        print("************ >(   )< *************")
        print("*************  ***   ************")
        print("*************   *    ************")

        print('1. Đăng nhập')
        print('2. Đăng kí')
        print('3. Thoát')
        choicedk = input('Nhập lựa chọn của bạn: ')
        
        if choicedk == '2':  # Đăng kí người dùng mới
            reg = input('Nhập thông tin đăng kí: ')
            if reg in register:
                print(f'Tên "{reg}" đã bị trùng.')
                input('Nhấn Enter để tiếp tục...')
            else:
                if reg:
                    register.append(reg)
                    print(f'{reg} đã được đăng ký thành công.')
                    input('Nhấn Enter để tiếp tục...')
        
        elif choicedk == '3':  # Thoát
            print('Thoát chương trình')
            break
        
        elif choicedk == '1':  # Đăng nhập
            login = input('Đăng nhập tên nhân viên: ')
            if login in register:  # Nếu tên đã đăng kí, truy cập vào giao diện
                input('Đăng nhập thành công')
                giaodien()
            else:
                print('Tên của bạn chưa được đăng kí.')
                input('Nhấn Enter để tiếp tục...')

def giaodien():  # Giao diện và chấm công
    while True:
        print("=== ỨNG DỤNG CHẤM CÔNG ===")
        print("1. Chấm công")
        print("2. Xem danh sách chấm công") 
        print('3. Tính lương')
        print("4. Thoát")
        
        choice = input("Chọn một tùy chọn: ")

        if choice == "1":  # Chấm công
            name = input("Nhập tên nhân viên: ")
            if name in register:
                namenv.append(name)
                print(f"Đã chấm công cho nhân viên {name}")
            else:
                print('Tên của bạn chưa được đăng kí')
                dangki()

        elif choice == "2":  # Tính ngày đi làm
            for item in namenv:
                if item in frequency:
                    frequency[item] += 1
                else:
                    frequency[item] = 1
            name_ds = input('Nhập tên nhân viên để hiển thị danh sách: ')
            if name_ds in frequency:  # Hiển thị danh sách chấm công
                print(f"{frequency[name_ds]} ngày")
            else:
                print(f"'{name_ds}' không có trong danh sách.")
            input('Nhấn Enter để tiếp tục...')

        elif choice == "3":  # Tính lương
            tinh_luong = input('Nhập tên nhân viên để tính lương: ')
            if tinh_luong in frequency:
                print(f'Số ngày làm việc: {frequency[tinh_luong] * 100} VNĐ')  # Giả sử mỗi ngày công là 100 VNĐ
            else:
                print(f'Nhân viên {tinh_luong} không có trong danh sách chấm công.')
            input('Nhấn Enter để tiếp tục...')

        elif choice == "4":  # Thoát
            print("Thoát phần mềm.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
            input('Nhấn Enter để tiếp tục...')

# Bắt đầu chương trình
dangki()
