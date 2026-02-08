#Variable Global

x=9.242

n="Hola Mundo"


#Variable Local con un scope determinado solo a su funcion

def funcion1():
    x = 1234
    global z
    z = "variable globa"
    print (x, id(x) ,sep= "---->")
    print (n, id(n) ,sep= " --esta variable es global---->")

def funcion2():
    x = "texto"
    print (x, id(x) ,sep= "---->")
    print (n, id(n) ,sep= " --esta variable es global---->" )
    print (z, id(z) ,sep= " --esta variable es global exportada de funcion 1---->" )

print (x, id(x) ,sep= "---->")
funcion1()
funcion2()
