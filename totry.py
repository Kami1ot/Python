import tkinter as tk
from math import cos, sin, radians

root = tk.Tk()
root.geometry("500x500")

canvas = tk.Canvas(root, background="black")
canvas.pack(fill="both",expand=True)

def create_circle(x, y, r, canvasName):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, outline='red')

def move(angle):
    if angle >=360:
        angle = 0
    x = 200 * cos(radians(angle))
    y = 200 * sin(radians(angle))
    angle+=1
    canvas.coords(plane, 250+x, 250+y)
    root.after(10, move, angle)

create_circle(250, 250, 200, canvas)
plane = create_circle(450,250,20,canvas)

root.after(10, move, 0)

root.mainloop()