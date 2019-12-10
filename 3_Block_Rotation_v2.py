# Morris H. 12/7

from vpython import *
from random import *

# initial perimeter setting
m, M, theta, v0, e, g = 2, 90, 0, 150, 1, 98
theta *= pi/180

# scene setting
def set_scene():
    global scene
    scene = canvas(title='<font size=30><center><i>Block Rotation\n</i></center></font>', 
                   width=1600, height=1000, align='left', range=200)
    floor = box(pos=vec(0, 0, 0), size=vec(1000, 1, 1000), color=color.blue)
    building1 = box(pos=vec(100, 50, 0), size=vec(10, 100, 10), color=color.cyan, 
                    up=vec(0,1,0))
    # building2 = box(pos=vec(-100, 50, 0), size=vec(20, 100, 50), color=color.orange, 
    #                 up=vec(0,1,0,), v=vec(0, 0, 0))
    scene.camera.pos = vec(0, 60, 250)
set_scene()
building2 = box(pos=vec(-100, 50.5, 0), size=vec(20, 100, 50), color=color.orange, 
    up=vec(0,1,0,), v=vec(0, 0, 0), w=0)


# generate ball
ball = []
i = 0
def gen_ball():
    global i
    a = sphere(pos=vec(100, 105, 0), radius=5, color=vec(randint(0, 100)/100, randint(0, 100/100), randint(0, 100)/100), 
               v=vec(-v0*cos(theta), v0*sin(theta), 0), a=vec(0, -g, 0))
    ball.append(a)
    i += 1
gen_ball()

# set theta
def set_theta(t):
    txt1.text = t.value
    
# set v0
def set_v0(v):
    txt2.text = v.value

# shoot
def shoot():
    global v0
    v0 += 10
    gen_ball()
    ball[i-1].v = vec(-v0*cos(s1.value*pi/180), 
                      v0*sin(s1.value*pi/180), 0)

# go
go = False
def Go(b):
    global go
    go = not go
    if go: b.text = "<font size=25>Stop</font>"
    else: b.text = "<font size=25>Go</font>"
    # while building2.up != vec(-1, 0, 0):
    #     gen_ball()
    #     ball[i-1].v = vec(-v0*cos(s1.value*pi/180), 
    #                     v0*sin(s1.value*pi/180), 0)
    #     v0 += 10
    #     sleep(5)

# set e
def set_e(g):
    # global e
    # e = g.value
    txt0.text = g.value

# clean all ball
def clc_ball():
    global t
    # print(len(ball))
    if len(ball) != 0:
        for j in range(len(ball)):
            ball[j].visible = False
    building2.pos = vec(-100, 50.5, 0) 
    building2.up=vec(0, 1, 0)
    building2.v=vec(0, 0, 0)
    building2.w=0
    w.delete()
    t = 0


# create widgets
scene.append_to_caption('      <font size=15>e: </font>')
s0 = slider(min=0.7, max=1, value=1, length=300, bind=set_e, 
            right=15, width=20)
txt0 = wtext(text=s0.value)
scene.append_to_caption(' \n\n\n')

scene.append_to_caption('      <font size=15>Angle: </font>')
s1 = slider(min=0, max=80, value=0, length=300, bind=set_theta, 
            right=15, width=20)
txt1 = wtext(text=s1.value)
scene.append_to_caption(' Degree\n\n\n')

scene.append_to_caption('      <font size=15>V0: </font>            ')
txt2 = wtext(text=v0)

scene.append_to_caption('\n\n\n                                    ')
b1 = button(text="<font size=25>Go</font>", bind=Go, background=color.purple)

b2 = button(text="<font size=25>Restart</font>", bind=clc_ball, background=color.purple)
scene.append_to_caption('\n\n\n\n\n\n')

# calculate collide speed
def collide(m, M, v1, v2):
    v1f = (m*v1 + M*v2 + s0.value*M*(v2 - v1))/(m + M)
    v2f = (m*v1 + M*v2 + s0.value*m*(v1 - v2))/(m + M)
    return v1f, v2f


# calculate angular acc
def angular_acc():
    center = building2.pos.x
    r = abs(-110-building2.pos.x)
    I = (M*(20**2+100**2)/12 + M*(10**2+50**2))
    if -100-center <= 10:
        return M*g*r/I
    elif -100-center > 10:
        return -M*g*r/I
    else:
        return 0

def angular_v(vx, r):
    return vx/r


# plot
g1 = graph(title='<b>Angular Velocity (for block)</b>', 
           xtitle='<b>time</b>', ytitle='<b>Angular Velocity</b>', align='right', 
           width=1000, height=600)

w = gdots(graph=g1)

t, dt = 0, 0.01
while True:
    rate(1/dt)
    if go:
        for j in range(len(ball)):

            # motion when hit thte ground
            if ball[j].pos.y <= 5.5  and ball[j].pos.x >= -85:
                ball[j].v.y *= -s0.value
                ball[j].v += ball[j].a*dt
                ball[j].pos += ball[j].v*dt

                # if the velocity is too slow, stay on the ground
                if ball[j].v.y <= 0.1:
                    ball[j].pos.y = 5.5

            # motion when hit the block
            elif ball[j].pos.x <= -85 and ball[j].v.x <= 0 and ball[j].pos.y <= 100 and ball[j].pos.x >= -115 and building2.up == vec(0, 1, 0):
                
                v1f, v2f = collide(m, M, ball[j].v.x, building2.v.x)
                # motion of ball
                ball[j].v.x = v1f
                ball[j].v += ball[j].a*dt
                ball[j].pos += ball[j].v*dt

                # motion of block
                building2.w = angular_v(v2f, ball[j].pos.y-0.5)
                dtheta = -building2.w*dt
                building2.rotate(origin=vec(-110, 0, 0), axis=vec(0, 0, 1), 
                                angle=dtheta)
                
                shoot()
                txt2.text = v0
                             
            
            # motion when in the air
            else:
                ball[j].v += ball[j].a*dt
                ball[j].pos += ball[j].v*dt

                
                building2.w += angular_acc()*dt
                dtheta = -building2.w*dt

                rotate_max = degrees(diff_angle(vec(0,1,0), building2.up))

                # prevent over turn
                if dtheta > rotate_max:
                    dtheta = rotate_max
                
                # when the block hit the ground
                if building2.pos.y <= 10.5:
                    building2.w = 0
                    # building2.pos = vec(-160, 10.5, 0)
                    building2.up = vec(-1, 0, 0)
                    dtheta = 0
                    
                    # stop shooting
                    go = not go
                    clc_ball()

                if building2.pos.x > -100:
                    # building2.pos = vec(-100, 50.5, 0) 
                    building2.up = vec(0, 1, 0)
                    building2.w = 0
                    dtheta = 0

                building2.rotate(origin=vec(-110, 0, 0), axis=vec(0, 0, 1), 
                                angle=dtheta)
                

        t += dt

        # plot
        w.plot(pos=(t, building2.w))



            

