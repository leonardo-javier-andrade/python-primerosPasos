def factorial (n):
    c=n
    f=1
    print (f"{c}! = ", end="")
    while ( c > 0):
        if c >1:
            print (f"{c} x", end= " ")
        else:
            print (f"x {c} = ", end= " ")
        f = c * f
        c=c-1
    print (f"{f} ")
    return f

print(__name__)

# estructuramos una funcion para que se ejecute solo si es el prog principal, y que no se ejecute en otros prog

if __name__ == "__main__":  
    factorial(7)
    a = factorial(5)


