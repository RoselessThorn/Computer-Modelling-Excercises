# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 19:55:03 2021

@author: Ruiqi Chu
"""

"""
CMod Ex3: symplectic Euler time integration of
a particle moving in a Morse potential.

Produces plots of the position of the particle
and its energy, both as function of time. Also
saves both to file.

The potential is Morse potential, where
all parameters required are hard-coded in the main() method
and passed to the functions that
calculate force and potential energy.

Author:Ruiqi Chu
"""

import sys
import math
import numpy as np
import matplotlib.pyplot as pyplot
from scipy.signal import find_peaks
from particle3D import Particle3D as p3d

def force_morse(particle1, particle2, D_e, r_e, alpha):
    """
    Method to return the force on two particles at r1 and r2
    in a Morse potential.
    Force is given by
    F(r1,r2) = 2*α*D_e*{1-exp[-α(r_12-r_e)]}*exp[-α(r_12-r_e)]r_hat_12
    where α, D_e and r_e are constants
    D_e has a unit of eV and r_e has a unit of angstrom
    r_12 = r2 - r1 as the direction vector array
    rh_12 is the unit vector array
    rm_12 is the length of r_12
    
    :param particle1,2: Particle3D instance
    :param r1: particle position r1
    :param r2: particle position r2
    :return: force acting on particle as a 3D Numpy array in all directions
    """
    r1 = particle1.pos
    r2 = particle2.pos
    r_12 = r2 - r1
    rm_12 = math.sqrt(r_12[0]**2 + r_12[1]**2 + r_12[2]**2)
    rh_12 = r_12/rm_12
    force = (2*alpha*D_e*(1-math.exp(-alpha*(rm_12-r_e)))*math.exp(-alpha*(rm_12-r_e)))*rh_12
    return force


def pot_energy_morse(particle1, particle2, D_e, r_e, alpha):
    """
    Method to return potential energy in eV
    of particle in Morse potential
    U(r1,r2) = D_e*{[1-exp[-α(r_12-r_e)]]^2-1}

    α, D_e and r_e are constants
    D_e has a unit of eV and r_e has a unit of angstrom
    r_12 = r2 - r1
    rm_12 is the length of r_12
    :param particle1,2: Particle3D instance
    :param r1: particle position r1
    :param r2: particle position r2
    :return: potential energy of particle as float
    """
    r1 = particle1.pos
    r2 = particle2.pos
    r_12 = r2 - r1
    rm_12 = math.sqrt(r_12[0]**2 + r_12[1]**2 + r_12[2]**2)
    energy = D_e*((1-math.exp(-alpha*(rm_12-r_e)))**2-1)
    return energy


# Begin main code
def main():
    # Read name of output file from command line
    if len(sys.argv)!=2:
        print("Wrong number of arguments.")
        print("Usage: " + sys.argv[0] + " <output file>")
        quit()
    else:
        outfile_name = sys.argv[1]
    # Open output file
    outfile = open(outfile_name, "w")

    # Read the initial parameters from the file, be aware that all parameters but numstep should
    # be floats, numstep is an integer for later loop, set an empty list to store readings    
    output = []
    
    # Start reading from the file, read the first 4 lines with parameters, then put the later
    # two lines into the new particle function to get two particles.
    # Unit for time here is [T] = 1.018050571e-14s
    with open('nitrogen.dat') as f:
        f.readline()
        file_input = [next(f) for x in range(3)]
        for row in file_input:
           output.append(row.split())
        dt = float(output[0][0])
        numstep = int(output[0][1])
        time = 0.0
        D_e = float(output[2][0])
        r_e = float(output[2][1])
        alpha = float(output[2][2])
        p1 = p3d.new_particle(f)
        p2 = p3d.new_particle(f)
        # From dt = 0.01 record initial wavenumber for the frequency inaccuracy
        initial_wavenumber = 2258.0907473531406
    # Write out initial conditions and save the absolute value of atomic seperation
    energy = p1.kinetic_e() + p2.kinetic_e() + pot_energy_morse(p1, p2, D_e, r_e, alpha)
    outfile.write("{0:f} {1:f} {2:12.8f}\n".format(time,p1.pos[0],energy))
    r_12 = abs(p2.pos - p1.pos)

    # Initialise data lists for plotting later
    time_list = [time]
    pos_list = [r_12[0]]
    energy_list = [energy]

    #Record initial, highest and lowest energy
    E_0 = energy
    energy_max = energy
    energy_min = energy
    
    
    # Start the time integration loop
    for i in range(numstep):  
        # Update the postions of particles first so that force and accelration are updated ones
        # and record the absolute value of interatomic seperation
        p1.update_pos(dt)
        p2.update_pos(dt)
        r_12 = abs(p2.pos - p1.pos)
        
        # Calculate force
        force = force_morse(p1, p2, D_e, r_e, alpha)


        # Update particle velocity 
        p1.update_vel(dt,force)
        p2.update_vel(dt,-force)
        
        
        # Increase time
        time += dt

        # Find the total energy which is the sum of two particles' kinetic energy and morse energy
        energy = p1.kinetic_e() + p2.kinetic_e() + pot_energy_morse(p1, p2, D_e, r_e, alpha)
        
        #Compare to the max and min energy stored
        if energy > energy_max:
            energy_max = energy
        if energy < energy_min:
            energy_min = energy
            
        # Output particle information
        outfile.write("{0:f} {1:f} {2:12.8f}\n".format(time,p1.pos[0],energy))
        
        # Append information to data lists
        time_list.append(time)
        pos_list.append(r_12[0])
        energy_list.append(energy)

    # Post-simulation:
    # Close output file
    outfile.close()
    
    
    # Find maximum peaks for position
    peaks = find_peaks(pos_list, height = 1)
    
    #list of the heights of the peaks
    height = peaks[1]['peak_heights'] 
    
    # Transfer both position and time lists to numpy arrays for further methods
    pos_list = np.array(pos_list)
    time_list = np.array(time_list)
    
    #list of the peaks positions
    peak_pos = time_list[peaks[0]] 
    
    # Period is the average value of the differences between positions of peaks in unit [T]
    period = (np.average(np.diff(peak_pos)))
    
    # Then transfer the period to seconds as defined before
    period = period * 1.018050571e-14

    # Calculate frequency and then wavenumber = frequency/light speed, unit in cm^-1
    frequency = 1/period
    wavenumber = frequency/(3e8*100)
    # Print out wave number and frequency inaccuracy
    print('Wavenumber = ' + str(wavenumber) + 'cm^-1')
    print('Frequency Inaccuracy = ' + str((wavenumber-initial_wavenumber)/initial_wavenumber))
    
    
    # Print out energy inaccuracy ΔE/E_0 where E_0 is the initial energy
    print('ΔE/E_0 = '  +str((energy_max-energy_min)/E_0))
    
    # Plot particle trajectory to screen
    pyplot.title('Symplectic Euler: x-position for interatomic seperation vs time')
    pyplot.xlabel('Time/[T]')
    pyplot.ylabel('x-position of interatomic seperationvs/Angstrom')
    pyplot.plot(time_list, pos_list)
    pyplot.show()

    # Plot particle energy to screen
    pyplot.title('Symplectic Euler: total energy vs time')
    pyplot.xlabel('Time/[T]')
    pyplot.ylabel('Energy/eV')
    pyplot.plot(time_list, energy_list)
    pyplot.show()

    # Plot peaks to find frequency
    fig = pyplot.figure()
    ax = fig.subplots()
    ax.plot(time_list, pos_list)
    pyplot.xlabel('Time/[T]')
    pyplot.ylabel('x-position of interatomic seperationvs/Angstrom')
    ax.scatter(peak_pos, height, color = 'r', s = 15, marker = 'X', label = 'Maxima')
    ax.legend()
    ax.grid()
    pyplot.show()
# Execute main method, but only when directly invoked
if __name__ == "__main__":
    main()

