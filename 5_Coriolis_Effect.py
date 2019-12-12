# Morris H. 12/10

from vpython import *

# perimeter

earth_r = 6.371E6

earth_m =  5.9724E24

theta = radians(45)

v0 = 6000

T = 86400

G = 6.67408E-11

omg = 2*pi/T*5

# scene setting

scene = canvas(title='<font size=30><center><i>Coriolis Effect\n</i></center></font>', 
               width=1600, height=1300, align='left', range=200)

scene.range = earth_r*1.5

# display earth

earth = sphere(radius=earth_r, texture=textures.earth, up=vec(0, 1, 0), pos=vec(0, 0, 0))

# ball

ball1 = sphere(radius=earth_r/50, pos=vec(0, 0, earth_r+earth_r/100), make_trail=True,

              v=vec(0, v0*cos(theta), v0*sin(theta)), a=vec(0, 0, 0), color=color.red)

ball2 = sphere(radius=earth_r/50, pos=vec(0, 0, earth_r+earth_r/100), make_trail=True,

              v=vec(0, -v0*cos(theta), v0*sin(theta)), a=vec(0, 0, 0), color=color.blue)

ball3 = sphere(radius=earth_r/50, pos=vec(0, 0, earth_r+earth_r/100), make_trail=True,

              v=vec(0, v0*cos(theta), v0*sin(theta)), a=vec(0, 0, 0))

ball4 = sphere(radius=earth_r/50, pos=vec(0, 0, earth_r+earth_r/100), make_trail=True,

              v=vec(0, -v0*cos(theta), v0*sin(theta)), a=vec(0, 0, 0))


ball = [ball1, ball2, ball3, ball4]

# plot

g1 = graph(title='horizontal motion', align='right', xtitle='<b>X(km)</b>', ytitle='<b>Y(km)</b>', 
           width=1400, height=600)

x1 = gdots(graph=g1, color=color.red)

x2 = gdots(graph=g1, color=color.blue)

# calculate force

def acc():
    return -G*earth_m*(ball[i].pos)/mag(ball[i].pos)**3 + 2*cross(vec(0, omg, 0), ball[i].v)

def cmp_acc():
    return -G*earth_m*(ball[i].pos)/mag(ball[i].pos)**3

# sim

t, dt = 0, 1

while True:

    rate(100)

    # earth rotate

    # earth.rotate(angle=2*pi/T*dt, axis=vec(0, 1, 0))

    # ball motion

    if mag(ball[0].pos) >= (earth_r + ball[0].radius*0.5):

        i = 0

        ball[0].a = acc()

        ball[0].v += ball[0].a*dt

        ball[0].pos += ball[0].v*dt

        x1.plot(pos=(ball[0].pos.x/1000, ball[0].pos.y/1000))

    if mag(ball[1].pos) >= (earth_r + ball[1].radius*0.5):

        i = 1

        ball[1].a = acc()

        ball[1].v += ball[1].a*dt

        ball[1].pos += ball[1].v*dt

        x2.plot(pos=(ball[1].pos.x/1000, ball[1].pos.y/1000))

    
    for i in range(2,4):

        if mag(ball[i].pos) >= (earth_r + ball[i].radius*0.5):

            ball[i].a = cmp_acc()

            ball[i].v += ball[i].a*dt

            ball[i].pos += ball[i].v*dt
    
    t += dt