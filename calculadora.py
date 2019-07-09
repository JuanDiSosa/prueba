#Interfaz para Calculadora
#Importar funciones desde otro archivo
from funcionescalculadora import * #puedes seleccionar la funcion especifica
from raices import raices

print("Calculadora SAM\nIntroduce el numero de la operacion a hacer, o presiona Q para salir:")
print("[1.-Suma] [2.-Resta] [3.-Multiplicacion]\n[4.-Division] [5.-Pontencia] [6.-Modulo]\n[7.-Raices polinomio segundo grado]")
x = input("X= ")
while x != "Q":
    if x == "1":
        suma(x)
        break
    elif x == "2":
        resta(x)
        break
    elif x == "3":
        Multiplicacion(x)
        break
    elif x == "4":
        divide(x)
        break
    elif x == "5":
        Potencia(x)
        break
    elif x == "6":
        modulo(x)
        break
    elif x == "7":
        raices()
        break
    else:
        print(f"{x} VALOR NO VALIDO")
        print("-------------------------------------------")
        x1 = input("Quieres reintentarlo? (y/n) ")
        while x1 != "y" or "n":
            if x1 == "y":
                x = input("Introduce el numero de la operacion a hacer, o presiona Q para salir:")
                break
            elif x1 == "n":
                print("Gracias por usar SAM")
                x = "Q"
                break
            else:
                print(f"{x1} valor no valido")
                x1 = input("Quieres reintentarlo? (y/n) ")

print("End")
