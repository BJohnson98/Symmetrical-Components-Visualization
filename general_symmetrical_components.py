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
	num_phases = 0
	#define and undetermined amount of phases.
	phasor_list = []
	max_R = []
	#ask user to input the number of phases they want.
	while num_phases < 3:
		num_phases = int(input("How many phases do you want to enter?:\n"))
		if num_phases < 3:
			print("Please enter more then 2 phases")
			
	#now ask the user to enter the values for the phases.
	for i in range(num_phases):
		radius = float(input(f "Enter Phase {alphabet[i%26]}'s radius: "))
		angle = float(input(f "Enter Phase {alphabet[i%26]}'s angle: "))	
		phasor_list.append(phasor(radius, angle))
		max_R.append(radius)
	
	#Create alpha 
	alpha = 360/num_phases
	a = phasor(1,alpha)
	
	
	
	'''
	Create the matrix
	'''
	
	'''
		plot vectors
	'''

	#prints the original list of phasors
	for i in range(num_phases):	
		print(phasor_list[i].radius, phasor_list[i].angle)
		plot_vector(0, 0, phasor_list[i].radius, phasor_list[i].angle, color[i%len(color)])
	#plot using scaling of max phasor radius length
	plot(max(max_R))

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
	
if __name__ == "__main__":
	main()
	
'''
4 case:

A3 =[1, 1  1 ]
	[1, a2 a ]
	[1, a  a2]

A4 =[1  1  1  1 ]
	[1  a3 a2 a ]
	[1  a2 a4 a2]
	[1  a  a2 a3]

A5 =[1  1  1  1  1 ]
	[1  a4 a3 a2 a ]
	[1  a3 a  a4 a2]
	[1  a2 a4 a  a3]
	[1  a  a2 a3 a4]

A6 =[1  1  1  1  1  1 ]    
	[1  a5 a4 a3 a2 a ]
	[1  a4 a2 a6 a4 a2]
	[1  a3 a6 a3 a6 a3]	
	[1  a2 a4 a6 a4 a2]	
	[1  a  a2 a3 a4 a5]

even case:	
A  = [1 .   .      .   . 1]
     [. n    n-1 
	 [. n-1 (n-1)/2
	 [. .   n
	 [. .	.
	 [1 n2  .      .   . n]
	 
Vandermonde matrix the value of alpha = alpha^(row*column)
'''
	
