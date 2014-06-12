import sciscipy

def polyrange(pol,x_range,xlabel,ylabel):
	code_string1 = "x = " + x_range + ";"
	code_string2 = "y = " + pol + ";"
	code_string3 = "plot(x,y);"
	code_string4 = "xtitle('Function Plot','" + xlabel + "','" + ylabel + "');"
	code_string5 = "xgrid();"

	code_string = code_string1 + code_string2 + code_string3 + code_string4 + code_string5
	sciscipy.eval(code_string)
		
