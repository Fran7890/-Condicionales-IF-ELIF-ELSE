#ejercicio_2.py2
#Realice un programa que le permita al usuario simular el pago ingresando el importe y la forma de pago:
#• Contado (1): se aplica un descuento del 10% al importe
#• Tarjeta (2): se aplica un interés de 10%
#• Débito (3): se aplica un descuento del 5%
#Mostrar el importe, el descuento o interés y el importe total.

def calcular_pago(importe, forma_pago):
    if forma_pago == 1:  # Contado
        descuento = importe * 0.10
        total = importe - descuento
    elif forma_pago == 2:  # Tarjeta
        interes = importe * 0.10
        total = importe + interes
    elif forma_pago == 3:  # Débito
        descuento = importe * 0.05
        total = importe - descuento
    else:
        print("Forma de pago no válida")
        return None
    
    return total

def main():
    try:
        importe = float(input("Ingrese el importe: "))
        forma_pago = int(input("Ingrese la forma de pago (1: Contado, 2: Tarjeta, 3: Débito): "))

        total = calcular_pago(importe, forma_pago)
        if total is not None:
            print("El total a pagar es:", total)
    except ValueError:
        print("Error: Ingrese un importe válido.")

if __name__ == "__main__":
    main()
