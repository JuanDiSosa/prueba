def raices():
    print("A="); A = float(input())
    print("B="); B = float(input())
    print("C="); C = float(input())
    #print(f"{(-1*B)-((B**2) - (4*A*C)**(-2))/(2*A)}")
    if ((B**2) - (4*A*C)) > 0:
        print(f"Dos raices reales distintas")
        print(f"X1 = {(((-1)*B) - (B**2 - 4*A*C)**(0.5))/(2*A)}")
        print(f"X2 = {(((-1)*B) + (B**2 - 4*A*C)**(0.5))/(2*A)}")
    elif ((B**2) - (4*A*C)) == 0:
        print(f"Una raices real nada mas")
        print(f"X = {(((-1)*B))/(2*A)}")
    else:
        print(f"No tiene raices reales")
    return print("End")
