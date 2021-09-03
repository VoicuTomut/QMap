
from project_qmap.tsp_solutions import get_minim_Brut
import numpy as np
import tkinter as tk
from tkinter import ttk
#from ttk import*
from tkinter import *
import time, sys
import  PIL
from PIL import ImageTk, Image

const_Lat1=44.431900
const_Long1=26.101470
# const_Lat2=
# const_Long2=

global m0
m0=100
global p0
p0=50
global m1
m1=200
global p1
p1=70
global m2
m2 = 65
global p2
p2 = 50
global m3
m3 = 150
global p3
p3 = 30
global m4
m4 = 160
global p4
p4 = 80
global m5
m5 = 90
global p5
p5 = 65

root=Tk()
root.title('Qmap')

title= tk.Label(root, text="Welkome to Qmap")
title.pack()

l1=tk.Label(root, text="Inputs")
l1.place(x=10,y=30)




def haversine_distance(lat1, lon1, lat2, lon2):
   r = 6371
   phi1 = np.radians(lat1)
   phi2 = np.radians(lat2)
   delta_phi = np.radians(lat2-lat1)
   delta_lambda = np.radians(lon2-lon1)
   a = np.sin(delta_phi / 2)**2 + np.cos(phi1) * np.cos(phi2) *   np.sin(delta_lambda / 2)**2
   res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1-a)))
   return np.round(res, 5)


def get_w(poz):
    nr_places=len(poz)
    w = np.zeros((nr_places, nr_places))
    for i in range(nr_places):
        for j in range(i + 1, nr_places):
            w[i][j] = haversine_distance(poz[i][0], poz[i][1], poz[j][0], poz[j][1])
            w[j][i] = haversine_distance(poz[i][0], poz[i][1], poz[j][0], poz[j][1])
    return w

def ceva():
    a ="Ai ales "
    b ="Carturesti "
    c ="Legalize it "
    d="Muzeul Bancii Nationale"
    e="St Patrick Pub"
    f="Muzeul de Istorie"
    g="Spital"
    j=""
    if (var1.get() == 1):
        j+=b
        l3.config(text=j)
        #cl=create_circle(100, 50, 10, canvas)
        canvas.create_image(m0, p0, anchor=NW, image=test3)
    elif (var1.get() == 0 or var2.get() == 0 or var3.get() == 0 or var3.get() == 0 or var4.get() == 0 or var5.get() == 0) or var6.get() == 0:
        #canvas.delete(test3)
        canvas.create_image(50, 10, anchor=NW, image=img)
        l3.config(text='')
    if (var2.get() == 1):
        j+=c
        l3.config(text=j)
        #canvas.create_line(110, 50, 210, 70)
        #create_circle(200, 70, 10, canvas)
        canvas.create_image(m1, p1, anchor=NW, image=test3)
    if (var3.get() == 1):
        j+=d
        l3.config(text=j)
        #create_circle(65, 50, 10, canvas)
        canvas.create_image(m2, p2, anchor=NW, image=test3)
    if (var4.get() == 1):
        j+=e
        l3.config(text=j)
        #create_circle(150, 30, 10, canvas)
        canvas.create_image(m3, p3, anchor=NW, image=test3)
    if (var5.get() == 1):
        j+=f
        l3.config(text=j)
        #create_circle(150, 80, 10, canvas)
        canvas.create_image(m4, p4, anchor=NW, image=test3)
    if (var6.get() == 1):
        j += g
        l3.config(text=j)
        #create_circle(90, 70, 10, canvas)
        canvas.create_image(m5,p5, anchor=NW, image=test3)

var1=IntVar()
c1=tk.Checkbutton(root,text="Carturesti",variable=var1, onvalue=1,offvalue=0,command=ceva)
c1.place(x=10,y=60)

var2=IntVar()
c2=tk.Checkbutton(root,text="Legalize it",variable=var2, onvalue=1,offvalue=0,command=ceva)
c2.place(x=10,y=90)

var3=IntVar()
c3=tk.Checkbutton(root,text="Muzeul Bancii Nationale",variable=var3, onvalue=1,offvalue=0,command=ceva)
c3.place(x=10,y=120)

var4=IntVar()
c4=tk.Checkbutton(root,text="St Patrick Pub",variable=var4, onvalue=1,offvalue=0,command=ceva)
c4.place(x=10,y=150)

var5=IntVar()
c5=tk.Checkbutton(root,text="Muzeul de Istorie",variable=var5, onvalue=1,offvalue=0,command=ceva)
c5.place(x=10,y=180)

var6=IntVar()
c6=tk.Checkbutton(root,text="Spital",variable=var6, onvalue=1,offvalue=0,command=ceva)
c6.place(x=10,y=210)

image1= Image.open("centruVechi.jpg")
test = ImageTk.PhotoImage(image1)
#l2=tk.Label(root,image=test)
#l2.image = test
#l2.place(x=100,y=40)

image2= Image.open("logo.jpg")
resize_img2= image2.resize((100,40))
test2 = ImageTk.PhotoImage(resize_img2)
l4=tk.Label(root,image=test2)
l4.image = test2
l4.place(x=5,y=5)
#l4.pack()

l3 = tk.Label(root)
l3.place(x=120, y=250)

def create_circle(x, y, r, canvas):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1)

canvas = Canvas(root, width = 400, height = 200)
canvas.place(x=165,y=40)
img = ImageTk.PhotoImage(Image.open("centruVechi.jpg"))
canvas.create_image(50, 10, anchor=NW, image=img)
#canvas.create_line(110, 50, 210, 70)
# canvas.create_line(200, 25, 60, 100)
# cl=create_circle(100,50,10,canvas)
# canvas.delete(cl)

image3= Image.open("pin.jpg")
resize_img3= image3.resize((30,20))
test3 = ImageTk.PhotoImage(resize_img3)
#img= ImageTk.PhotoImage(Image.open("pin.jpg"))
#canvas.create_image(100, 100, anchor=NW, image=test3)

def click():
    canvas.create_line(m0+10, p0, m1+10, p1)


but1= tk.Button(root, text="Start", bg='red', command=click)
but1.place(x=480,y=100)

algoritmi=["1","2","3"]
#algoritmiS=tk.StringVar()

def comb_command(event):
    if event.widget.get()=="1":
        print("Ai ales 1")
    elif event.widget.get()=="2":
        print("Ai ales 2")
    elif event.widget.get()=="3":
        print("Ai ales 3")

comb= ttk.Combobox(root, values=algoritmi)
comb.place(x=480,y=140)
#comb['values']=algoritmi
comb['state'] = 'readonly'

comb.bind('<<ComboboxSelected>>', comb_command)

root.geometry('650x300')
root.mainloop()