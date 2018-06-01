from vpython import *

ball=sphere(pos=vector(-5,0,0) , radius=0.5 , color=color.cyan)
wallR = box(pos=vector(6,0,0),size=vector(0.2,12,12) , color=color.green)

ball.velocity= vector(10,0,0)

deltat= 0.05
t =0
#ball.pos = ball.pos + ball.velocity*deltat
while t <3:
    ball.pos = ball.pos + ball.velocity*deltat
    t = t + deltat
    rate(5000)
