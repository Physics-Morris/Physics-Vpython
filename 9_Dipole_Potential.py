# 2020/2/10 Morris
# import package
from vpython import *

# parameter setting
k = 9E9                     # Coulomb constant
ec = 1.6E-19                # charge of a electron
radius = 1.2E-14            # radius of charge
arrow_length = 1E-14        # length of arrow
shaftwidth = 1E-15          # shaft width of arrow
dt = 0.01                   # update time interval
m = 1.6E-27                 # mass of charge


def main():
    '''main function'''

    # create scene and object
    scene = canvas(width=1000, height=600, range=2E-13, userspin=False, userpan=False, 
                   userzoom = False)

    # create a dipole at +-10*radius away from the origin and using class 'Charge'
    charges = Charge([[vec(-10*radius, 0, 0), -ec], 
                     [vec(10*radius, 0, 0), ec]])

    # show electric potential in the given region
    charges.show_potential(scene.range*1.8)

    # show field the dipole in the given region
    charges.show_field(scene.range*1.8)


class Charge:
    '''
    a class that handle the attribute and the method regarding of charges
    '''

    def __init__(self, infos):
        '''
        --> initialize the class charge by creating sphere that representing the charge.
        --> info[0] and info[1] representing the position of the charge and the coulommb 
            for the charge repectively.
        '''
        self.infos = infos 
              
        # create charge by using 'sphere' 
        # red and blue represent negative and positive charge respectively
        for info in self.infos:
            sphere(pos=info[0], radius=radius, coulomb=info[1]*ec, 
                   color = color.blue if info[1] > 0 else color.red)

               
    def show_field(self, range):
        '''
        create field in the given range and set the default interval that create a 
        arrow be the radius of the charge
        '''

        # create arrow representing eletric field in the given region
        for x, y in self.meshgrid(range, range):
            pos, E = vec(x, y, 0), vec(0, 0, 0)

            # using try and except syntax to prevent the error by divided 0
            try:
                # use superposition quality of electric field to calcuate the field
                for info in self.infos:
                    E += k*info[1]*(pos-info[0])/mag(pos-info[0])**3
                
                # normalize the value of eletric field to (0, 1)
                color = self.field_color(mag(E))

                # create field by creating arrow 
                arrow(pos=pos, axis=hat(E)*arrow_length, color=color, shaftwidth=shaftwidth)
            except ZeroDivisionError:
                # cannot calculate the eletric field at the surface of the charge
                print('Electric field is infinity at the susrface of the charge')
        

    def show_potential(self, range):
        '''
        for a given position calculate electric potential and draw a 
        '''
        
        # create quad object that representing eletric potnetial in the given region
        for x, y in self.meshgrid(range, range, 0.5*radius):
            pos, V = vec(x, y, 0), 0
            # using try and except syntax to prevent the error by divided 0
            try:
                # calculate the eletric potential using fromula v = k*q/r
                for info in self.infos:
                    V += k*info[1]/mag(pos-info[0])
                
                # given red color if potnetial is smaller than 0, and vice versa
                color = self.potential_color(V)

                # create field by creating quad of meshgrid and the color represnt potential
                self.create_quad(pos, color)
                
            except ZeroDivisionError:
                # cannot calculate the eletric field at the surface of the charge
                print('Electric field is infinity at the susrface of the charge')
    

    def field_norm(self, value):
        '''
        normalize the value of eletric field between vmin and vmax to 0 and 1 
        by taking log, so the normalize value can be used for mapping the colors
        '''
        a = 1E-17
        return 1 - log(a*value)


    def potential_norm(self, value):
        '''
            normalize the value of eletric potential between vmin and vmax to 0 and 1 
            by taking log, so the normalize value can be used for mapping the colors
        '''
        b = 3E-4
        # to prevent the area that potential equals to 0 that will arise domain error
        try:
            return log(b*abs(value))
        except ValueError:
            return 0


    def field_color(self, value):
        '''
            --> return a vector of color by a given magnitude of elecric field
            --> the value of eletric field needs to be normalized first
        '''
        return vec(1, self.field_norm(value), 0)


    def potential_color(self, value):
        '''
            --> return a vector of color(blue stands for positive potential, and vice versa)
            --> the value of eletric potential needs to be normalized first
        '''
        return vec(0, 0, self.potential_norm(value)) if value > 0 else vec(self.potential_norm(value), 0, 0)

    def create_quad(self, pos, color):
        '''
        --> create a meshgrid at the given position and the color at that position
        --> using quad object and the side length be the 0.1 times raidus of the charge
        '''
        quad(vs=[vertex(pos=(pos-vec(0.25*radius, 0.25*radius, 0)), color=color, opacity=0.6),
                vertex(pos=(pos-vec(0.25*radius, -0.25*radius, 0)), color=color, opacity=0.6),
                vertex(pos=(pos-vec(-0.25*radius, -0.25*radius, 0)), color=color, opacity=0.6),
                vertex(pos=(pos-vec(-0.25*radius, 0.25*radius, 0)), color=color, opacity=0.6)])


    def meshgrid(self, xrange, yrange, step=radius):
        '''
        create a meshgrid a given xrange and yrange
        setting default step be the radius of the charge
        '''
        grid = []
        for x in self.frange(-xrange, xrange, step):
            for y in self.frange(-yrange, yrange, step):
                grid.append([x, y])
        return grid

    def frange(self, start, stop, step=1):
        '''
        create a range that each stap can be a float number that can be in this program
        '''
        n = int(round((stop - start)/float(step)))
        if n > 1:
            return([start + step*i for i in range(n+1)])
        elif n == 1:
            return([start])
        else:
            return([])


# execute main functin after run all the function
main()
