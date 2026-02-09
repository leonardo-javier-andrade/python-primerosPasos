# Bucle "For" se utiliza generalmetne cuanto se sabe de antemano cuantes veces se va a iterar el codigo


for i in range(0,10): #range se refiere a el rango en que arranca y termina el indice "i"
    print (i)
print("fin del bucle")

for i in range (0,20,2): # en el rango se puede modificar la cantidad en la que se suma el indice
    print(i)
print("fin del bucle cada dos")


#Bucle "for" tambien puede ser utilizado para iterar cadenas caracter por caracteres

texto = "Ejemplo de texto para iterar"

for caracter in texto:
    print(caracter)

print("fin del bucle sting")