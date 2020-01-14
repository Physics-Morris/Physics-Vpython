# Morris H. 12/6



from vpython import *


# 初始值設定



M, m, g, theta, k = 3.0, 1.0, 9.8, 45, 0.0





# 物體運動公式，當摩擦係數大於tan斜坡角度時，物體不會運動



def acc(theta, k, M, m):

    theta = radians(theta)

    if k >= tan(theta):

        a_m, a_M, m_a_x, m_a_y, M_a_x = 0.0, 0.0, 0.0, 0.0, 0.0

    else:

        a_m = g/(M*(cos(theta)**2 + k*sin(theta)*cos(theta))/(m + M)/(sin(theta) - k*cos(theta))+ sin(theta))

        a_M = m*cos(theta)/(m+M)*a_m



        m_a_x = a_m*cos(theta)-a_M

        m_a_y = -a_m*sin(theta)

        M_a_x = -a_M

    return m_a_x, m_a_y, M_a_x

    

m_a_x, m_a_y, M_a_x = acc(theta, k, M, m)



# 場景設定

def set_scene():

    global scene

    scene = canvas(width=1000, height=300, align='left')

    scene.camera.pos = vec(30, 10, 40)

    scene.camera.axis = vec(-5, -10, -30)

set_scene()



running = False

def Run(r):

    global running

    running = not running

    if running: 

        r.text = "Pause"

    else: 

        r.text = "Run"



def restart():

    theta_tmp, friction_tmp, M_tmp, m_tmp = s1.number, s2.number, s0.number, s3.number
    if theta_tmp == None: theta_tmp = theta
    if friction_tmp == None: friction_tmp = k
    if M_tmp == None: M_tmp = M
    if m_tmp == None: m_tmp = m

    global running

    global t 

    running = False

    b1.text = "Run"

    t = 0

    m_v.delete()

    M_v.delete()

    # m_p.delete()

    # M_p.delete()

    total_E.delete()

    m_E.delete()

    M_E.delete()

    A.pos, B.pos, C.pos, D.pos, E.pos, F.pos = vec(0, 0, 0), vec(10/tan(radians(theta_tmp)), 0, 0), vec(10/tan(radians(theta_tmp)), 0, 10), vec(0, 0, 10), vec(0, 10, 10), vec(0, 10, 0)

    A.v, B.v, C.v, D.v, E.v, F.v = vec(0,0,0), vec(0,0,0), vec(0,0,0), vec(0,0,0), vec(0,0,0), vec(0,0,0)

    apex = [A, B, C, D, E, F]


    m_a_x, m_a_y, M_a_x = acc(theta_tmp, friction_tmp, M_tmp, m_tmp)


    for i in range(0,6):

        apex[i].v.x, apex[i].a.x = 0, M_a_x

    

    ball.v, ball.pos, ball.a.x, ball.a.y = vec(0,0,0), vec(1.5/sin(radians(theta_tmp)), 10, 5), m_a_x, m_a_y



def set_theta():

    theta_tmp, friction_tmp, M_tmp, m_tmp = s1.number, s2.number, s0.number, s3.number
    if theta_tmp == None: theta_tmp = theta
    if friction_tmp == None: friction_tmp = k
    if M_tmp == None: M_tmp = M
    if m_tmp == None: m_tmp = m
    if theta_tmp > 80 or theta_tmp < 10: theta_tmp = theta
    m_a_x, m_a_y, M_a_x = acc(theta_tmp, friction_tmp, M_tmp, m_tmp)

    for i in range(1,3):

        apex[i].pos.x = 10/tan(radians(theta_tmp))

    for i in range(0,6):

        apex[i].a.x = M_a_x

    ball.pos.x = 1.5/sin(radians(theta_tmp))

    ball.a.x, ball.a.y = m_a_x, m_a_y

    

def set_friction():

    theta_tmp, friction_tmp, M_tmp, m_tmp = s1.number, s2.number, s0.number, s3.number
    if theta_tmp == None: theta_tmp = theta
    if friction_tmp == None: friction_tmp = k
    if M_tmp == None: M_tmp = M
    if m_tmp == None: m_tmp = m

    m_a_x, m_a_y, M_a_x = acc(theta_tmp, friction_tmp, M_tmp, m_tmp)

    for i in range(0,6):

        apex[i].a.x = M_a_x

    ball.a.x, ball.a.y = m_a_x, m_a_y



def set_mass():

    theta_tmp, friction_tmp, M_tmp, m_tmp = s1.number, s2.number, s0.number, s3.number
    if theta_tmp == None: theta_tmp = theta
    if friction_tmp == None: friction_tmp = k
    if M_tmp == None: M_tmp = M
    if m_tmp == None: m_tmp = m

    m_a_x, m_a_y, M_a_x = acc(theta_tmp, friction_tmp, M_tmp, m_tmp)

    for i in range(0,6):

        apex[i].a.x = M_a_x

    ball.a.x, ball.a.y = m_a_x, m_a_y





# 開使按鈕、角度設定、摩擦力設定


scene.append_to_caption('      ')

b1 = button(text="Run", bind=Run, background=color.cyan)



scene.append_to_caption('      ')

b2 = button(text="Restart", bind=restart, background=color.cyan)

# 設定M

scene.append_to_caption('\n\nM =     ')

