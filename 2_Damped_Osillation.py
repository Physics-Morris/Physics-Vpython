# Morris 2019/11/21

from vpython import *
# from random import *

############################################################################################

k, m = 1, 5
# critical, under, over = 2*m*(k/m)**0.5, 0.2, 10
gamma = 2*(m*k)**0.5


############################################################################################

scene = canvas(width=1000, height=600, background=vec(0, 0.6, 0.6), align='left')
scene.camera.pos = vec(-35, 80, 90)
scene.camera.axis = vec(25, -60, -90)

############################################################################################

# box()
# scene.caption = "\\(m\\dfrac {d^{2}x}{dt^{2}}+\\gamma \\dfrac {dx}{dt}+kx = 0\\)"

# MathJax.Hub.Queue(["Typeset",MathJax.Hub])

############################################################################################
 
A = vertex(pos=vec(50, 45, 17), color=color.green, opacity=0.2)
B = vertex(pos=vec(50, 45, -17), color=color.green, opacity=0.2)
D = vertex(pos=vec(-50, 45, 17), color=color.green, opacity=0.2)
C = vertex(pos=vec(-50, 45, -17), color=color.green, opacity=0.2)

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
block = []

spring = helix(pos=vec(0, 33, 0), axis=vec(0, 37, 0), radius=3, coil=30,
                v=vec(0, 0, 0), a=vec(0, -35*k/m, 0))

a = box(pos=vec(0, 35, 0), size=vec(7, 7, 7), color=color.red, v=vec(0, 0, 0),
             a=vec(0, -35*k/m, 0))

block.append(a)

water = box(pos=vec(0, 2, 0), size=vec(100, 74, 34), color=vec(0, 0, 1), opacity=0.2)

celling = box(pos=vec(0, 70, 0), size=vec(100, 2, 34), color=vec(0.3, 0.3, 0.3))



############################################################################################

running = False

def Run(r):
    global running
    running = not running

    if running: 
        r.text = "Pause"

    else: 
        r.text = "Run"

i = 0
yt = []
def Restart():
    global running, t, i
    k0, m0, gamma0 = test_none(ipt_k.number, ipt_m.number, ipt_gamma.number)
    running = False
    b1.text = 'Run'
    t = 0
    i += 1
    x, y, z = random(), random(), random()
    yt_idx = gcurve(graph=g1, color=vec(x, y, z))
    yt.append(yt_idx)
    a = box(pos=vec(0, 35, 0), size=vec(7, 7, 7), color=vec(x, y, z), v=vec(0, 0, 0),
             a=vec(0, -35*k0/m0, 0))
    block.append(a)
    block[i-1].visible = False
    spring.pos = vec(0, 33, 0)
    spring.v = vec(0, 0, 0)
    spring.a = vec(0, -35*k0/m0, 0)
    spring.axis = vec(0, 37, 0)

def set_k():
    k0, m0, gamma0 = test_none(ipt_k.number, ipt_m.number, ipt_gamma.number)
    critical(k0, m0, gamma0)

def set_m():
    k0, m0, gamma0 = test_none(ipt_k.number, ipt_m.number, ipt_gamma.number)
    critical(k0, m0, gamma0)

def set_gamma():
    k0, m0, gamma0 = test_none(ipt_k.number, ipt_m.number, ipt_gamma.number)    
    critical(k0, m0, gamma0)

def test_none(k_tmp, m_tmp, gamma_tmp):
    if k_tmp == None: k_ans = k 
    else: k_ans = k_tmp
    if m_tmp == None: m_ans = m
    else: m_ans = m_tmp
    if gamma_tmp == None: gamma_ans = gamma
    else: gamma_ans = gamma_tmp
    return k_ans, m_ans, gamma_ans

def critical(k_tmp, m_tmp, gamma_tmp):
    k0, m0, gamma0 = test_none(ipt_k.number, ipt_m.number, ipt_gamma.number)
    txt1.text = 2*(k0*m0)**0.5
    return 0
############################################################################################

scene.append_to_caption('      ')

b1 = button(text="Run", bind=Run, background=color.cyan)

scene.append_to_caption('      ')

b2 = button(text="Restart", bind=Restart, background=color.cyan)

scene.append_to_caption('\n\n      k =     ')
ipt_k = winput(bind=set_k, type='numeric')

scene.append_to_caption('\n\n      m =     ')
ipt_m = winput(bind=set_m, type='numeric')

scene.append_to_caption('\n\n      &Gamma; =     ')
ipt_gamma = winput(bind=set_gamma, type='numeric')

scene.append_to_caption('\n\n      (for critical damping &Gamma; = ')
txt1 = wtext(text=2*(k*m)**0.5)
scene.append_to_caption(')')

scene.append_to_caption('<i>\n\n(Please press enter after setting each parameter to confirm the setting,\n otherwise it will run on default parameter)</i>')

############################################################################################
g1 = graph(title='Position', xtitle='t', ytitle='position', align='right', width=500,
           height=300)

yt_idx = gcurve(graph=g1, color=color.red)
yt.append(yt_idx)
############################################################################################

dt = 0.01
t = 0

while True:

    if running:
        k0, m0, gamma0 = test_none(ipt_k.number, ipt_m.number, ipt_gamma.number)

        rate(300)
        block[i].a.y = -k0*block[i].pos.y/m0 - block[i].v.y*gamma0/m0
        block[i].v.y += block[i].a.y*dt
        block[i].pos.y += block[i].v.y*dt


        spring.a.y = -k0*spring.pos.y/m0 - spring.v.y*gamma0/m0
        spring.v.y += spring.a.y*dt
        spring.pos.y += spring.v.y*dt


        spring.axis.y = spring.axis.y - spring.v.y*dt

        yt[i].plot(pos=(t, block[i].pos.y))

        t += dt
