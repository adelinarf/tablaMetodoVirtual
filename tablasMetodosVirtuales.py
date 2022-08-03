#Manejador de tablas de metodos virtuales
'''La funcion verificarEntrada verifica que una lista de strings tenga el tamano 
   correcto segun la entrada que es, si es CLASS o DESCRIBIR
'''
def verificarEntrada(separacion,num):
	if num == 1:
		if 2>=len(separacion)>1:
			return True
		else:
			return False
	else:
		if ":" in separacion:
			if len(separacion)>4:
				return True
			else:
				return False
		else:
			if len(separacion)>2:
				return True
			else:
				return False
	return True

tipos = {} 
'''Este es el diccionario que alojara los tipos que se crean
   Los keys del diccionario tipos tienen la forma:
   clase : [Herencia,metodos] donde 
   metodos es una secuencia de string que representa a los metodos de la clase
   Herencia puede ser None si no es superclase o el nombre de la clase que es su 
   superclase
''' 

'''La funcion eliminarStringVacio toma una lista y verifica si contiene el string
   vacio o ''. Si alguna de sus posiciones contiene el '', no lo anade a la nueva
   lista que crea
'''
def eliminarStringVacio(lista):
	final = []
	for x in range(0,len(lista)):
		if lista[x]!='':
			final.append(lista[x])
	return final
'''La funcion nuevaSubClase toma una lista de entrada de usuario y verifica si
   ya existe. Como es una subclase, se guarda la herencia de la subclase en la lista
   de metodos de la clase y todo se aloja en tipos.
'''
def nuevaSubClase(lista):
	nombre = lista[0]
	superclase = lista[2]
	metodos = lista[3:]
	if nombre in tipos:
		print("La clase ya ha sido definida")
	if superclase in tipos:			
		if len(metodos) == len(set(metodos)):  #Si fuesen posibles los ciclos en la herencia aqui se verificarian
			tipos[nombre] = [superclase] + metodos
		else:
			print("Los metodos estan repetidos")
	else:
		print("La superclase "+ superclase+" no ha sido definida")
		
'''La funcion nuevaSubClase toma una lista de entrada de usuario y verifica si
   ya existe. Como es clase, se guarda la herencia como None y los metodos de
   la clase que esta definiendose. Todo se aloja en tipos.
'''
def nuevaClase(lista):
	nombre = lista[0]
	metodos = lista[1:]
	if nombre in tipos:
		print("La clase ya ha sido definida")
	else:
		if len(metodos) == len(set(metodos)):
			tipos[nombre] = [None] + metodos
		else:
			print("Los metodos estan repetidos")

'''La funcion nuevoTipo toma una lista de entrada de usuario y verifica si tiene
   : y es una subclase o si solo es una clase y llama a nuevaSubClase y 
   nuevaClase de acuerdo a esto
'''
def nuevoTipo(lista):
	if ":" in lista:
		nuevaSubClase(lista)
	else:
		nuevaClase(lista)

'''La funcion buscarMetodos se utiliza para conseguir los metodos de una 
   superclase cuando se desea describir una subclase de esta. Debido a que
   la subclase tambien se describe con los metodos de sus subclase, entonces
   se busca en todas las clases que sean subclase hasta llegar a una clase con 
   herencia None.
   Estos metodos se guardan en una lista de tuplas que define el primer elemento
   el nombre de la superclase y el segundo son sus metodos.
'''
def buscarMetodos(superclase):
	continua = True
	tiposDisponibles = []
	while continua:
		herencia = tipos[superclase][0]
		tiposDisponibles.append((superclase,tipos[superclase][1:]))
		if herencia == None:
			continua = False
		else:
			superclase = herencia
	return tiposDisponibles

'''La funcion conseguirMetodos recibe los metodos de una subclase, los 
   metodos de las superclases asociadas y el nombre de la subclase.
   Esta funcion itera sobre los metodos de las superclases y si alguno
   de estos metodos se encuentra en la clase, se imprime la def de esta,
   si no esta se imprimen los de las superclases.
   Ademas se guardan los impresos de la clase actual en una lista para
   evitar imprimirlos dos veces.
   Una vez impresos estos, se imprimen los metodos de la clase.
'''
def conseguirMetodos(metClase, metHerencia, clase):
	impresos = []
	for y in range(0,len(metHerencia)):
		metodos = metHerencia[y][1]
		for x in range(0,len(metodos)):
			if metodos[x] in metClase:
				print(metodos[x]+" -> "+clase+" :: "+metodos[x])
				impresos.append(metodos[x])
			else:
				print(metodos[x]+" -> "+metHerencia[y][0]+" :: "+metodos[x])
	for z in range(0,len(metClase)):
		if metClase[z] not in impresos:
			print(metClase[z]+" -> "+clase+" :: "+metClase[z])

'''La funcion describeTipo toma una lista de entrada de usuario y describe una
   clase o subclase basandose en sus metodos. Las clases buscan solo en los
   metodos alojados en su espacio de memoria en tipos.
   Pero las subclases buscan las herencias de su superclase hasta llegar a 
   una clase de herencia None y considera los metodos de todas las clases que
   puedan ser su superclase.
'''
def describeTipo(lista):
	nombre = lista[0]
	if nombre in tipos:
		clase = tipos[nombre]
		if clase[0]!=None:
			listaTupla = buscarMetodos(clase[0])  #(nombresuperclase,[metodos])
			metodosClase = clase[1:]
			conseguirMetodos(metodosClase,listaTupla,nombre)
		else:
			metodosClase = clase[1:]
			for x in range(0,len(metodosClase)):
				print(metodosClase[x]+" -> "+nombre+" :: "+metodosClase[x])
	else:
		print("La clase "+nombre+" no se ha definido.")

'''La funcion main recibe un input por consola que puede ser del tipo
	CLASS nombre metodos
	CLASS nombre : superclase metodos
	DESCRIBIR nombre
	SALIR
	La entrada se divide en una lista con el metodo split y se eliminan
	los strings vacios de dicha lista. Luego se verifica la entrada y si 
	no es una entrada valida, se indica en pantalla.
	Si es valida se realizara la operacion deseada.
'''
def main():
	funciona = True
	while funciona:
		entrada = str(input(":"))
		e1 = entrada.find("CLASS")
		e2 = entrada.find("DESCRIBIR")
		e3 = entrada.find("SALIR")
		if e1 == 0:
			separacion = eliminarStringVacio(entrada.split(" "))
			if verificarEntrada(separacion,0) == False:
				print("La entrada no es valida")
			else:
				separacion.pop(0)
				nuevoTipo(separacion)
		elif e2 == 0:
			separacion1 = eliminarStringVacio(entrada.split(" "))
			if verificarEntrada(separacion1,1) == False:
				print("La entrada no es valida")
			else:
				separacion1.pop(0)
				describeTipo(separacion1)
		elif e3 == 0 and len(entrada):
			print("Ha culminado el programa.")
			funciona = False
		if e1 != 0 and e2 != 0 and e3 != 0:
			print("La entrada no es valida")
main()
