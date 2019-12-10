# Morris 2019/11/21

from vpython import *


############################################################################################

k, m, g = 1, 5, 9.8
critical, under, over = 2*m*(k/m)**0.5, 0.2, 10


############################################################################################

scene = canvas(title='Spring in Water', width=1600, height=900, background=vec(0, 0.6, 0.6),
               align='left')
scene.camera.pos = vec(-35, 80, 90)
scene.camera.axis = vec(25, -60, -90)

############################################################################################

A = vertex(pos=vec(50, 40, 17), color=color.green, opacity=0.2)
B = vertex(pos=vec(50, 40, -17), color=color.green, opacity=0.2)
D = vertex(pos=vec(-50, 40, 17), color=color.green, opacity=0.2)
C = vertex(pos=vec(-50, 40, -17), color=color.green, opacity=0.2)

E = vertex(pos=vec(50, -35, 17), color=color.green, opacity=0.2)
F = vertex(pos=vec(50, -35, -17), color=color.green, opacity=0.2)
H = vertex(pos=vec(-50, -35, 17), color=color.green, opacity=0.2)
G = vertex(pos=vec(-50, -35, -17), color=color.green, opacity=0.2)

S1 = quad(v0=E, v1=F, v2=G, v3=H)
S2 = quad(v0=A, v1=B, v2=E, v3=H)
S3 = quad(v0=B, v1=C, v2=F, v3=E)
S4 = quad(v0=C, v1=D, v2=G, v3=F)
S5 = quad(v0=D, v1=A, v2=H, v3=G)

############################################################################################

spring = helix(pos=vec(-30, 33, 0), axis=vec(0, 37, 0), radius=3,
               coil=30, v=vec(0, 0, 0), a=vec(0, -35*k/m, 0))

block = box(pos=vec(-30, 35, 0), size=vec(7, 7, 7), color=color.blue,
            v=vec(0, 0, 0), a=vec(0, -35*k/m, 0))

spring2 = helix(pos=vec(0, 33, 0), axis=vec(0, 37, 0), radius=3, coil=30,
                v=vec(0, 0, 0), a=vec(0, -35*k/m, 0))

block2 = box(pos=vec(0, 35, 0), size=vec(7, 7, 7), color=color.red, v=vec(0, 0, 0),
             a=vec(0, -35*k/m, 0))

spring3 = helix(pos=vec(30, 33, 0), axis=vec(0, 37, 0), radius=3, coil=30, v=vec(0, 0, 0),
                a=vec(0, -35*k/m, 0))

block3 = box(pos=vec(30, 35, 0), size=vec(7, 7, 7), color=color.green, v=vec(0, 0, 0),
             a=vec(0, -35*k/m, 0))

water = box(pos=vec(0, 0, 0), size=vec(100, 70, 34), color=vec(0, 0, 1), opacity=0.2)

celling = box(pos=vec(0, 70, 0), size=vec(100, 2, 34), color=vec(0.3, 0.3, 0.3))

sep1 = box(pos=vec(-15,2.5,0), size=vec(1,70,34), color=color.green)

sep2 = box(pos=vec(15,2.5,0), size=vec(1,70,34), color=color.green)

############################################################################################

g1 = graph(title='Position', xtitle='t', ytitle='position', align='right', width=1300,
           height=800)

yt = gcurve(graph=g1, color=color.blue)
y2t = gcurve(graph=g1, color=color.red)
y3t = gcurve(graph=g1, color=color.green)

############################################################################################

dt = 0.01
t = 0

while t<45:
    rate(300)
    block.a.y = -k*block.pos.y - block.v.y*under
    block.v.y += block.a.y*dt
    block.pos.y += block.v.y*dt
    block2.a.y = -k*block2.pos.y - block2.v.y*critical
    block2.v.y += block2.a.y*dt
    block2.pos.y += block2.v.y*dt
    block3.a.y = -k*block3.pos.y - block3.v.y*over
    block3.v.y += block3.a.y*dt
    block3.pos.y += block3.v.y*dt

    spring.a.y = -k*spring.pos.y - spring.v.y*under
    spring.v.y += spring.a.y*dt
    spring.pos.y += spring.v.y*dt
    spring2.a.y = -k*spring2.pos.y - spring2.v.y*critical
    spring2.v.y += spring2.a.y*dt
    spring2.pos.y += spring2.v.y*dt
    spring3.a.y = -k*spring3.pos.y - spring3.v.y*over
    spring3.v.y += spring3.a.y*dt
    spring3.pos.y += spring3.v.y*dt

    spring.axis.y = spring.axis.y - spring.v.y*dt
    spring2.axis.y = spring2.axis.y - spring2.v.y*dt
    spring3.axis.y = spring3.axis.y - spring3.v.y*dt
    yt.plot(pos=(t, block.pos.y))
    y2t.plot(pos=(t, block2.pos.y))
    y3t.plot(pos=(t, block3.pos.y))
    t += dt
