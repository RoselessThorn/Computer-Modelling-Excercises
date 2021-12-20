# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 19:41:02 2021
A programe includes PBC and MIC methods to determine the image of x inside a cube with edge l
@author: Ruiqi Chu
"""

import numpy as np

def pbc():
    #Input the length of the cube edge and the position vector x in array
    l = float(input('Edge length of the cube:'))
    x = []
    #Set the empty array for the image of x
    x_image = np.array([])
    for i in range(3):
        x.append(float(input('Element ' + str(i+1) + ': ')))
    x = np.array(x)
    #print (x,l)
    #Use modulo method in numpy to find the image position, available for negative position
    x_image = np.mod(x,l)
    print ('Position of the image of x',x_image)
# Execute the method, delete the # sign to operate
pbc()

def mic():
    #Input the length of the cube edge and the position vector x in array
    l = float(input('Edge length of the cube:'))
    x = []
    #Set the empty array for the image of x
    x_image = np.array([])
    for i in range(3):
        x.append(float(input('Element ' + str(i+1) + ': ')))
    x = np.array(x)
    x_image = np.mod(x,l)
    #To test whether the position is cloest to the origin or not, if not move it to the next cell
    for i in range (3):
        if x_image[i] > 0.5 * l:
            x_image[i] = x_image[i]-l
    print ('Position of the image of x closest to origin',x_image)
# Execute the method, delete the # sign to operate
mic()