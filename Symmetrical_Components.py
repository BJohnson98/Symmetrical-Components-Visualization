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
	def __init__(self, radius=0, angle=0):
		self.radius = radius
		self.angle = angle
	def cart(self):
		x = self.radius*np.cos(self.angle*math.pi/180)
		y = self.radius*np.sin(self.angle*math.pi/180)
		z = round(x,2) + round(y,2)*cmath.sqrt(-1)
		return(z)
	def get_real(self):
		return(round(self.radius*np.cos(self.angle*math.pi/180),2))
		
	def get_imaginary(self): 
		return(round(self.radius*np.sin(self.angle*math.pi/180),2))
	#allows you to input a new phasor in cartesian form.
	def input_cart(self, real, imag):
		self.radius = round(np.sqrt(real**2 + imag**2),3)
		self.angle = round(np.arctan2(imag, real)*180/math.pi,2)
	
	def rotate(self, alpha):
		self.angle = self.angle + alpha

#alpha operator 1<120
a= -0.5+0.866j
#Symmetrical Components Matrix
A = np.array([[1, 1   , 1   ],
	      [1, a**2, a   ],
	      [1, a   , a**2]]) 

def main():
	#defining the sequence components phasors
	Va0 = phasor()
	Va_pos = phasor()
	Va_neg = phasor()
	
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
	#dot product of 3 components with inverse A matrix to solve for the positive, negative, and zero sequence components
	sequence_components = np.dot(np.linalg.inv(A), unbalanced)

	#inputing the sequence components into the sequence phasors.
	Va0.input_cart(sequence_components[0].real, sequence_components[0].imag)
	Va_pos.input_cart(sequence_components[1].real, sequence_components[1].imag)
	Va_neg.input_cart(sequence_components[2].real, sequence_components[2].imag)

	#plot the sequence components for phase_A,
	#the order is the positive, negative, then zero sequence components
	plot_vector(0,0, Va_pos.radius, Va_pos.angle, 'orange')
	plot_vector(Va_pos.get_real(),Va_pos.get_imaginary(), Va_neg.radius, Va_neg.angle, 'black')	
	plot_vector(Va_pos.get_real()+Va_neg.get_real(), Va_pos.get_imaginary()+Va_neg.get_imaginary(), Va0.radius, Va0.angle, 'green')
	
	#rotate the positive and negative sequence components to get phase_B
	Va_pos.rotate(-120)
	Va_neg.rotate(120)
	
	#plot the sequence components for phase_B
	plot_vector(0,0, Va_pos.radius, Va_pos.angle, 'orange')
	plot_vector(Va_pos.get_real(),Va_pos.get_imaginary(), Va_neg.radius, Va_neg.angle, 'black')	
	plot_vector(Va_pos.get_real()+Va_neg.get_real(), Va_pos.get_imaginary()+Va_neg.get_imaginary(), Va0.radius, Va0.angle, 'green')	
	
	#rotate the positive and negative sequence components to get phase_C
	Va_pos.rotate(-120)
	Va_neg.rotate(120)
	
	#plot the sequence components for phase_C
	plot_vector(0,0, Va_pos.radius, Va_pos.angle, 'orange')
	plot_vector(Va_pos.get_real(),Va_pos.get_imaginary(), Va_neg.radius, Va_neg.angle, 'black')	
	plot_vector(Va_pos.get_real()+Va_neg.get_real(), Va_pos.get_imaginary()+Va_neg.get_imaginary(), Va0.radius, Va0.angle, 'green')
	
	#plot the original unbalanced 3 phases
	plot_vector(0, 0,phase_A.radius, phase_A.angle, 'r')
	plot_vector(0, 0,phase_B.radius, phase_B.angle, 'y')
	plot_vector(0, 0,phase_C.radius, phase_C.angle, 'b')
	
	#plot the graph and scale to match the phasors.
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
