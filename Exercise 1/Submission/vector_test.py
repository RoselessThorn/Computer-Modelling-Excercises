56# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 15:24:42 2021
CMod Ex1: tester of the vector.py module.
Creates three random vectors and
runs through all functions implemented in vector.py
@author: Ruiqi Chu
"""
import math
import random
import vector as vector

# Main method:
def main():
    # Create three random vectors
    v1 = [random.random(), random.random(), random.random()]
    v2 = [random.random(), random.random(), random.random()]
    v3 = [random.random(), random.random(), random.random()]
    # Print out three vectors
    print("v1 = ", v1)
    print("v2 = ", v2)
    print("v3 = ", v3)
    
    # addition, multiplication, division

    print("v1+v2 = ", vector.add(v1,v2))
    print("v1*v2 = ", vector.dot_product(v1,v2))
    print("v1×v2 = ", vector.cross_product(v1, v2))

    #Independently calculate vector identity 1
    cross_1 = vector.cross_product(v1, v2)
    cross_2 = vector.cross_product(v2, v1)
    for i in range (3):
        cross_2[i] = -cross_2[i]
    #Test whether they are the 'same'
    print('Are these two vectors the same for identity 1?')
    print(vector.same_check(cross_1,cross_2))
    #Vector identity 2
    two_1 = vector.cross_product(v1, (vector.add(v2, v3)))
    two_2 = vector.add((vector.cross_product(v1, v2)), (vector.cross_product(v1, v3)))
    #Test whether they are the same
    print('Are these two vectors the same for identity 2?')
    print(vector.same_check(two_1,two_2))
    #Vector identity 3
    three_1 = vector.cross_product(v1, vector.cross_product(v2, v3))
    three_2_1 = [element * vector.dot_product(v1,v3)[0] for element in v2]
    three_2_2 = [element * vector.dot_product(v1,v2)[0] for element in v3]
    three_2 = vector.sub(three_2_1, three_2_2)
    #Test whether they are the same
    print('Are these two vectors the same for identity 3?')
    print(vector.same_check(three_1,three_2))
# Execute main method, but only if it is invoked directly
if __name__ == "__main__":
    main()