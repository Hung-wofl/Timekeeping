import turtle
import time

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
    # custom_sleep(0.5) # Tạo độ trễ 1 giây
    turtle_screen.ontimer(update_time, 1000) # Cập nhật lại thời gian sau 1 giây

# Bắt đầu cập nhật thời gian
# update_time()
turtle_screen.exitonclick()

