menu = """ Bienvenido al sistema de ingreo de usuarios, por favor selecciones una opcion:
[1] Ingresa el nombre del usuario
[2] Ingresa la edad del usuario
[3] Ingresa el correo del usuario
"""

print(menu)

opcion = input ("Ingrese la opcion deseada:")

if opcion == "1":
    nombre = input ("ingrese su nombre: ")
    if nombre.isalpha():
        print ( F"su nombre es {nombre}")
    else:
        print ("Su nombre ingresado no es valido")
elif opcion == "2":
    edad = input ("Ingrese su Edad: ")
    if edad.isnumeric():
        print( f"La edad ingresada es: {edad} ")
    else: 
        print("Debe ingresar una edad correcta")
elif opcion == "3":
    email = input ("Ingrese su email: ")
    if email.find("@")>0 and email.find(".")>0:
        print( f"El mail ingresado es: {email} ")
    else: 
        print("Debe ingresar un email correcto")
else :
    print ("ingrese una opcion del 1 al 3")