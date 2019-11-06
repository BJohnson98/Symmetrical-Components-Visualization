'''
This program will visualize the theorm of symmetrical components. You should be able to
input a non balanced 3 phase system and this program will show the sequence components that
the system is made out of.
Author: Brandon Johnson
Date: 10/27/2019
'''
import numpy as np
import matplotlib.pyplot as plt
import math
import cmath
from string import ascii_uppercase

class phasor:
	def __init__(self, radius=0, angle=0):
		self.radius = radius
		self.angle = angle
	def cart(self):
		x = self.radius*np.cos(self.angle*math.pi/180)
		y = self.radius*np.sin(self.angle*math.pi/180)
		z = round(x,3) + round(y,3)*cmath.sqrt(-1)
		return(z)
	def get_real(self):
		return(round(self.radius*np.cos(self.angle*math.pi/180),3))
		
	def get_imaginary(self): 
		return(round(self.radius*np.sin(self.angle*math.pi/180),3))
	#allows you to input a new phasor in cartesian form.
	def input_cart(self, real, imag):
		self.radius = round(np.sqrt(real**2 + imag**2),3)
		self.angle = round(np.arctan2(imag, real)*180/math.pi,3)
	
	def rotate(self, alpha):
		self.angle = self.angle + alpha

def main():
	color = ['red','y','blue','orange','green','magenta','cyan','brown','purple']
	alphabet = ascii_uppercase
	
	#define and undetermined amount of phases.
	phasor_list = []
	max_R = []
	#ask user to input the number of phases they want.
	num_phases = int(input("How many phases do you want to enter?:\n"))
	#now ask the user to enter the values for the phases.
	for i in range(num_phases):
		radius = float(input(f"Enter Phase {alphabet[i%26]}'s radius: "))
		angle = float(input(f"Enter Phase {alphabet[i%26]}'s angle: "))	
		phasor_list.append(phasor(radius, angle))
		max_R.append(radius)

	alpha = 360/num_phases
	a = phasor(1,alpha)
		


	#prints the original list of phasors
	for i in range(num_phases):	
		print(phasor_list[i].radius, phasor_list[i].angle)
		plot_vector(0, 0, phasor_list[i].radius, phasor_list[i].angle, color[i%len(color)])
	#plot using scaling of max phasor radius length
	plot(max(max_R))
	#plot the graph and scale to match the phasors.
	#plot(maximum(phase_A.radius, phase_B.radius, phase_C.radius))

'''
Adds a vector to the plot. Inputs are polar coords and color of line. 
Author: Brandon Johnson.
Date created: 10/27/2019
'''
def plot_vector(start_x, start_y, radius, angle, c):
	x,y = pol2cart(radius,angle)
	plt.quiver(start_x, start_y, x, y, angles='xy', scale_units='xy', scale=1, color=c)

'''
Finally plots the graph and post processing.
max input helps scale the graph. 
Author: Brandon Johnson.
Date created: 10/27/2019
'''
def plot(max):
	plt.xlim(-max*1.1, max*1.1)
	plt.ylim(-max*1.1, max*1.1)
	plt.grid()
	plt.gca().set_aspect('equal', adjustable='box')
	plt.show()
	
'''
Converts cartesian coordinates to polar. 
Output for angle is degrees
Author: Brandon Johnson.
Date created: 10/27/2019
'''
def cart2pol(x, y):
	rho = np.sqrt(x**2 + y**2)
	phi = np.arctan2(y, x)*180/math.pi
	return(round(rho,2), round(phi,2))
	
'''
Converts polar coordinates to cartesian. This function
is used when plotting each phase. Angles are inputed in degrees
Author: Brandon Johnson.
Date created: 10/27/2019
'''
def pol2cart(rho, phi):
	phi = phi*math.pi/180
	x = rho*np.cos(phi)
	y = rho*np.sin(phi)
	return(round(x,2),round(y,2))

'''
Finds max of 3 numbers. Used for scaling plot.
Author: Brandon Johnson.
Date created: 10/27/2019
'''
def maximum(a, b, c): 
    list = [a, b, c] 
    return max(list) 
	
if __name__ == "__main__":
	main()
	
