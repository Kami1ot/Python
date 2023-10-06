import tkinter as tk
import time
import random
def close():
    global flag
    flag = False

winx = 800
winy = 600
win = tk.Tk()
win.title('rain')
win.config(width = winx, height = winy)
win.resizable(False,False) 
win.protocol("WM_DELETE_WINDOW",close)

canvas = tk.Canvas(win,highlightthickness=0)
canvas.place(anchor='center',width = winx, height = winxy)

def create_drop(n):
    obj_list = []
    for i in range(n):
        x0 = 10
        y0 = 10
        x1 = 20
        y1 = 40
        speedx = 0
        speedy = random.randint(1,4)
        color1 = 'blue'
        color2 = 'black'
        object = canvas.create_oval(x0,y0,x1,y1, fill = color1, outline = color2)
        config = {'drop': object,
                  'speedx': speedx,
                  'speedy': speedy}
        obj_list.append(config)
    return obj_list
n = 1        
drops = create_drop(n)
for i in range(n):
    
flag = True

while flag:
    
    
    
    win.update()
    time.sleep(0.01)
    
win.destroy()