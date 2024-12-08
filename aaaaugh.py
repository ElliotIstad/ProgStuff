import tkinter as tk
import math
import time
 
root = tk.Tk()
canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
root.attributes("-fullscreen", True)
canvas.configure(background='#202020')
canvas.pack()
 
def draw_dot(x,y,radius):
    x2,y2=x+radius,y+radius
    canvas.create_oval(x,y,x2,y2,fill='red')
 
def draw_line(x1,y1,x2,y2,width):
    canvas.create_line(x1,y1,x2,y2,width=width)
 
 
angle = 30
speed = -30
radius = 10
lineW = 4
sizeX = root.winfo_screenheight()/4
sizeY = root.winfo_screenheight()/3.5
sizeZ = 50
 
o1 = (root.winfo_screenwidth()/2)
o2 = (root.winfo_screenheight()/2.5)
offset=[o1,o2]
 
def draw():
    vertices = []
 
    for i in range(1,5):
        pX = (math.cos(math.radians(angle+((i*2+1)*45)))*sizeX)+offset[0]
        pY = (math.sin(math.radians(angle+((i*2+1)*45)))*sizeZ)+offset[1]
        cords = [pX,pY]
        vertices.append(cords)
    for i in range(1,5):
        pX = (math.cos(math.radians(angle+((i*2+1)*45)))*sizeX)+offset[0]
        pY = (math.sin(math.radians(angle+((i*2+1)*45)))*sizeZ)+offset[1]+sizeY
        cords = [pX,pY]
        vertices.append(cords)
 
    draw_line(vertices[0][0],vertices[0][1],vertices[1][0],vertices[1][1],lineW)
    draw_line(vertices[1][0],vertices[1][1],vertices[2][0],vertices[2][1],lineW)
    draw_line(vertices[2][0],vertices[2][1],vertices[3][0],vertices[3][1],lineW)
    draw_line(vertices[3][0],vertices[3][1],vertices[0][0],vertices[0][1],lineW)
 
    draw_line(vertices[4][0],vertices[4][1],vertices[5][0],vertices[5][1],lineW)
    draw_line(vertices[5][0],vertices[5][1],vertices[6][0],vertices[6][1],lineW)
    draw_line(vertices[6][0],vertices[6][1],vertices[7][0],vertices[7][1],lineW)
    draw_line(vertices[7][0],vertices[7][1],vertices[4][0],vertices[4][1],lineW)
 
    draw_line(vertices[0][0],vertices[0][1],vertices[4][0],vertices[4][1],lineW)
    draw_line(vertices[1][0],vertices[1][1],vertices[5][0],vertices[5][1],lineW)
    draw_line(vertices[2][0],vertices[2][1],vertices[6][0],vertices[6][1],lineW)
    draw_line(vertices[3][0],vertices[3][1],vertices[7][0],vertices[7][1],lineW)
 
draw()
 
while 1:
    root.update()
    canvas.delete("all")
    angle+=speed/100
    draw()
    time.sleep(0.001)