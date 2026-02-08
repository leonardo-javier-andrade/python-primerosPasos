def saludo(nombre):
    print(f"Buenos dias {nombre}")
    print("Bienvenido al curso")


tunombre= input("ingresa tu nombre: ")

saludo(tunombre)


#Funcion de resta

def resta(a,b):
    if a== None or b== None:
        print("Debe ingresar dos numeros para realizar la resta")
        return 
    
    return a-b



num1 = int(input("ingrese el primer numero a restar: "))
num2= int(input("ingrese el segundo numero a restar: "))

c= resta(num1,num2)

print(f"la resta de {num1} menos {num2} es igual a: {c}")



# Funcion de conversion de grados

def convertirgrados(grados,unidad):
    if unidad == "c" or unidad == "C":
        resultado = grados * 1.8 + 32

        print ( resultado , "K")

    elif unidad == "k" or unidad == "K":
        resultado = (grados -32)/1.8
        print (resultado , "C")


temp= int(input("ingrese el valor en numero de la temperatura: "))
tipo= input ("Ingrese el tipo de unidad Celcius (C) o Kelvil (K)")

convertirgrados(temp,tipo)