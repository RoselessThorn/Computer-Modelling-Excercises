# -*- coding: utf-8 -*-
"""

Created on Tue Sep 28 14:57:01 2021
CMod Ex. 1: vector.py, a module that provides a set of functions to
manipulate vectors, expressed as lists.
@author: Ruiqi Chu

"""

import math

def norm_sq(v):
    """
    Square modulus
    
    :param v: vector (v1, v2, v3)
    :return: square modulus v1**2+v2**2+v3**2
    """
    return v[0]**2 + v[1]**2+v[2]**2


def norm(v):
    """
    Modulus
    
    :param v: vector (v1, v2, v3)
    :return: modulus (v1**2+v2**2+v3**2)**(1/2)
    """
    return math.sqrt(norm_sq(v))


def scale_mul(v, scalar):
    """
    Multiplication of vector with scalar
    
    :param v: vector (v1, v2, v3)
    :param scalar: scalar factor
    :return: scaled vector (v1*scalar, v2*scalar, v3*scalar)
    """
    return [v[0]*scalar, v[1]*scalar, v[2]*scalar]


def scale_div(v, scalar):
    """
    Division of vector with scalar
    
    :param v: vector (v1, v2, v3)
    :param scalar: scalar factor
    :return: scaled vector (v1/scalar, v2/scalar, v3/scalar)
    """
    return [v[0]/scalar, v[1]/scalar, v[2]/scalar]


def add(v1, v2):
    """
    Vector addition
    
    :param v1: first vector
    :param v2: second vector
    :return: vector sum v1+v2
    """
    return [v1[0]+v2[0], v1[1]+v2[1],v1[2]+v2[2]]


def sub(v1, v2):
    """
    Vector sublimation
    
    :param v1: first vector
    :param v2: second vector
    :return: vector sublimation v1-v2
    """
    return [v1[0]-v2[0], v1[1]-v2[1],v1[2]-v2[2]]


def cross_product(v1, v2):
    """
    Vector cross product
    
    :param v1: first vector
    :param v2: second vector
    :return: vector cross product too long to write lol
    """

    return [round(v1[1]*v2[2]-v1[2]*v2[1],10), round(v2[0]*v1[2]-v2[2]*v1[0],10), round(v1[0]*v2[1]-v1[1]*v2[0],10)]


def dot_product(v1, v2):
    """
    Vector dot product
    
    :param v1: first vector
    :param v2: second vector
    :return: vector dot product 
    """

    return [v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]]

def same_check(v1, v2):
    """
    Check whether two vectors are the same, since binary will make small difference between two same 
    numbers, we use a thresh here to determine
    
    :param v1: first vector
    :param v2: second vector
    :return: true or false
    """
    thresh = 1.0e-7
    if (abs(v1[0] - v2[0]) < thresh):
        if (abs(v1[1] - v2[1]) < thresh):
                if (abs(v1[1] - v2[1]) < thresh):
                    return ('True')
                else:
                    return ('False')
        