#AREA PARA MIS FUNCIONES --> Reutilizacion de codigo

def mensaje(): #Declaracion

    print("Estamos aprendiendo Python.")
    print("Estamos aprendiendo instrucciones basicas.")
    print("Poco a poco iremos avanzando.")

def suma_2():
    num1 = 5
    num2 = 7
    print(num1+num2)

def suma(num1, num3): #la funcion recibe 2 parametros
    print(num1+num3)


def sumar(num1, num2, num3):
    resultado = num1+num2+num3
    return resultado

#AREA PRINCIPAL DE PYTHON

# Llamo a mis funciones, las veces que necesito.
mensaje() #Llamada funcion

suma(5, 6)

suma(2, 3)

suma_2()

print(sumar(7.2, 3.2, 8.2))

print(sumar(9.3, 9.5, 13.8))

almacena_resultado=suma(7, 6)

print(almacena_resultado)