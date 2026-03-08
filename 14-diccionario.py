#Creacion de diccionario que contiene un key y un valor

diccionario_ejemplo = {'string':"hola", 'bool': True, 'int': 9, 'float': 4.3}

#ahora podemos acceder al valor desde el key

print (diccionario_ejemplo)

def run ():
    diccionario = {'string':"hola", 'bool': True, 'int': 9, 'float': 4.3}
    print(diccionario['bool'])

if __name__ == '__main__':
    run()




#Creacion de diccionarios con diferentes elementos

dic1={ 'nombre': "tienda", 
      'item':['lapiz', 'carpeta', ' borrador'],
      'cantidad': [2,5,1],
      'precio': [24,12,5]
      }

#si uno quiere acceder al borrador, deberia hacerlo de la siguiente manera

print ( dic1['item'][2])

#Si uno desea agreagar un dato nuevo al diciconario 

dic1['estado']="nuevo"

print(dic1)
#si uno desea borrar algo especifico

del dic1['cantidad']


print(dic1)

# si uno desea imprimir solo los valores o las llaves 

print (dic1.values())

print(dic1.keys())


#se puede imprimir los item como tuplas para luego trabajar con ellos

print (dic1.items())


#si uno desea trabajar con los datos puede hacerlo de la siguiente forma

for i,j in dic1.items():
    print (f'Su {i} es {j}')


#-----------DICCIONARIO COMPRENHENSION---

#crear una lista en el rango de -10 a o en donde el valor del key sea el numero par y elevado al cuadrado

def main():
    ejercicio={}
    for i in range(-10,0):
        if i % 2 == 0:
            ejercicio[i]= i**2
    print(ejercicio)

if __name__== '__main__':
    main()


#Aplicacmos el comprenhension realizando el mismo ejercicio en 1 linea

dicc={x:x**2 for x in range(-10,0) if x%2==0 }


print(dicc)

#Se puede utilizar para modificar un diccionario ya existente,

dic_one={'a':1, 'b':2, 'c':3, 'd':4}

dic_triple={ k:v*3 for (k,v) in dic_one.items()}

print(dic_one)
print(dic_triple)


#Ejercicio es aplicar un impuesto de 19% a una lista de precio ya existente

old_price= { 'Milk':0.75, 'meat':10.69, 'eggs': 2.14, 'bread': 1.07 }


new_price={ k: v + (v*19)/100  for (k,v) in old_price.items()}

print(f' el precio viejo es {old_price}')

print(f' el precio nuevo es {new_price}')
