# Symmetrical-Components-Visualization
In this project, I use python to visualize one of the most important concepts in Power Systems Engineering, the Method of Symmetrical Components.
![Example_1](https://github.com/BJohnson98/Symmetrical-Components-Visualization/blob/master/Examples/example_1.png)

The Theorem of Symmetrical Components states that given an unsymmetric set of N phasors, it can be represented by the sum of N symmetrical sets of phasors. This is very useful in fault analysis of power systems. It is really easy to solve circuits that are symmetric, but really hard to solve unsymmetric circuits. Symmetrical componenents allows us to solve unsymmetric circuits (like a faulted 3-phase circuit) by allowing us to analyze each of the symmetrical sets individually. 

There are two versions of the same code:
* Symmetrical_Components.py (only the 3-phase case and code written poorly)
* General_symmetrical_components.py (works for any phase and also written well)

When I first started this project I only tried to see if I could do the three phase case, because almost all power systems user three phases. I was inspired after reading this old set of iowa state EE 457 [notes](http://home.engineering.iastate.edu/~jdm/ee457/SymmetricalComponents1.pdf)

A realistic example is a line-to ground fault on the power system. this would mean that one of the phase voltages would go to 0, the system below shows how these 2 symmetric sets, and 1 unsymmetric but equal set form our original system.

# 3-Phase system where the C-phase is shorted.
![Example_2](https://github.com/BJohnson98/Symmetrical-Components-Visualization/blob/master/Examples/3_Phase_Case.png)


After I was able to get the three phase case I wondered if I would be to recreate this for every case. The idea was to first ask the user how many phases they would want to enter, and it would show the phasors they entered broked down into N symmetric sets. This is largely impractical because there are not any 4-phase, 5-phase, 6-phase power systems but I was really intrigued how these graphs would look after I saw how cool the looked for the three phase case. I couldn't find anyone else who made something similiar to this so I had to a lot of research on how I would extend this concept, Thanks to wikipedia I found that higher order symmetrical components are just [Discrete fourier transforms](https://en.wikipedia.org/wiki/DFT_matrix).

# 4-Phase example
![Example_1](https://github.com/BJohnson98/Symmetrical-Components-Visualization/blob/master/Examples/4_Phase_Example.png)
# 5-Phase example
![Example_1](https://github.com/BJohnson98/Symmetrical-Components-Visualization/blob/master/Examples/5_Phase_example.png)
# 6-Phase example
![Example_1](https://github.com/BJohnson98/Symmetrical-Components-Visualization/blob/master/Examples/6_Phase_Example.png)
# 8-Phase example
![Example_1](https://github.com/BJohnson98/Symmetrical-Components-Visualization/blob/master/Examples/8_Phase_Example.png)
# 10-Phase example
![Example_3](https://github.com/BJohnson98/Symmetrical-Components-Visualization/blob/master/Examples/10_Phase_Example.png)
# 30-Phase example
![Example_1](https://github.com/BJohnson98/Symmetrical-Components-Visualization/blob/master/Examples/30_Phase_Case.png)
