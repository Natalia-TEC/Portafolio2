#Portafolio 02


                                #Ejercicio 1
#Invertir los elementos de una lista.
"""
Nombre: invertiLista(lista)
Entrada: (lista) una lista de números enteros positivos.
Salida: la lista invertida.
Restircciones: el parámetro de entrada debe de ser una lista con números enteros
positivos. Si la lista está vacía devolver un cero.
"""

def invertirLista(lista):
    if(isinstance(lista, list)and (lista, int)):
        if(lista == []):
            return 0
        else:
            return invertirLista_aux(lista, [])

def invertirLista_aux(lista, invertida):
    if(lista == []):
        return invertida
    else:
        return invertirLista_aux(lista[:-1], invertida+ [lista[-1]])


                                #Ejercicio 2
#Determinar cuál es el número menor y mayor de una lista.
"""
Nombre: extremosLista(lista)
Entrada: (lista) una lista de números enteros positivos.
Salida: la lista con el número menor y el mayor de (lista)
Restircciones: el parámetro de entrada debe de ser una lista con números enteros
positivos. Si la lista está vacía devolver ºerrorº
"""

def extremosLista(lista):
    if(isinstance(lista, list)and (lista, int)):
        if(lista == []):
            return print("error")
        else:
            return extremosLista_aux(lista[1:], [], [], [])
def extremosLista_aux(lista, resultado, mayor, menor):
    if(lista == []):
        return resultado
    else:
        mayor = lista[0]
        menor = lista[-1]
        resultado = [lista[0]] + [lista[-1]]
        return extremosLista_aux(lista[1:], resultado, mayor, menor)

                                #Ejercicio 3
#Sacar dígitos de un número.
"""
Nombre: eliminarDigito(num, digito)
Entrada: (num) un número entero positivo, (digito) un número entero positivo
del 1 al 9.
Salida: un número sin el dígito repetido.
Restircciones: el parámetro de entrada debe de ser un número entero positivo. Si
el número es CERO debe de devolver un mensaje correspondiente al  ºerrorº.
"""

def eliminarDigito(num, digito):
    if(isinstance(num, int)and (num >= 0)and (isinstance(digito, int)and (digito >= 0)and (digito < 10))):
        if(num == 0):
            return print("Error, el parámetro no posee dígitos que puedan ser utiles.")
        else:
            return eliminarDigito_aux(num, digito, 0, 1)

def eliminarDigito_aux(num, digito, resultado, contador):
    if(num == 0):
        return resultado
    else:
        dig = (num % 10)
        if(dig == digito):
            return eliminarDigito_aux(num // 10, digito, resultado, contador)
        else:
            numero = dig * contador
            return eliminarDigito_aux(num// 10, digito, resultado + numero, contador * 10)
        
                                #Ejercicio 4
#Determinar subListas.
"""
Nombre: nivelesLista(lista)
Entrada: (lista) una lista que contenga sublistas.
Salida: Devolver de una lista de listas la cantidad de sublistas que lo contiene
Restircciones: el parámetro de entrada debe de ser una lista. La lista puede estar
vacía.
"""

def nivelesLista(lista):
    if(isinstance(lista, list)):
        return nivelesLista_aux(lista[1:], [])

def nivelesLista_aux(lista, resultado):
    if(lista == []):
        return resultado
    else:
        return nivelesLista_aux(lista[1:], resultado + [lista[-1]])
    
    
[]
