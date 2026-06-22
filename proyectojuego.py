print ("BIENVENIDO AL JUEGO")#Mensajes de bienvenida al juego
print("ADIVINA EL NUMERO")

# Genera un número entero entre 1 y 25 (ambos incluidos)
import random
NumeroGenerado = random.randint(1, 25)


print("El sistema ha generado un numero entre el 1 y el 25 si lo adivinas te puedes llevar una enorme sorpresa")
print("Ingresa tu numero ")
NumeroIngresado = int(input())#En esta seccion el usuario ingresa su numero

#Comparamos el numero
while NumeroGenerado!=NumeroIngresado:
    if NumeroIngresado > NumeroGenerado:
        print("El numero que ingresaste es mayor al numero sorpresa")
    elif NumeroIngresado < NumeroGenerado:
        print("El numero que ingresaste es menor a numero sorpresa")
    else :
        print("Felicidades el numero ingresado es el correcto")