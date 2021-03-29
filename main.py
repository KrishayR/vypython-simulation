from vpython import *
canvas(background=color.purple)
bball = sphere(pos=vector(0,0,0),radius=0.25,color=color.orange)
backboard = box(pos=vector(2,0,0),size=vector(0.1,1,1),color=color.white)
backboard2 = box(pos=vector(-2,0,0),size=vector(0.1,1,1),color=color.white)
rim1 = ring(pos=vector(0,0,0),thickness=0.1,color=color.red)
rim2 = ring(pos=vector(0.5,0,0),thickness=0.1,color=color.red)
rim3 = ring(pos=vector(-0.5,0,0),thickness=0.1,color=color.red)
rim4 = ring(pos=vector(1,0,0),thickness=0.1,color=color.red)
rim5 = ring(pos=vector(-1,0,0),thickness=0.1,color=color.red)

dx = 0.2

while True :
    rate(30)
    
    if bball.pos.x >= 1.8 or bball.pos.x <= -1.8:
        dx = -dx
        
    
    bball.pos.x += dx
