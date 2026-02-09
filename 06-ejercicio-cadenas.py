#poder manipular cadenas de texto
#funciones de candenas: seleccion de una parte

#Definir una cadena de texto

texto= "Hola curso de python"

#Seleccion de una parte de la cadena (un caracte o grupo de caracteres)

print (texto[0]) #selecciona el primer caracter de la cadena "H"


print(texto[3]) #selecciona el cuarto caracter de la cadena "a"

print (texto[0:4]) #selecciona los caracteres desde el indice 0 hasta el indice 3 "Hola"

# Seleccion de un grupo d ela cadena salteando caracteres

print (texto[0:20:2]) #selecciona los caracteres desde el indice 0 hasta el indice 19 saltando de a 2 "Hlcrs e yhn"



#Funcion de cadena: longitud de la cadena

print (len(texto)) #devuelve la cantidad de caracteres que tiene la cadena "19"

#Funcion de conteo de caracteres

print (texto.count("o")) #devuelve la cantidad de veces que aparece el caracter "o" en la cadena "3"

print (texto.count("x", 8, 19)) #devuelve la cantidad de veces que aparece el caracter "a" en la cadena desde el indice 8 hasta el indice 18 "1"
#si no encuentra el caracter deseado devuelve "0"

#---------------------------------------------------------------------------------------------------

#TRANSFORMACION DE STRING (CADENAS)

#Funcion de cadena: convertir a mayusculas

print (texto.upper()) #convierte toda la cadena a mayusculas "HOLA CURSO DE PYTHON"

#Funcion de cadena: convertir a minusculas
print (texto.lower()) #convierte toda la cadena a minusculas "hola curso de python"

#Funcion de cadena: convertir a mayusculas la primera letra de cada palabra
print (texto.title()) #convierte la primera letra de cada palabra a mayuscula "Hola Curso De Python"

#Funcion de cadena: convertir a mayusculas la primera letra de la cadena
print (texto.capitalize()) #convierte la primera letra de la cadena a mayuscula "Hola curso de python"  

#Funcion de cadena: eliminar espacios al inicio y al final de la cadena

texto2 = "   Hola curso de python   "   
print (texto2.strip()) #elimina los espacios al inicio y al final de la cadena "Hola curso de python"
        #variante de strip: lstrip() elimina los espacios al inicio de la cadena y rstrip() elimina los espacios al final de la cadena


#Funcion de cadena: reemplazar un caracter o grupo de caracteres por otro
print (texto.replace("curso", "Bienvenido a")) #reemplaza la palabra "curso" por "Bienvenido a" en la cadena "Hola Bienvenido a de python"  

#----------------------------------------------------------------------------

#Funcion de cadena: dividir una cadena en una lista de palabras

print (texto.split()) #divide la cadena en una lista de palabras ["Hola", "curso", "de", "python"]  

lista_palabras = texto.split() #guarda la lista de palabras en una variable

#Funcion de cadena: unir una lista de palabras en una cadena

print ("-".join(lista_palabras)) #une la lista de palabras en una cadena separada por guiones "Hola-curso-de-python"
texto = " ".join(lista_palabras) #une la lista de palabras en una cadena separada por espacios "Hola curso de python"

print (texto)   

 
#Reto : Crear un programa que solicite nombre y apellido de Usuario 

#Que muestre 
#1-Nombre  completo con todas las letras mayusculas
#2- Nombre completo con todas las letras minusculas
#3- Que cuente cuantas letras tiene el nombre completo sin contar los espacios
#4 - Cuantas letras tiene el primer nombre


print("--------------RETO-------------")

nombre = input ("Ingrese su nombre completo: ")

print (f" su nombre ingresado es {nombre}")

print (f"#1 su nombre een mayuscula {nombre.upper()} ")

print (f"#2 su nombre en minuscula: {nombre.lower()}")

def Sinespacios():
    global lista
    lista = nombre.split()
    print(lista)
    global  nombreSinEspacios
    nombreSinEspacios = "".join(lista)
Sinespacios()
print(f"#3 la cantidad de caracteres sin escpacio es {len(nombreSinEspacios)}")


print (f"La cantidad de letras del primer nombre es: {len(lista[0])}")
