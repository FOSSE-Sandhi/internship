#!/usr/bin/python

import sciscipy


def csim(P,I,D,n0,n1,d0,d1,u):
	
	code_string1 = "s = %s;"
	code_string_u = "u = "+str(u)+";"


	#If the controller simulation is not required, the block functions as a plant block.
	if P == 0 and I == 0 and D==0:
		code_string2 = "G = syslin('c'," + str(n0) + "*s" + "+" + str(n1) + "," + str(d0) + "*s +" + str(d1) + ");"
		code_string3 = "r = tf2ss(G);"
		code_string4 = "y = csim(u,1:length(u),r)"
		code_string = code_string1 + code_string2 + code_string3 + code_string_u + code_string4

	# If the Plant simulation is not required, the block functions as a controller block.
	elif n0 == 0 and n1 == 0 and d0 == 0 and d1 == 0:
		code_string2 = "Gc = syslin('c'," + str(P*I+D)+"*s,("+str(I)+")*s);"
		code_string3 = "r = tf2ss(Gc);"
		code_string4 = "y = csim(u,1:length(u),r)"
		code_string = code_string1 + code_string2 + code_string3 + code_string_u + code_string4

	# Combining the plant and controller dynamics
	else:
		code_string2 = "Gc=syslin('c',("+str(P*I+D)+"*s)"+","+str(I)+"*s);"
		code_string3 = "G = syslin('c'," + str(n0) + "*s" + "+" + str(n1) + "," + str(d0) + "*s +" + str(d1) + ");"
		code_string4 = "r=tf2ss(G*Gc);"
		code_string5 = "y = csim(u,1:length(u),r)"
		code_string = code_string1 + code_string2 + code_string3 + code_string4 + code_string_u + code_string5
	

	import sciscipy
	sciscipy.eval(code_string)
	y = sciscipy.read("y")
	return y

if __name__ == "__main__":
	u = [0]*10
	u[5] = 1
	out = csim(2,0.5,0.6,0,0,0,0,u)
	print out

	import matplotlib.pyplot as plt
        plt.plot(out)
        plt.show()


