import threading 
import time

def task(name):
    print(f"{name} bắt đầu")
    time.sleep(4)  # giả lập công việc mất 4 giây
    print(f"{name} xong")

# Tạo 2 thread
t1 = threading.Thread(target=task, args=("Tác vụ 1",))
t2 = threading.Thread(target=task, args=("Tác vụ 2",))

# Bắt đầu thread
t1.start()
t2.start()

# Chờ cả 2 xong
t1.join()
t2.join()

print("Hoàn thành tất cả tác vụ")
