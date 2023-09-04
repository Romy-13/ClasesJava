# lista = Ariel , Liliana , Osvaldo
# Colecciones de Python

# Las listas en otros lenguajes se las conoce como arregos o vectores
nombres = ["Naty", "Osvaldo", "Romi" , "Lautaro"]
print(nombres)
# mostrar en el indice que se ecuentra el elemento en la lista
print(nombres[0])
print(nombres[2])
# muestra el último elemento de la lista
print(nombres[-1])

# recuperar un rango de nuestra lista
print(nombres[0:2])

# para ir del inicio de la lista al indice(sin incluirlo
print(nombres[ :3])

# desde el indice indicado hasta el final
print(nombres[1: ])

# Modificar un valor
nombres[1] = "Iris"
print(nombres)

# iterar nuestra lista
for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre)
else:
    print("se acaba los elementos de la lista")

# preguntamos cuantos elementos tiene
print(len(nombres))

# agregamos un elemento
nombres.append("Naira")
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)
print(nombres)

# incertar un elemento en un indice especifico
nombres.insert(1,"Fernando")
print(nombres)
nombres.insert(3,"Jazmín")
print(nombres)

# Eliminar un elemento de la lista
nombres.remove("Naty")
print(nombres)

# Eliminar el último elemento
nombres.pop()
print(nombres)

# Eliminar un indice especifico
del nombres[3] # delete (iliminar)
print(nombres)

# Eliminar todos os elementos de la lista
nombres.clear()
print(nombres)

# Definimos una tupla
cocina =("cuchara", "cuchillo", "tenedor")
print(len(cocina))

# Acceder a un elemnto, se realiza con corchetes
print(cocina[0])
# Mostrar de manera inversa
print(cocina[-1])

# Como acceder a un rango
print(cocina[0:2])

# Recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar, end=" ")# usamos end= para eliminar el salto de linea

cocina_lista= list(cocina)
cocina_lista[0]='plato'
cocina=tuple(cocina_lista)
print(cocina)



# Tipo Set:

planetas = {"Marte", "Júpiter", "Venus"}
print(len(planetas)) # con len(lengt) se utiliza para saber el largo o cantidad

# Revisar si algun elemento existe dentro de set
print("Júpiter" in planetas)

# Agregar un elemento
planetas.add("Tierra")
print(planetas)

# Eliminar elementos, puede arrojar una herror si el elemento no existe
planetas.remove("Júpiter")# Esta función ante un mal ingreso o inexistencia, noa arroja una error
print(planetas)
planetas.discard("Tierra")# Estafunción no nos representa ningún error, caso de un mal ingreso
print(planetas)

# Limpiar set o conjunto
planetas.clear()
print(planetas)

# Eliminar set o conjunto
del planetas
#print(planetas) # al eliminar nos muetra un error


# Diccionario:

#"Maradona" : 10 -Un diccionario esta compuesto por dos elementos
#dict(key,value)
diccionario = {
    'IDE': 'Integrated Development Environment',
    'POO': 'Programación Orientada  a Objetos',
    'SABD': 'Sistema de Administración de Datos'
}
# Verificar la cantidad de elementos de un diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave 'key'
print(diccionario['IDE'])

# otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificar elementos
diccionario['IDE'] = 'Entorno de desarrollo Integrado'

# Como recorrer los elementos
for termino in diccionario: #Recorremos mostrando solo las llaves
    print(termino)

# Necesitamos una función para reccorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) # Muestra solo las llaves

for valor in diccionario.values(): # Usamos una función para acceder al valor
    print(valor)

# Comprobar la existencia de algun elemento
print("IDE" in diccionario) # Devuelve u booleano

# Agregar u elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario

# Concatenar listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1+lista2 # concatenamos
print(lista3)

lista3.extend([7, 8, 9])# función para agregar varios elementos
print(lista3)

print(lista3.index(5))# función para ubicar en que indice esta el valor ingresado
# print(lista3.index(0)) esto daría un error por ser un elemento que no es parte de la lista

# Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) # esta función cuenta cuantos valores hay dentro de una lista

# Para poner al revés una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo susu elementos
lista3 = lista3 * 2
print(lista3)

# Métodos de ordenamiento
lista3.sort() # ordena los elementos ascendentemente
print(lista3)
lista3.sort(reverse=True) # ordena descendentemente
print(lista3)

tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola') # puede tener diferentes tipos de elementos
print(tupla)

print(4 in tupla) # acción booleana, su respuesta es de tipo booleana
# lo que podemos usar dentro de tuplas son: index, count, len
# en tuplas se puede convertir de tupla a lista y de lista a tupla