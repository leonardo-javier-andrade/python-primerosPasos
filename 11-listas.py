    # las listas son arregos que permiten almacenar diferentes datos en una sola variable (pudiendo tener diferentes tipos)

# creacion de lista

objetos = [7, "Hola", True, 3.4]

# podemos averiguar la longitud de los item de la lista

len(objetos)

# podemos agregar un item al final de la lista

objetos.append("nuevo objeto")


# Tambien podemos agregar mas un objeto o otra lista

objetos.extend (["cosa uno", 7, False])

print(objetos)

# Se puede insertar un objeto en algun lugar especifico de la lista --- por ejemplo entre Hola y True

objetos.insert(2 ,"objeto insertado en donde uno quiere")

print(objetos)

# Se puede remover un elemento poniendo el valor de la lista --- por ejemplo remover True 

objetos.remove(True)

print(objetos)

# Se puede revover por numero de indice de la lista --- por ejemplo remover el indice 2 ("objeto insertado...")

objetos.pop(2)

print(objetos)