# 2020/1/12 Morris

# import package
from vpython import *

# parameter setting
k = 9E9                 # Coulomb constant
ec = 1.6E-19            # electron charge
radius = 1.2E-14        # radius of charge
field = []              # store electric field arrow
arrow_length = 3E-14    # length of arrow

def main():
    # create scene and object
    scene = canvas(width=1000, height=600, align='left', range=3E-13)

    Create_Charge(vec(10*radius, 0, 0), -1)
    Create_Charge(vec(-10*radius, 0, 0), 1)

    # generate electric field
    for x in range(-22, 22, 5):
        for y in range(-22, 22, 5):
            for z in range(-12, 12, 5):
                Create_Field(vec(x*radius, y*radius, z*radius))

# create charge
charges = []
def Create_Charge(pos, C):
    charge = sphere(pos=pos, radius=radius, coulomb=C*ec)
    charges.append(charge)

# create electric field
def Create_Field(pos):
    # calculate electric field (superposition property)
    E = vec(0, 0, 0)
    for charge in charges:
        E += k*charge.coulomb*(pos-charge.pos)/mag(pos-charge.pos)**3
    # create electric field using arrow
    color = Mapping(mag(E))
    field.append(arrow(pos=pos, axis=hat(E)*arrow_length, color=vec(1, color, 0)))

# coordinate transformation
def Transform_Coordinate(r, theta, phi):
    x = r*sin(theta)*cos(phi)
    y = r*sin(theta)*sin(phi)
    z = r*cos(theta)
    return vec(x, y, z)

# mapping from (Inf, 0) to (1, 0)
def Mapping(E):
    a = 1E-17
    return 1-exp(-a*E)

main()
