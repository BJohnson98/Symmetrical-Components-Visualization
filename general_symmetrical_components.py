'''
In my previous progam, I visualized symmetrical components of the 3-Phase case only. 
In this program I will allow the user to enter how many phases they want. This requires
a general method for solving symmetrical components and requires the Discrete Fourier Transform
Matrix. This matrix is dynamically generated. The method I used is described here:
https://en.wikipedia.org/wiki/DFT_matrix
Author: Brandon Johnson
Date Started: 11/6/2019
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
	color = ['red','y','blue','orange','green','magenta','cyan','brown','purple','skyblue','tomato','springgreen']
	alphabet = ascii_uppercase
	num_phases = 0
	#define and undetermined amount of phases.
	phasor_list = []
	# Want to keep track of the maxium radius size inputted. 
	max_R = []
	sequence_list = []

	#ask user to input the number of phases they want.
	while num_phases < 3:
		num_phases = int(input("How many phases do you want to enter?:\n"))
		if num_phases < 3:
			print("Please enter more then 2 phases")

	#create unbalanced array to dot with the A_matrix. 	
	unbalanced = np.zeros(shape=(num_phases), dtype=complex)
		
	#now ask the user to enter the values for the phases.
	for i in range(num_phases):
		radius = float(input(f"Enter Phase {alphabet[i%26]}'s radius: "))
		angle = float(input(f"Enter Phase {alphabet[i%26]}'s angle: "))	
		#add phasors to the list and cartesian coordinates to unbalanced array
		phasor_list.append(phasor(radius, angle))
		unbalanced[i] = phasor_list[i].cart()
		max_R.append(radius)
	
	#Create alpha 
	alpha = 360/num_phases
	a = phasor(1,alpha)
	
	#create the numpy array
	A_Matrix = np.zeros(shape=(num_phases,num_phases), dtype=complex)
	#create the matrix
	for row in range(num_phases):
		for col in range(num_phases): 
			#this equation helps us create a DFT_matrix.
			A_Matrix[row][col] = a.cart()**((row*col)%num_phases)
	
	#Get the sequence components by dotting A_matrix(-1) * the unbalanced phases 
	sequence_components = np.dot(np.linalg.inv(A_Matrix), unbalanced)
	
	#I take the sequence components matrix and I put it into a list of phasor objects. 
	#I do this to make plotting all n*n sequence components much easier. 
	for i in range(num_phases):
		sequence_list.append(phasor())
		sequence_list[i].input_cart(sequence_components[i].real, sequence_components[i].imag)
	
	#plots all of the sequence components for every phase.
	for i in range(num_phases):
		start_x = 0
		start_y = 0
		#Plot all the sequence components for the current phase. 
		for j in range(num_phases):
			plot_vector(start_x, start_y, sequence_list[j].radius, sequence_list[j].angle, color[(num_phases+j)%len(color)])
			start_x += sequence_list[j].get_real() 		
			start_y += sequence_list[j].get_imaginary()	
		#rotates the vectors for the next phase.
		for j in range(num_phases):
			sequence_list[j].rotate((alpha*j)%360)
	
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
	
