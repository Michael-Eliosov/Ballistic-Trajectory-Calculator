import numpy as np
from math import *
from tkinter import *
from time import *

g=9.81
w=0
m=1
t=10000 # simulation step

class Projectile:
    def __init__(self,speed,angle,canvas,color,resistance):
        self.resistance=resistance
        self.V=np.array([[speed*cos(radians(angle))],[speed*sin(radians(angle))]]).dot(1/sqrt(t))
        self.canvas=canvas
        self.id = canvas.create_oval(0,980,20,1000, fill=color)
    def draw(self):
        global g,m
        pos=canvas.coords(self.id)
        canvas.create_oval(pos[0]+9,pos[1]+9,pos[2]-9,pos[3]-9,fill='blue')
        self.canvas.move(self.id,self.V[0][0],-self.V[1][0])
        self.V = self.V.dot(1-self.resistance/(m*t))
        self.V[0][0] -= self.resistance*w/t
        self.V[1][0] -= g/t

master=Tk()
canvas=Canvas(master, width=1000, height=1000, bd=0, highlightthickness=0)
canvas.pack()

Ball1 = Projectile(90,45,canvas,'red',0)
Ball2 = Projectile(90,45,canvas,'green',10)

while 1:
    Ball1.draw()
    Ball2.draw()
    canvas.update()
    sleep(1/t)
