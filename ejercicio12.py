#Realice un programa que pida un número del 1 al 12 y diga el nombredel mes correspondiente.
meses_del_año=int(input("ingrese el mes del año que desea saber:"))
meses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
if meses_del_año <= 12:
    print(f"el mes que desea saber es {meses[meses_del_año]}") 
