# Morris H. 12/7

from vpython import *


# initial perimeter setting
M, m, dt, g, h, v0, fs, t = 5, 1, 0.01, 9.8, 50, 30, 0.1, 0

# scene setting

scene = canvas(width=1000, height=600, align='left', range=120)

scene.camera.pos = vec(50, 60, 270)

floor = box(pos=vec(0, 0, 0), size=vec(1000, 1, 1000), color=color.blue)

building1 = box(pos=vec(110, h, 0), size=vec(200, 10, 10), 
                color=color.cyan, up=vec(0,1,0))

building2 = box(pos=vec(0, 50.5, 0), size=vec(20, 100, 50), 
                color=color.orange, up=vec(0,1,0,), v=vec(0, 0, 0), w=0)

ball = sphere(pos=vec(100, h+7.5, 0), radius=5, 
               color=vec(random(), random(), random()), v=vec(0, 0, 0))


# Using default value if user did NOT enter value

def test_none(h_tmp, v0_tmp, fs_tmp):

    if h_tmp == None: h_ans = h 
    elif (h_tmp > 90 or h_tmp < 10): h_ans = h
    else: h_ans = h_tmp

    if v0_tmp == None: v0_ans = v0
    else: v0_ans = v0_tmp

    if fs_tmp == None: fs_ans = fs
    else: fs_ans = fs_tmp

    return h_ans, v0_ans, fs_ans



# clean all ball
def clc_ball():
    global t, ball
    ball.visible = False

    building2.pos = vec(0, 50.5, 0) 
    building2.up=vec(0, 1, 0)
    building2.v=vec(0, 0, 0)
    building2.w=0
    # w.delete()
    t = 0

# generate ball

# ball = []
# i = 0

def gen_ball():
    clc_ball()
    global h, v0, fs, ball
    h, v0, fs = test_none(ipt_h.number, ipt_v0.number, ipt_fs.number)
    building1.pos.y = h
    ball = sphere(pos=vec(100, h+7.5, 0), radius=5, 
               color=vec(random(), random(), random()), v=vec(-v0, 0, 0))
    # ball.append(a)
    # i += 1


# initial condition setting

def init_setting():
    global h, v0, fs
    h, v0, fs = test_none(ipt_h.number, ipt_v0.number, ipt_fs.number)


# create widgets

scene.append_to_caption('      Height: ')
ipt_h = winput(bind=init_setting, type='numeric')
scene.append_to_caption(' (Enter a value between 10 to 90)\n\n\n')

scene.append_to_caption('      V0: ')
ipt_v0 = winput(bind=init_setting, type='numeric')
scene.append_to_caption(' \n\n\n')

scene.append_to_caption('      fs:')
ipt_fs = winput(bind=init_setting, type='numeric')
scene.append_to_caption('                                    ')

b1 = button(text="Shoot", bind=gen_ball, 
            background=color.purple)

b2 = button(text="Restart", bind=clc_ball, 
            background=color.purple)

scene.append_to_caption('\n\n')

scene.append_to_caption('<i>\n\n(Please press enter after setting each parameter to confirm the setting,\n otherwise it will run on default parameter)</i>')



# # calculate angular acc
# def angular_acc():
#     center = building2.pos.x
#     r = abs(-110-building2.pos.x)
#     I = (M*(20**2+100**2)/12 + M*(10**2+50**2))
#     if -100-center <= 10:
#         return M*g*r/I
#     elif -100-center > 10:
#         return -M*g*r/I
#     else:
#         return 0

# def angular_v(vx, r):
#     return vx/r


# plot

# g1 = graph(title='<b>Angular Velocity (for block)</b>', 
#            xtitle='<b>time</b>', ytitle='<b>Angular Velocity</b>', 
#            align='right', width=500, height=300)

# w = gdots(graph=g1)

while True:

    rate(1/dt)
    # when the ball hit the wall

    if ball.pos.x <= (building2.size.x + ball.radius)*0.5:

        I = M*(building2.size.x**2+building2.size.y**2)/12\
            + M*((building2.size.x/2)**2+building2.size.z**2)

        building2.w = dt*(2*m*ball.v.x/dt)*(h)/I - (M*g*building2.size.x/2)/I

        # prevent overturn
        if building2.w < 0:

            building2.w = 0

        ball.v.x *= -1

    # when wall hit bt the ball and start moving

    if building2.w > 0:

        building2.w += -(M*g*(building2.pos.x+10))/I

        # prevent over turn 

        if building2.w*dt >= (diff_angle(vec(0,1,0), building2.up)):

            building2.rotate(angle=diff_angle(vec(0,1,0), building2.up), origin=vec(-10, 0, 0), 
                             axis=vec(0, 0, 1))

    

    ball.pos += ball.v*dt

    building2.rotate(angle=-building2.w*dt, origin=vec(-10, 0, 0), 
                     axis=vec(0, 0, 1))

    t += dt

    # # plot
    # w.plot(pos=(t, building2.w))