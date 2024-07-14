# import clock
import turtle
import time
def clock():
    # Hàm tạo độ trễ 
    def custom_sleep(seconds):
        start = time.time() # Trả về thời gian hiện tại tính bằng giây
        while time.time() - start < seconds: # Chạy cho đến khi khoảng thời gian đã trôi qua bằng số giây yêu cầu
            pass

    # Hàm để lấy thời gian hiện tại từ hệ thống
    def get_current_time():
        now = time.localtime() # Trả về thời gian hiện tại
        hours = now.tm_hour
        minutes = now.tm_min  # (now.tm_hour, now.tm_min, now.tm_sec) truy xuất giờ, phút và giây từ struct_time
        seconds = now.tm_sec
        day = now.tm_mday
        month = now.tm_mon
        year =now.tm_year
        return f"{hours:02}:{minutes:02}:{seconds:02}\n{day}/{month}/{year}" # Định dạng thời gian thành chuỗi với hai chữ số (ví dụ: 09:05:03).

    # Thiết lập màn hình Turtle
    turtle_screen = turtle.Screen()
    turtle_screen.title("Đồng hồ tại đây")
    turtle_screen.bgcolor("black")

    # Thiết lập đối tượng Turtle để hiển thị thời gian
    actor_turtle = turtle.Turtle()
    actor_turtle.hideturtle()
    actor_turtle.color("pink")
    # actor_turtle.penup()
    actor_turtle.goto(0, 0)
    # actor_turtle.speed(0)

    def update_time():
        current_time = get_current_time() # Lấy thời gian hiện tại
        actor_turtle.clear() # Xóa thời gian cũ
        actor_turtle.write(current_time, align="center", font=("Courier", 40, "bold")) # In thời gian hiện tại
        turtle_screen.ontimer(update_time, 1000) # Cập nhật lại thời gian sau 1 giây

# Bắt đầu cập nhật thời gian
    update_time()
    turtle_screen.exitonclick()

# ---------------------------------------------------

namenv = []
register = []
log = []

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
                log.append(login)
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
            clock()
            print(f'{log} chấm công thành công')
            input('')
            namenv.append(log)
       

        if choice == "2":  # Tính ngày đi làm
            day = namenv.count(log)
            print(f"{log} đã đi làm được {day} ngày ")
            input('')
            
        if choice == "3":  # Tính lương
            print(f'tổng lương {log} làm được {day} và tổng lương là {day * 100} VNĐ')  # Giả sử mỗi ngày công là 100 VNĐ
            input('')
           
        if choice == "4":  # Thoát
            print("Thoát phần mềm.")
            log.clear()
            break

        

# Bắt đầu chương trình
dangki()
