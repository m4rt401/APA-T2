"""
MARTA ENRICH GARCIA

Módulo de gestión de números primos

PRIMOS I DESCOMPON està canviat a llista

Exemples:

>>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)

>>> mcm(90, 14)
630

>>> mcd(924, 780)
12
"""

def esPrimo(numero):
    """
    Devuelve true si su argumento es primo, y False si no lo es.  
    """

    if numero < 2:
        return False
    for i in range(2, int(numero**0.5)+1):
        if numero % i == 0:
            return False
    return True                         

def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que su argumento.
    """

    return tuple([prova for prova in range(2, numero) if esPrimo(prova)])

def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.
    """
  
    llista = list()
    for prova in primos(numero):            #Mentre el valor prova damb tots els valors primers dens del rang establert (range(2, numero))
        while numero % prova == 0:          
            llista.append(prova)            
            numero = numero // prova        
    #return llista                           
    return tuple(llista)                   
    
def mcm(num1, num2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    """
    
    A = list(descompon(num1))             #S'obtenen els valors de a amb la funció descompon
    B = list(descompon(num2))             #S'obtenen els valors de b amb la funció descompon
    for x in A:                     #Per cada valor dins de la llista A
        if x in B:                  #Si aquest valor també està a la llista B
            B.remove(x)             #Eliminem els valors de b que es repeteixen en A
    A = A + B                       #Sumem les dos llistes (no es sumen els valors només s'afegeixen a la llista)
    mcm = 1                         #Creem una variable per el resultat final
    for x in A:                     #Per cada valor dins de la llista A
        mcm = mcm * x               #Multipliquem tots els valors que hi ha dins de la llista
    return mcm                      #Valor final

def mcd(num1, num2):
    """
    Devuelve el máximo común divisor de sus argumentos.
    """

    A = list(descompon(num1))             #S'obtenen els valors de a amb la funció descompon
    B = list(descompon(num2))             #S'obtenen els valors de b amb la funció descompon
    aux = list()                    #Creem una llista nova per poder guardar valors després
    for x in A:                     #Per cada valor de x dins de la llista A
        if x in B:                  #Si aquest valor també està a la llista B
            B.remove(x)             #Eliminem els valors de b que es repeteixen en A
            aux.append(x)           #Guardem el valor en aquesta llista per posterior fer el mcd
    mcd = 1                         #Creem una variable per el resultat final
    for x in aux:                   #Per cada valor dins de la llista A
        mcd = mcd * x               #Multipliquem tots els valors que hi ha dins de la llista

    return mcd                      #Valor final

 
import doctest
doctest.testmod()

    
