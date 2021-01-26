#check out the f(x) function on line 34
#This calculator graphs the f(x) function and input is given in the code part

import math

xmin = -10
xmax = 10

ymin = -10
ymax = 10

rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    size(600 ,600)
    global xscl ,yscl
    xscl = width/rangex
    yscl = -height/rangey
    
    
def grid(xscl , yscl):
    strokeWeight(1)
    stroke(0,255,255)
    
    for i in range(xmin ,xmax+1):
        line(i*xscl ,ymin*yscl ,i*xscl ,ymax*yscl)
        line(xmin*xscl ,i*yscl ,xmax*xscl ,i*yscl)
        
    stroke(0)
    strokeWeight(2)
    line(xmin*xscl ,0 ,xmax*xscl ,0)
    line(0 ,ymax*yscl ,0 ,ymin*yscl)

def f(x):
    return math.cos(math.sin(x))

def graph_function():
    x = xmin
    while (x <= xmax):
        stroke(255 ,0 ,0)   #all subsequent shapes will follow color code defined by this function
        line(x*xscl ,f(x)*yscl ,(x+0.1)*xscl ,f(x + 0.1)*yscl)
        x += 0.1
    
def draw():
    global xscl ,yscl
    background(255)
    translate(height/2 ,width/2)
    grid(xscl ,yscl)
    graph_function()
    
    
