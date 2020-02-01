# 2020/1/12 Morris

# import package
from vpython import *

# parameter setting
k = 9E9                 # Coulomb constant
ec = 1.6E-19            # electron charge
radius = 1.2E-14        # radius of charge
field = []              # store electric field arrow
arrow_length = 3E-14    # length of arrow
dt = 0.01               # update time interval
m = 1.6E-27             # mass of charge

def main():
    '''main function'''
    # create scene
    scene = canvas(width=1000, height=600, align='left', range=3E-13)

    # create two plates and create a capacitor 
    up_plate = box(pos=vec(0, 1E-13, 0), size=vec(4E-13, 4E-16, 4E-13),
                   color=color.blue)
    down_plate = box(pos=vec(0, -1E-13, 0), size=vec(4E-13, 4E-16, 4E-13),
                     color=color.red)

    # fill the plates with charge
    for x in range(-20, 22, 2):
        for y in [up_plate.pos.y, down_plate.pos.y]:
            for z in range(-20, 22, 2):
                # positive charge and negative charge locate at top plate and down plate
                if y > 0: mu = 1
                else: mu = -1
                Create_Charge(vec(x*1E-14, y, z*1E-14), mu)

    # create field between plates
    for x in range(-9, 9, 4):
        for y in range(-9, 9, 4):
            for z in range(-9, 9, 4):
                Create_Field(vec(x*2E-14, y*1E-14, z*2E-14))

    # create a moving charge
    moving_charge = sphere(pos=vec(-4E-13, 5E-14, 0), radius=radius,
                           coulomb=5E-42*ec, color=color.green,
                           v=vec(1.5E-13, 0, 0), make_trail=True)

    # simulation
    while True:
        rate(1/dt)
        # update the velcocity and position of moving charge
        Update(moving_charge)

charges = []
def Create_Charge(pos, C):
    '''input coulomb and position of the charge and create it'''
    charge = sphere(pos=pos, radius=radius, coulomb=C*ec)
    # red and blue represent negative and positive charge respectively
    if C > 0: charge.color = color.blue
    else: charge.color = color.red
    # store all charge inside charges[]
    charges.append(charge)

def Create_Field(pos):
    '''for a given position calculate electric field'''
    # intialize the electric field
    E = vec(0, 0, 0)
    # use superposition quality of electric field to calcuate the field
    for charge in charges:
        E += k*charge.coulomb*(pos-charge.pos)/mag(pos-charge.pos)**3
    # use color to show the magnitude of electric field
    color = Mapping(mag(E))
    field.append(arrow(pos=pos, axis=hat(E)*arrow_length,
                       color=vec(1, color, 0)))

# mapping from (Inf, 0) to (1, 0), and convert into rgb color
def Mapping(E):
    '''mapping from (Inf, 0) to (1, 0) as the rgb color value'''
    a = 1E-17
    return 1-exp(-a*E)

# calculate charge motion
def Update(obj):
    '''given a charge and position and update position'''
    # first calculate electric field at a given position
    E = vec(0, 0, 0)
    # superposition quality
    for charge in charges:
        E += k*charge.coulomb*(obj.pos-charge.pos)/mag(obj.pos-charge.pos)**3
    # use formula: s = v0*t + 1/2*a*t^2
    obj.v += obj.coulomb*E/m*dt
    obj.pos += obj.v*dt

main()