s0 = winput(bind=set_mass, type='numeric')

# 設定m

scene.append_to_caption('\n\nm =     ')

s3 = winput(bind=set_mass, type='numeric')

# 設定角度

scene.append_to_caption('\n\nAngle of wedge(10~80):')

s1 = winput(bind=set_theta, type='numeric')

scene.append_to_caption(' Degree\n')

# 設定摩擦力

scene.append_to_caption('\n\nCoefficient of friction on the slope: ')      

s2 = winput(bind=set_friction, type='numeric')

scene.append_to_caption('<i>\n\n(Please press enter after setting each parameter, otherwise \n it will run on default parameter)</i>')

scene.append_to_caption('\n\n\n\n\n')




# k = s2.value





# 大木塊



def set_wedge():

    A = vertex(pos=vec(0, 0, 0), color=color.orange, v=vec(0, 0, 0), a=vec(M_a_x, 0, 0))

    B = vertex(pos=vec(10/tan(radians(theta)), 0, 0), color=color.purple, v=vec(0, 0, 0), a=vec(M_a_x, 0, 0))

    C = vertex(pos=vec(10/tan(radians(theta)), 0, 10), color=color.green, v=vec(0, 0, 0), a=vec(M_a_x, 0, 0))

    D = vertex(pos=vec(0, 0, 10), color=color.blue, v=vec(0, 0, 0), a=vec(M_a_x, 0, 0))

    E = vertex(pos=vec(0, 10, 10), color=color.cyan, v=vec(0, 0, 0), a=vec(M_a_x, 0, 0))

    F = vertex(pos=vec(0, 10, 0), color=color.red, v=vec(0, 0, 0), a=vec(M_a_x, 0, 0))

    apex = [A, B, C, D, E, F]



    T1 = triangle(v0=E, v1=D, v2=C)

    T2 = triangle(v0=F, v1=A, v2=B)

    Q1 = quad(v0=F, v1=E, v2=D, v3=A)

    Q2 = quad(v0=F, v1=E, v2=C, v3=B)

    Q3 = quad(v0=A, v1=B, v2=C, v3=D)

    return A, B, C, D, E, F

A, B, C, D, E, F = set_wedge()

apex = [A, B, C, D, E, F]





#地板



floor = box(pos=vec(0,0,0), size=vec(300, 1, 30), color=color.blue, v=vec(0, 0, 0), 

            a=vec(0, 0, 0))



# 小球



ball = sphere(pos=vec(1.5/sin(radians(theta)), 10, 5), radius=1.5, v=vec(0, 0, 0),

            a=vec(m_a_x, m_a_y, 0), texture=textures.wood)





# 作圖



g1 = graph(title='<b>Velocity (x direction)</b>', 

           xtitle='<b>time</b>', ytitle='<b>P</b>', 

           align='left', width=500, height=300)

g2 = graph(title='<b>Energy<b>', xtitle='<b>time</b>', 

           ytitle='<b>E</b>', align='left', width=500, height=300)



# 動量


m_v = gdots(graph=g1, color=color.red)

M_v = gdots(graph=g1, color=color.green)



# 能量



m_E = gdots(graph=g2, color=color.blue)

M_E = gdots(graph=g2, color=color.red)

total_E = gdots(graph=g2, color=color.green)



#運動動畫



dt = 0.01

t = 0



while True:

    rate(1/dt)
    
    if ball.pos.x > 50:
        
        running = False

    if running:



        # 小木塊移動



        ball.v.x += ball.a.x * dt

        ball.pos.x += ball.v.x * dt

        ball.v.y += ball.a.y * dt

        ball.pos.y += ball.v.y * dt



        # 大木塊移動



        for i in range(0,6):

            apex[i].v.x += apex[i].a.x * dt

            apex[i].pos.x += apex[i].v.x * dt



        # 當木塊到底



        if ball.pos.y <= ball.radius+floor.size.y/2:



            #小球運動

            ball.v.x = (ball.v.x**2 + ball.v.y**2)**0.5

            ball.a.x, ball.a.y, ball.v.y = 0, 0, 0

            ball.up = vec(0, 1, 0)

            ball.pos.x += ball.v.x * dt



            #木塊運動

            for i in range(0,6):

                apex[i].a.x = 0

                apex[i].pos.x += apex[i].v.x * dt



        # 作圖(動量和能量)，到達底部後不畫動量

        if s0.number == None: tmp_M = M
        else: tmp_M = s0.number
        if s3.number == None: tmp_m = m
        else: tmp_m = s3.number

        if ball.pos.y >= ball.radius+floor.size.y/2:

            p = ball.v.x * tmp_m + A.v.x * tmp_M

            m_v.plot(pos=(t, ball.v.x))

            M_v.plot(pos=(t, A.v.x))

            # m_p.plot(pos=(t, m * ball.v.x))

            # M_p.plot(pos=(t, s0.value * A.v.x))



        K = 0.5*tmp_m*(ball.v.x**2 + ball.v.y**2) + 0.5*tmp_M*A.v.x**2

        U = tmp_m*g*(ball.pos.y - (ball.radius+floor.size.y/2))



        m_E.plot(pos=(t, K))

        M_E.plot(pos=(t, U))



        total_E.plot(pos=(t, K+U))



        t += dt