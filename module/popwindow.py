'''
本模块参考的是[kic8462852](https://gitee.com/kic8462852/gui)的[GUI](https://gitee.com/kic8462852/gui)项目，感谢Ta分享的源码:)
该项目的许可证是[木兰宽松许可证， 第2版 2020年1月 ](http://license.coscl.org.cn/MulanPSL2)
'''

import tkinter, sys, time, threading

windowsize = '60x40+'

root = tkinter.Tk()
root.overrideredirect(True)
root.attributes("-alpha", 0.8)
root.wm_attributes('-topmost', 1)
root.geometry(windowsize+"1200+100") # 第一个参数是设置窗口大小
tkinter.Label(root,
              justify='left',
              font=(None, 12),
              text='译排').place(x=0, y=0)
all_y = root.winfo_screenheight()
all_x = root.winfo_screenwidth()
print(all_x)
x, y = 0, 0
rootalpha = 0.1
is_hide = 'right'


def get_pos(event):
    global x, y
    x, y = event.x, event.y

# 响应鼠标拖动

def window_move(event):
    global x, y
    new_x = min(all_x - 160, (event.x - x) + root.winfo_x())
    new_y = max(0, (event.y - y) + root.winfo_y())
    root.geometry(windowsize + str(new_x) + "+" + str(new_y))


def change_alpha(event):
    global rootalpha
    if rootalpha == 0.1: rootalpha = 0.8
    else: rootalpha = 0.1
    root.attributes("-alpha", rootalpha)


def close(event):
    root.destroy()
    sys.exit()


def move_3(a, b, root=root):
    global lab
    while root.winfo_x() < all_x - 40 and is_hide == 'right':
        root.geometry(windowsize + str(root.winfo_x() + 4) + "+" +
                      str(root.winfo_y()))
        time.sleep(0.001)
    while root.winfo_x() > all_x - 160 and is_hide == 'left':
        root.geometry(windowsize + str(root.winfo_x() - 4) + "+" +
                      str(root.winfo_y()))
        time.sleep(0.001)
    while root.winfo_y() >= 40 - 200 and is_hide == 'up':
        root.geometry(windowsize + str(root.winfo_x()) + "+" +
                      str(root.winfo_y() - 5))
        time.sleep(0.001)
    while root.winfo_y() < 0 and is_hide == 'down':
        root.geometry(windowsize + str(root.winfo_x()) + "+" +
                      str(root.winfo_y() + 5))
        time.sleep(0.001)


def move_1(event):
    global is_hide
    if root.winfo_x() >= all_x - 160 and str(event.type) == 'Leave':
        is_hide = 'right'
    elif root.winfo_x() <= all_x - 40 and str(
            event.type) == 'Enter' and not is_hide in 'updown':
        is_hide = 'left'
    elif 0 >= root.winfo_y() >= 40 - 200 and str(event.type) == 'Leave':
        is_hide = 'up'
    elif root.winfo_y() <= 0 and str(event.type) == 'Enter':
        is_hide = 'down'
    else:
        pass
    threading.Thread(target=move_3,
                     args=(root.winfo_x(), root.winfo_y())).start()


root.bind("<B1-Motion>", window_move)
root.bind("<Button-1>", get_pos)

root.bind("<Double-Button-1>", change_alpha)
root.bind("<Double-Button-3>", close)

root.bind("<Leave>", move_1)
root.bind("<Enter>", move_1)

root.mainloop()
