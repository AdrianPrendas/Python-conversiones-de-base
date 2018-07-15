
### sub-rutinas ###
def print_options():
	print("""
		Promgrama de conversiones
		1.  decimal a binario
		2.  decimal a octal
		3.  decimal a hexadecimal
		4.  binario a decimal
		5.  binario a octal
		6.  binario a hexadecimal
		7.  octal a binario
		8.  octal a decimal
		9.  octal a hexadecimal
		10. hexadecimal a binario
		11. hexadecimal a decimal
		12. hexadecimal a octal
		13. salir
	""")

def decimal_a_binario():
	decimal = input("decimal: ")
	try:
		print( "binario = {0:08b}".format(int(decimal)) )
	except:
		print("Error ("+decimal+") no es decimal")

def decimal_a_octal():
	decimal = input("decimal: ")
	try:
		print( "octal = {0:o}".format(int(decimal)) )
	except:
		print("Error ("+decimal+") no es decimal")

def decimal_a_hexadecimal():
	decimal = input("decimal: ")
	try:
		print( "hexadecimal = {0:02x}".format(int(decimal)) )
	except:
		print("Error ("+decimal+") no es decimal")

def binario_a_decimal():
	binario = input("binario: ")
	try:
		print("decimal = %d"%(int(binario,2)))
	except:
		print("Error ("+binario+") no es binario")

def binario_a_octal():
	binario = input("binario: ")
	try:
		print("octal = {0:o}".format(int(binario,2)))
	except:
		print("Error ("+binario+") no es binario")		

def binario_a_hexadecimal():
	binario = input("binario: ")
	try:
		print("hexadecimal = {0:02x}".format(int(binario,2)))
	except:
		print("Error ("+binario+") no es binario")

def octal_a_binario():
	octal = input("octal: ")
	try:
		print("binario = {0:08b} ".format( int(octal,8) ) )
	except:
		print("Error ("+octal+") no es octal")

def octal_a_decinal():
	octal = input("octal: ")
	try:
		print("decimal = %d " % ( int(octal,8) ) )
	except:
		print("Error ("+octal+") no es octal")

def octal_a_hexadecimal():
	octal = input("octal: ")
	try:
		print("hexadecimal = {0:02x} ".format ( int(octal,8) ) )
	except:
		print("Error ("+octal+") no es octal")

def hexadecimal_a_binario():
	hexadecimal = input("hexadecimal: ")
	try:
		print("binario = {0:08b}".format(int(hexadecimal,16)))
	except:
		print("Error ("+hexadecimal+") no es hexadecimal")

def hexadecimal_a_decimal():
	hexadecimal = input("hexadecimal: ")
	try:
		print("decimal = %d" % ( int(hexadecimal,16) ) )
	except:
		print("Error ("+hexadecimal+") no es hexadecimal")

def hexadecimal_a_octal():
	hexadecimal = input("hexadecimal: ")
	try:
		print("octal = {0:o}".format( int(hexadecimal,16) ) )
	except:
		print("Error ("+hexadecimal+") no es hexadecimal")

def end():
	print("### find del programa ###")

###################################

def default():
	print("Error la opcion no existe")

def switch(k):
	return {
		1:decimal_a_binario,
		2:decimal_a_octal,
		3:decimal_a_hexadecimal,
		4:binario_a_decimal,
		5:binario_a_octal,
		6:binario_a_hexadecimal,
		7:octal_a_binario,
		8:octal_a_decinal,
		9:octal_a_hexadecimal,
		10:hexadecimal_a_binario,
		11:hexadecimal_a_decimal,
		12:hexadecimal_a_octal,
		13:end
	}.get(k,default)

def program():
	print_options()
	option = input("seleccione alguna opcion: ")
	switch(int(option))()
	if option != "13": program() # recursion


program() # inicio del programa