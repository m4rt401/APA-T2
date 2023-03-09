# Segunda tarea de APA 2023: Manejo de números primos

## Nom i cognoms: Marta Enrich Garcia

## Fichero `primos.py`

- El alumno debe escribir el fichero `primos.py` que incorporará distintas funciones relacionadas con el manejo
  de los números primos.

- El fichero debe incluir una cadena de documentación que incluirá el nombre del alumno y los tests unitarios
  de las funciones incluidas.

- Cada función deberá incluir su propia cadena de documentación que indicará el cometido de la función, los
  argumentos de la misma y la salida proporcionada.

- Se valorará lo pythónico de la solución; en concreto, su claridad y sencillez, y el uso de los estándares marcados
  por PEP-8. También se valorará su eficiencia computacional.

### Determinación de la *primalidad* y descomposición de un número en factores primos

Incluya en el fichero `primos.py` las tres funciones siguientes:

- `esPrimo(numero)`   Devuelve `True` si su argumento es primo, y `False` si no lo es.
- `primos(numero)`    Devuelve una **tupla** con todos los números primos menores que su argumento.
- `descompon(numero)` Devuelve una **tupla** con la descomposición en factores primos de su argumento.

### Obtención del mínimo común múltiplo y el máximo común divisor

Usando las tres funciones del apartado anterior (y cualquier otra que considere conveniente añadir), escriba otras
dos que calculen el máximo común divisor y el mínimo común múltiplo de sus argumentos:

- `mcm(numero1, numero2)`:  Devuelve el mínimo común múltiplo de sus argumentos.
- `mcd(numero1, numero2)`:  Devuelve el máximo común divisor de sus argumentos.

Estas dos funciones deben cumplir las condiciones siguientes:

- Aunque se trate de una solución sub-óptima, en ambos casos deberá partirse de la descomposición en factores
  primos de los argumentos usando las funciones del apartado anterior.

- Aunque también sea sub-óptimo desde el punto de vista de la programación, ninguna de las dos funciones puede
  depender de la otra; cada una debe programarse por separado.

### Tests unitarios

La cadena de documentación del fichero debe incluir los tests unitarios de las cinco funciones. En concreto, deberán
comprobarse las siguientes condiciones:

- `esPrimo(numero)`:  Al ejecutar `[ numero for numero in range(2, 50) if esPrimo(numero) ]`, la salida debe ser
                      `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]`.
- `primos(numeor)`: Al ejecutar `primos(50)`, la salida debe ser `(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)`.
- `descompon(numero)`: Al ejecutar `descompon(36 * 175 * 143)`, la salida debe ser `(2, 2, 3, 3, 5, 5, 7, 11, 13)`.
- `mcm(num1, num2)`: Al ejecutar `mcm(90, 14)`, la salida debe ser `630`.
- `mcd(num1, num2)`: Al ejecutar `mcd(924, 780)`, la salida debe ser `12`.

### Entrega

#### Ejecución de los tests unitarios

Inserte a continuación una captura de pantalla que muestre el resultado de ejecutar el fichero `primos.py` con la opción
*verbosa*, de manera que se muestre el resultado de la ejecución de los tests unitarios.

<img src="Prova_Comp.PNG" width="480" align="center">

#### Código desarrollado

Inserte a continuación el contenido del fichero `primos.py` usando los comandos necesarios para que se realice el
realce sintáctico en Python del mismo.

```
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
    for prova in primos(numero):
        while numero % prova == 0:          
            llista.append(prova)            
            numero = numero // prova        
    #return llista                           
    return tuple(llista)                   
    
def mcm(num1, num2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    """
    
    lista=list()                    #Es crea una llista
    lista.append(num2)              #S'incorpora un valor qualsevol
    a = descompon(num1)             #S'obtenen els valors de a amb la funció descompon
    b = descompon(num2)             #S'obtenen els valors de b amb la funció descompon
    A = list()                      #Creem una llista
    B = list()                      #Creem una llista
    for x in a:                     #Per cada valor de A en la posició x
        A.append(x)                 #Guardem el valor en una llista
    for x in b:                     #Per cada valor de B en la posició x
        B.append(x)                 #Guardem el valor en una llista

    while len(lista)>0:             #Iniciem un bucle per fer la comparació
        lista.pop()                 #Eliminem el valor que em posat a la llista per fer el bucle un cop
        for x in A:                 #Per cada valor dins de la llista A
            if x in B:              #Si aquest valor també està a la llista B
                B.remove(x)         #Eliminem els valors de b que es repeteixen en A
        A = A + B                   #Sumem les dos llistes (no es sumen els valors només s'afegeixen a la llista)
    mcm = 1                         #Creem una variable per el resultat final
    for x in A:                     #Per cada valor dins de la llista A
        mcm = mcm * x               #Multipliquem tots els valors que hi ha dins de la llista
    return mcm                      #Valor final

def mcd(num1, num2):
    """
    Devuelve el máximo común divisor de sus argumentos.
    """
    
    lista = list()                  #Es crea una llista
    lista.append(num2)              #S'incorpora un valor qualsevol
    a = descompon(num1)             #S'obtenen els valors de a amb la funció descompon
    b = descompon(num2)             #S'obtenen els valors de b amb la funció descompon
    A = list()                      #Creem una llista
    B = list()                      #Creem una llista
    for x in a:                     #Per cada valor de A en la posició x
        A.append(x)                 #Guardem el valor en una llista
    for x in b:                     #Per cada valor de B en la posició x
        B.append(x)                 #Guardem el valor en una llista

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
```

#### Subida del resultado al repositorio GitHub ¿y *pull-request*?

El fichero `primos.py`, la imagen con la ejecución de los tests unitarios y este mismo fichero, `README.md`, deberán
subirse al repositorio GitHub mediante la orden `git push`. Si los profesores de la asignatura consiguen montar el
sistema a tiempo, la entrega se formalizará realizando un *pull-request* al propietario del repositorio original.

El fichero `README.md` deberá respetar las reglas de los ficheros Markdown y visualizarse correctamente en el repositorio,
incluyendo la imagen con la ejecución de los tests unitarios y el realce sintáctico del código fuente insertado.
