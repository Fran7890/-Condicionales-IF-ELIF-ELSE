#Realice un programa que lea tres números, muestre cuál es el mayor y determine si es par o impar.
def mayor_y_par_o_impar(num1, num2, num3):
    mayor = max(num1, num2, num3)
    print("El mayor número es:", mayor)
    
    if mayor % 2 == 0:
        print("El número mayor es par.")
    else:
        print("El número mayor es impar.")

if __name__ == "__main__":
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))

    mayor_y_par_o_impar(num1, num2, num3)

    
    
    
    
    