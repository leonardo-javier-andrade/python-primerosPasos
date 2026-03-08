# creamos una lista con elementos

lista = [1,2,3,4]

# msotramos el id de la lista y vemos en que parte de la memoria se encuentra 
print(lista)
print(id(lista))


# creamos una nueva lista y le asignamos el valor de la lista anterior

list_1= lista
print(list_1)
# Aqui se muestra el id de la nueva lista y vemos que tiene el mismo que la anteiror lista
print(id(list_1))


#Ahora si modificamos la lista original tmb se modifica la nueva list_1

lista.append(5)

print(lista)
print(list_1)
print(id(lista))
print(id(list_1))
#para evitarlo lo que debemos hacer es clonar la lista originar 

list_2 = list(lista)
print(id(list_2))


#otra forma de clonarlo es

list_3 = lista[::]

print(id(list_3))


#LIST COMPREHENSION
#funciones que se le puede dar al crear listas como rangos, modificar nuevas listas, o filtrar numeros pares entre otros
l1 = list(range(10))

print(l1)

l2= [i *10 for i in l1]
print (l2)


l3=[i for i in l1 if i%2==0]

print(l3)