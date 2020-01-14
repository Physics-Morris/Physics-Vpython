# import package
from vpython import *

# parameter setting
k = 9E9             # Coulomb constant
ec = 1.6E-19        # electron charge 
scale = 4E-14/1E17       # scale up the magnetude of electric field

# create scene and object
scene = canvas(width=1000, height=600, align='left', range=2E-13)

# create charge
charges = []
def Create_Charge(pos):
    charge = sphere(pos=pos, radius=1.2e-14)
    charges.append(charge)

# calculate electric field at a given position
def Calculate_Field(pos):
    # superposition property
    for charge in charges:
        field = (pos-charge.pos)/mag(pos-charge.pos)**3
    return field

# create electric field arrow at a given position
field = []
def Create_Field(pos):
    field.append(arrow(pos=pos, axis=Calculate_Field(pos)*scale, color=color.red, shaftwidth=6e-15))

Create_Charge(vec(1E-13, 0, 0))
Create_Field(vec(-1E-13, 0, 0))     