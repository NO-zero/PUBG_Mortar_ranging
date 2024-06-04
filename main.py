import pynput
import pyautogui
import tkinter as tk

X = None
Y = None
A = None
B = None
C = None
D = None
Pressed = False
E = 0


def on_click(x, y, button, pressed):
    # 如果需要，你也可以在这里处理鼠标点击事件
    global X, Y, Pressed
    if pressed:
        print(f"{button} pressed at ({x}, {y})")
        X, Y = pyautogui.position()
        Pressed = True


# 更新标签显示的数字
def update_number_label(E):
    global A, B, C, D, X, Y, Pressed
    if Pressed and A is None and B is None and C is None and D is None:
        A = X
        B = Y
        Pressed = False
    if Pressed and A is not None and B is not None and C is None and D is None:
        C = X
        D = Y
        E = ((A - C) ** 2 + (B - D) ** 2) ** 0.5
        A = None
        B = None
        C = None
        D = None
        Pressed = False
    # 将标签的文本设置为新的数字
    number_label.config(text=str(round(E, 2)))
    # 安排下一次更新，数字加1，并延迟1000毫秒（1秒）
    root.after(100, update_number_label, E)


# 创建主窗口
root = tk.Tk()
root.title("屏幕右上角显示窗口")

# 设置窗口始终在最前面
root.attributes('-topmost', True)

# 设置窗口大小
window_width = 200
window_height = 100

# 获取屏幕分辨率并设置窗口位置
screen_width, screen_height = pyautogui.size()
root.geometry(f"{window_width}x{window_height}+{screen_width - 200}+{100}")

# 创建一个标签用于显示数字
number_label = tk.Label(root, font=("Arial", 24), text="0")  # 初始数字为0
number_label.pack(pady=20)  # 设置垂直填充和间距

# 启动数字更新循环，从0开始
update_number_label(0)

if __name__ == '__main__':
    listener = pynput.mouse.Listener(on_click=on_click)
    listener.start()
    # 运行Tkinter事件循环
    root.mainloop()
    listener.stop()