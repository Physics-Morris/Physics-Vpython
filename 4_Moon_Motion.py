# Morris H. 12/10

from vpython import *

# intial setting

sun_mass, sun_r= 1988500E24, 695700*10**3
earth_mass, earth_r, earth_v = 5.9724*10**24, 6371*10**3, 29780
moon_mass, moon_r, moon_v = 0.07346*10**24, 1737*10**3, 1.023*10**3
sun_earth_r, earth_moon_r = 152.10*10**9 , 384400*10**3
G = 6.67408E-11
T = 2551392


scene = canvas(title='<font size=30><center><i>Motion of Moon\n</i></center></font>', 
                   width=1600, height=1300, align='left', range=200)
scene.range = sun_earth_r + earth_moon_r*70

earth = sphere(pos=vec(sun_earth_r, 0, 0), texture=textures.earth, up=vec(-tan(23.5/180*pi), 0, 1), 
               radius=earth_r*1000, make_trail=False, v=vec(0, earth_v, 0), a=vec(0, 0, 0))

sun = sphere(pos=vec(0,0,0), radius=sun_r, color=color.orange, emissive=True, v=vec(0, 0, 0), 
             a=vec(0, 0, 0))

# moon = sphere(pos=vec(earth_moon_r+sun_earth_r, 0, 0), radius=moon_r*20, make_trail=False, 
#               v=vec(0, moon_v+earth_v, 0), a=vec(0, 0, 0))

moon = sphere(pos=vec(sun_earth_r+earth_moon_r, 0, 0), radius=moon_r*2000, make_trail=False)


g1 = graph(title='Moon Position', align='right', xtitle='<b>X</b>', ytitle='<b>Y</b>')

xy = gdots(graph=g1, color=color.black)



t, dt = 0, 60*60
while True:
    rate(150)
    earth.rotate(angle=1, axis=vec(-tan(23.5/180*pi), 0, 1))

    earth.a = G*sun_mass*(sun.pos-earth.pos)/mag(sun.pos-earth.pos)**3 
    earth.v += earth.a*dt
    earth.pos += earth.v*dt
    
    # moon.a = G*earth_mass*(earth.pos-moon.pos)/mag(earth.pos-moon.pos)**3 + G*sun_mass*(sun.pos-moon.pos)/mag(sun.pos-moon.pos)**3
    # moon.v += moon.a*dt + earth.a*dt
    # moon.pos += moon.v*dt + earth.v*dt

    # scene.camera.follow(earth)
    
    xy.plot(pos=(moon.pos.x, moon.pos.y))

    moon.make_trail, earth.make_trail = True, True
    
    moon.rotate(origin=earth.pos, angle=2*pi/T*dt, axis=vec(0, 0, 1))
    t += dt

    
