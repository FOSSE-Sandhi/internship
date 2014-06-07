#!/usr/bin/python

import sciscipy

def csim(P,I,D,n0,n1,n2,n3,d0,d1,d2,d3,u):
	
	code_string1 = "s = %s;"

	# If the plant simulation is not required, the block functions as a controller block.
	if n0 == 0 and n1 == 0 and n2 == 0 and n3 == 0 and d0 == 0 and d1 == 0 and d2 == 0 and d3 == 0:
		code_string2 = "Gc = syslin('c'," + str(P*I) + "*s + " + str(D) + "*s^2 + 1," + str(I) + "*s);"
		code_string3 = "r = tf2ss(Gc);"
		code_string4 = "u = " + str(u) + ";"
		code_string5 = "y = csim(u,1:length(u),r)"
		code_string = code_string1 + code_string2 + code_string3 + code_string4 + code_string5
	# If the Controller simulation is not required, the block functions as a plant block
	elif P == 0 and I ==0 and D == 0:
		code_string2 = "G = syslin('c'," + str(n0) + "*s^3 + " + str(n1) + "*s^2 + " + str(n2) + "*s + "+ str(n3)+ "," + str(d0) + "*s^3 + " + str(d1) + "*s^2 + " + str(d2) + "*s + " + str(d3) + ");"
                code_string3 = "r = tf2ss(G);"
                code_string4 = "u = " + str(u) + ";"
                code_string5 = "y = csim(u,1:length(u),r)"
                code_string = code_string1 + code_string2 + code_string3 + code_string4 + code_string5
	# If combined plant and controller dynamics are required
	else:
		code_string2 = "Gc = syslin('c'," + str(P*I) + "*s + " + str(D) + "*s^2 + 1," + str(I) + "*s);"

		code_string3 = "G = syslin('c'," + str(n0) + "*s^3 + " + str(n1) + "*s^2 + " + str(n2) + "*s + "+ str(n3)+ "," + str(d0) + "*s^3 + " + str(d1) + "*s^2 + " + str(d2) + "*s + " + str(d3) + ");"
	
		code_string4 = "r = tf2ss(G*Gc);"
		code_string5 = "u = " + str(u)+ ";"
		code_string6 = "y = csim(u,1:length(u),r)"

		code_string = code_string1 + code_string2 + code_string3 + code_string4 + code_string5 + code_string6

	sciscipy.eval(code_string)
	y = sciscipy.read("y")
	return y


