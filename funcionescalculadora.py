#Funciones de la calculadora
def suma(e):
    print ("A="); a=float(input())
    print ("B="); b=float(input())
    return(print(f"{a+b}"))

def resta(x):
    print ("A="); a=float(input())
    print ("B="); b=float(input())
    return(print(f"{a-b}"))

def Multiplicacion(x):
    print ("A="); a=float(input())
    print ("B="); b=float(input())
    return(print(f"{a*b}"))

def divide(x):
    print ("A="); a=float(input())
    print ("B="); b=float(input())
    while b==0:
        print (f"{b} no se puede dividir entre cero")
        print ("B="); b=float(input())
    return(print(f"{a/b}"))

def Potencia(x):
    print ("A="); a=float(input())
    print ("B="); b=float(input())
    return(print(f"{a**b}"))

def modulo(x):
    print ("A="); a=float(input())
    print ("B="); b=float(input())
    return(print(f"{a%b}"))
