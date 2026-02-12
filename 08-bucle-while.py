#bucle "while" se utiliza hasta que cambie una condicion o criterio

a = 0

while a< 100:
    print (a)
    a = a+1
print ("Fin del bucle")


#utilizacion de "Break" finaliza automaticamente el bucle
b=0
while b < 100:
    print (b)
    b += 1
    if b>10:
        break

print ("El bucle ha finalizado")

#utilizacion de "Continue" salta a la siguiente iteracion del bucle

c= 0

while c <100:
    c +=1
    if c%2 == 0:
        print (c)
        continue
print ("Fin del bucle continue")




#---------------------------------------------------------

#Reto 1: Crear un programa con cuenta regresiva de 10 hasta 0 y que al terminar diga "Fuego"

for i in range (10,-1,-1):
    print (i)
print("Fuego!")

#Reto 2: Entre los numero 1 y 100, se piden los multiplos de 4 y mostras la suma de todos los multiplos de 4

i=0
sumaM4=0
while i <101:
    i +=1
    if i%4==0:
        print (i)
        sumaM4= i + sumaM4
        continue
print("el bucle multiplo de 4 finalizo")

print ( f"la suma total de los multiplos de 4 es {sumaM4}")

#Reto 3: Cree un programa en e cual se pueda mostrar el factorial de cualquier numero y que sea visible en la terminal

numero = int(input("ingrese el numero que desee calcular: "))
a = numero 

print (f"{numero}! = ", end=" ")
resultado = 1
while a > 0:
    if a == numero:
        print (f"{a}", end= " ")
        resultado =  a * resultado
        a=a-1
        continue
    print (f"x {a} ", end= " ")
    resultado =  a * resultado
    a= a -1

print (f" resultado es = {resultado}")