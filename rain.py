import tkinter as tk
import time
from math import cos,sin,radians
import random

color_list = ['red', 'blue', 'green', 'purple','navy', 'orange','black','white']

def close():
    global running
    running = False  
    
def color_change():
    color1 = random.choice(color_list)
    canvas.itemconfig(c2,fill = color1)

win = tk.Tk()
winx = 600
winy = 600
win.title('tk application')
win.config (width = winx, height = winy)
win.geometry('600x600')
win.resizable(True,True)
win.protocol ("WM_DELETE_WINDOW",close)

canvas = tk.Canvas(win, highlightthickness=0)
canvas.place(x = 0, y = 0, width = winx, height = winy)


    
def create_obj(x,y,r, canvasname, color=''):
    return canvasname.create_oval(x-r,y-r,x+r,y+r,fill = color, outline = 'black')


c1 = create_obj(300,300,200,canvas)
c2 = create_obj(300,100,20,canvas,'black')
angle = 0


btn1 = tk.Button(canvas,text= 'CHANGE COLOR', command= color_change)
btn1.pack(expand=False,ipadx=20,ipady=0.1)

btn3 = tk.Button(canvas,text= 'EXIT', command=close)
btn3.pack(expand=False,ipadx=20,ipady=0.1)


running = True

while running:
    if angle >= 360:
        angle = 0
    canvas.move(c2,200*cos(radians(angle))/58,200*sin(radians(angle))/58)  

    angle+=1
    win.update()
    time.sleep(0.01)
    
    
    
win.destroy()
    
