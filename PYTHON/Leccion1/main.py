miVariable = 3
print(miVariable)
miVariable = "Hola a todos los estudiantes de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
# Las literales se escriben con x344, la variable y = x088, la variable z = x408
print(id(y))
print(id(z))

a = False
print(type(a))
# Tips int, float, bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de cadenas(String)
miGrupoFavorito = "Divididos"
caracteristicas = "La mejor banda de rock"
print("Mi grupo favorito es:" + miGrupoFavorito, caracteristicas)

numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2))

# Tipos de Boleanos(bool)
miBoleano = 1 > 2
print(miBoleano)

if miBoleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar la entrada del usuario
# función input
resultado = input("digite un numero: ")  # regresa un dato tipo string
print(resultado)

# Conversión de la entrada de datos
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)
