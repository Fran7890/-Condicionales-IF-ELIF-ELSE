#Confeccione un programa que pida un número del 1 al 7 y diga el día de la semana correspondiente.
semana=int(input("ingrese un numero del dia :"))
semana_numero= ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
if semana <= 7 :
 print(f" es el dia {semana_numero[semana]} correcto")

