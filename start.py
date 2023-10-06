import time
import tkinter as tk
import random
color_list = ['red', 'blue', 'green', 'purple','navy', 'orange']
def close():
    global running
    running = False
    
def create_odj(n):
    obj_list = []
    for i in range(n):
        x = random.randint(0, winx- 200)
        y = random.randint(0, winx- 200)
        r = 10 
        speedx = random.randint(1,4) 
        speedy = random.randint(1,4)
        color1 = random.choice(color_list)
        color2 = random.choice(color_list)
        object = canvas.create_oval(x - r,y - r, x + r , y + r,fill = color1,outline = color2, width=2)
        config = {'obj': object,
                  'speedx': speedx,
                  'speedy': speedy}
        obj_list.append(config)
    return obj_list
    
win = tk.Tk()
winx = 600
winy = 400
win.title('tk application')
win.config (width = winx, height = winy)
win.resizable(False,False)
win.protocol ("WM_DELETE_WINDOW",close)

canvas = tk.Canvas(win, highlightthickness=0)
canvas.place(x = 0, y = 0, width = winx, height = winy)

odj = create_odj(50)


running = True

while running:
    for config in odj:
        cords = canvas.coords(config['obj'])
        if cords[0] < 0 or cords[2] > winx:
            config['speedx'] = -config['speedx']
        if cords[1] < 0 or cords[3] > winy:
            config['speedy'] = -config['speedy']
        canvas.move (config['obj'], config['speedx'], config['speedy'])
    win.update()
    time.sleep(0.01)
    
    
win.destroy()


