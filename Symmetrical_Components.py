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

class phasor:
	def __init__(self, radius, angle):
		self.radius = radius
		self.angle = angle
	def cart(self):
		x = self.radius*np.cos(self.angle*math.pi/180)
		y = self.radius*np.sin(self.angle*math.pi/180)
		z = round(x,2) + round(y,2)*cmath.sqrt(-1)
		return(z)

#alpha operator 1<120
a= -0.5+0.866j
#Symmetrical Components Matrix
A = np.array([[1, 1   , 1   ],
			  [1, a**2, a   ],
			  [1, a   , a**2]]) 

#quiver plots (start_x,start_y,end_x,end_y)
def main():

	#Inputing the 3 phasors to seperate into its sequence components	
	A_radius = int(input("Enter Phase A's radius: "))
	A_angle = int(input("Enter Phase A's angle: "))
	phase_A = phasor(A_radius, A_angle)
	B_radius = int(input("Enter Phase B's radius: "))
	B_angle = int(input("Enter Phase B's angle: "))
	phase_B = phasor(B_radius, B_angle)
	C_radius = int(input("Enter Phase C's radius: "))
	C_angle = int(input("Enter Phase C's angle: "))	
	phase_C = phasor(C_radius, C_angle)

	#creating a 3x1 array of the 3 unbalanced phases
	unbalanced = np.array([phase_A.cart(), phase_B.cart(), phase_C.cart()])
	#dot product of 3 components with A matrix
	sequence_components = np.dot(np.linalg.inv(A), unbalanced)

	Va0 = sequence_components[0]
	Va_pos = sequence_components[1]
	Va_neg = sequence_components[2]
	


	plot_vector(0, 0,phase_A.radius, phase_A.angle, 'r')
	plot_vector(0, 0,phase_B.radius, phase_B.angle, 'y')
	plot_vector(0, 0,phase_C.radius, phase_C.angle, 'b')
	plot(maximum(phase_A.radius, phase_B.radius, phase_C.radius))

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
