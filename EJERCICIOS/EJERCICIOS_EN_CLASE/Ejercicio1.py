# 1. Una línea de código que muestre la fecha de hoy.
from datetime import date
print("Hoy es: " + str(date.today()))

# 2. Construir un convertidor de unidades de centimetros a metros (el formato del resultado deberá ser: X cm son igual a X metros, según el usuarios ingrese la cantidad a convertir).
dato1 = input('Ingresa la cantidad de centimetros que deseas convertir a metros')
resultado = int(dato1) / 100
print(str(dato1) + ' cm, son ' + str(resultado) + ' mts')

# 3. Exploremos cómo podemos crear un programa que pueda calcular la distancia entre dos planetas EN KILOMETROS Y EN MILLAS. Comenzaremos usando dos distancias de planetas al sol: Tierra (149.597.870 km) y Júpiter (778.547.200 km). Calcular cuanta distancia hay en kilometos y en millas entre estos dos planetas. Nota: Quita las comas cuando uses los valores.
tierra = 149597870
jupiter = 778547200
distanciakm = jupiter - tierra
distanciamill = distanciakm * 0.6
print(' La distancia entre Jupiter y la tierra es de ' + str(distanciakm) + ' KM, y de ' + str(distanciamill) + ' MILLAS')

# Crear una aplicación para trabajar con números y entrada de usuario

planeta1 = int(input ('Ingresa la distancia del primer planeta'))
planeta2 = int(input ('Ingresa la distancia del planeta 2'))

distancia = planeta1 - planeta2
print('LA DISTANCIA ES DE ', distancia)