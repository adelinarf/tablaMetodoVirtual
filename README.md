# Manejador de tablas de métodos virtuales
### Pregunta 4
Este programa permite manejar las definiciones de clases, subclases y describir los métodos que cada una de estas poseen. Se debe correr el archivo tablasMetodosVirtuales.py al igual que cualquier archivo de Python y se reciben las entradas por consola.

    python tablasMetodosVirtuales.py

## Entradas
Las entradas en el programa pueden ser:

    CLASS nombreDeLaClase metodos
    CLASS nombreDeLaClase : nombreDeLaSuperClase metodos
    
Ejemplo:

    CLASS A f g
    CLASS B : A f j l
    
Se pueden describir los métodos de la clase con:

    DESCRIBIR nombreDeLaClase
    
 Ejemplo:
 
    DESCRIBIR A
    
 Y se finaliza el programa con:
 
    SALIR

## Herencia
El programa puede manejar la herencia simple como A: B o B: C siempre que B y C estén definidas al momento de definir la subclase. Por esto, el ciclo de las herencias no es posible. La herencia en ciclo como:

    CLASS A : C
    CLASS C : D
    CLASS D : A

No es posible en este programa, ya que al definir A se necesita haber definido C, pero C es subclase de D, por lo que D debe estar definida y no puede ser subclase de A, porque A debe definirse anteriormente. Por esto, se puede modificar este código para el manejo de ciclos en las herencias, aunque debido a la definición dada no es necesario el manejo de las herencias cíclicas en estos momentos. No es posible generar herencias cíclicas con este programa.

## Code Coverage
El code coverage se verificó con la herramienta Coverage.py (https://coverage.readthedocs.io/en/6.4.1/) y se obtuvo un 90% de coverage para el archivo tablasMetodosVirtuales.py
