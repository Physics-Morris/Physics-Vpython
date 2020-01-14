# Morris H. 12/10

from vpython import *

# intial setting

sun_mass, sun_r= 1988500E24, 695700*10**3
earth_mass, earth_r, earth_v = 5.9724*10**24, 6371*10**3, 29780
moon_mass, moon_r, moon_v = 0.07346*10**24, 1737*10**3, 1.023*10**3
sun_earth_r, earth_moon_r = 152.10*10**9 , 384400*10**3
G = 6.67408E-11
T = 2360488


scene = canvas(title='<font size=30><center><i>Motion of Moon\n</i></center></font>', 
                   width=1000, height=600, align='left', range=200)


scene.range = sun_earth_r + earth_moon_r*50

earth = sphere(pos=vec(sun_earth_r, 0, 0), texture=textures.earth, up=vec(-tan(23.5/180*pi), 0, 1), 
               radius=earth_r, make_trail=True, v=vec(0, earth_v, 0), a=vec(0, 0, 0))

sun = sphere(pos=vec(0,0,0), radius=sun_r*50, color=color.orange, emissive=True, v=vec(0, 0, 0), 
             a=vec(0, 0, 0))

# moon = sphere(pos=vec(earth_moon_r+sun_earth_r, 0, 0), radius=moon_r*20, make_trail=False, 
#               v=vec(0, moon_v+earth_v, 0), a=vec(0, 0, 0))

moon = sphere(pos=vec(sun_earth_r+earth_moon_r*10, 0, 0), radius=moon_r*2500, make_trail=True, 
              color=vec(0.95, 0.94, 0.78))


g1 = graph(title='Moon Position', align='right', xtitle='<b>X(km)</b>', ytitle='<b>Y(km)</b>', 
           width=500, height=350)

scene.append_to_caption('\n\n<i>Make sun 50 times bigger and moon 2500 times bigger</i>\n\n\n\n\n\n\n')

moon_p = gdots(graph=g1, color=color.black)
earth_p = gdots(graph=g1, color=color.blue)





t, dt, i = 0, 60*60, 0
while True:
    rate(150)
    earth.rotate(angle=1, axis=vec(-tan(23.5/180*pi), 0, 1))

    earth.a = G*sun_mass*(sun.pos-earth.pos)/mag(sun.pos-earth.pos)**3 
    earth.v += earth.a*dt
    earth.pos += earth.v*dt

    moon.pos = vec(earth_moon_r*cos(dt*i*2*pi/T)*10, earth_moon_r*sin(dt*i*2*pi/T)*10, 0) + earth.pos
    i += 1

    moon_p.plot(pos=(moon.pos.x/1000, moon.pos.y/1000))
    earth_p.plot(pos=(earth.pos.x/1000, earth.pos.y/1000))

    t += dt

    
