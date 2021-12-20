# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 19:04:35 2021
CMod Ex1: tester of the numpy.py module.
Creates three random vectors and
runs through all functions by numpy
@author: Ruiqi Chu
"""

import numpy as np
import random

# Main method:
def main():
    #This is to avoid bit-inequivalent between two same numbers
    thresh = 1.0e-7
    # Create three random vectors
    v1 = np.array([random.random(), random.random(), random.random()])
    v2 = np.array([random.random(), random.random(), random.random()])
    v3 = np.array([random.random(), random.random(), random.random()])
    #v1 = [1,9,3]
    #v2 = [4,2,3]
    #v3 = [1,8,3]
    # Print out both vectors
    print("v1 = ", v1)
    print("v2 = ", v2)
    print("v3 = ", v3)
    
    # addition, subtraction, multiplication, division

    print("v1+v2 = ", np.add(v1,v2))
    print("v1*v2 = ", np.inner(v1,v2))
    print("v1×v2 = ", np.cross(v1, v2))

    #Independently calculate vector identity 1
    cross_1 = np.cross(v1, v2)
    cross_2 = np.cross(v2, v1)
    cross_3 = cross_2*(-1)
    #Test whether they are the 'same'
    print('Are these two vectors the same for identity 1?')
    if (abs(cross_1[0] - cross_3[0]) < thresh):
        if (abs(cross_1[1] - cross_3[1]) < thresh):
                if (abs(cross_1[1] - cross_3[1]) < thresh):
                    print ('True')
                else:
                    print ('False')
    #Vector identity 2
    two_1 = np.cross(v1, (np.add(v2, v3)))
    two_2 = np.add((np.cross(v1, v2)), (np.cross(v1, v3)))
    #Test whether they are the same
    #print (vector.add(v2, v3),two_1)
    print('Are these two vectors the same for identity 2?')
    if abs(two_1[0] - two_2[0]) < thresh:
        if abs(two_1[1] - two_2[1]) < thresh:
                if abs(two_1[1] - two_2[1]) < thresh:
                    print ('True')
                else:
                    print ('False')
    #Vector identity 3
    three_1 = np.cross(v1, np.cross(v2, v3))
    three_2 = np.subtract([element * np.inner(v1,v3) for element in v2], [element * np.inner(v1,v2)for element in v3])
    #Test whether they are the same
    print('Are these two vectors the same for identity 3?')
    if abs(three_1[0] - three_2[0]) < thresh:
        if abs(three_1[1] - three_2[1]) < thresh:
                if abs(three_1[1] - three_2[1]) < thresh:
                    print ('True')
                else:
                    print ('False')
# Execute main method, but only if it is invoked directly
if __name__ == "__main__":
    main()