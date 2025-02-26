#Funcion para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit (celsius):
    return(celsius * 9/5) + 32

#Funcion para convertir Celsius a Kelvin
def celsius_a_kelvin (celsius):
    return celsius + 273.15

#Funcion para convertir Fahrenheit a Celsius
def fahrenheit_a_celsius (fahrenheit):
    return (fahrenheit - 32) * 5/9

#Funcion para convertir Fahrenheit a Kelvin
def fahrenheit_a_kelvin (fahrenheit):
    return (fahrenheit -32) * 5/9 + 273.15

#Funcion para convertir Kelvin a celsius
def kelvin_a_celsius (kelvin):
    return kelvin - 273.15

#Funcion para convertir kelvin a Fahrenheit
def kelvin_a_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

#Menu de opciones
print("Bienvenido al conversor de temperaturas")
print("Elige una opcion: ")
print("1. Convertir de Celsius a Fahrenheit")
print("2. Convertir de Celsius a Kelvin")
print("3. Convertir de Fahrenheit a Celsius")
print("4. Convertir de Fahrenheit a Kelvin")
print("5. Convertir de Kelvin a Celsius")
print("6. Convertir de Kelvin a Fahrenheit")

#Validacion de entrada
try:
    opcion = int(input("Ingresa el numero de la opcion que deseas: "))
    
    if opcion == 1:
        celsius = float(input("Ingresa la temperatura en grados Celsius: "))
        fahrenheit = celsius_a_fahrenheit(celsius)
        print(celsius, "grados Celsius son:", fahrenheit, "grados Fahrenheit")
        
    elif opcion == 2:
        celsius = float(input("Ingresa la temperatura en grados Celsius: "))
        kelvin = celsius_a_kelvin(celsius)
        print(celsius, "grados Celsius son", kelvin, "grados Kelvin.")
        
    elif opcion == 3:
        fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))
        celsius = fahrenheit_a_celsius(fahrenheit)
        print(fahrenheit, "grados Fahrenheit son", celsius, "grados Celsius.")
    
    elif opcion == 4:
        fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))
        kelvin = fahrenheit_a_kelvin(fahrenheit)
        print(fahrenheit, "grados Fahrenheit son", kelvin, "grados Kelvin.")
        
    elif opcion == 5:
        kelvin = float(input("Ingresa la temperatura en grados Kelvin: "))
        celsius = kelvin_a_celsius(kelvin)
        print(kelvin, "grados Kelvin son", celsius, "grados Celsius.")
    
    elif opcion == 6:
        kelvin = float(input("Ingresa la temperatura en grados Kelvin"))
        fahrenheit = kelvin_a_fahrenheit(kelvin)
        print(kelvin, "grados Kelvin son", fahrenheit, "grados Fahrenheit.")
        
    else:
        print("Opcion no valida. Por favor, elige una opcion entre el 1 y el 6.")

except ValueError:
    print("Entrada no valida. Por favor, ingresa un numero valido.")
    
