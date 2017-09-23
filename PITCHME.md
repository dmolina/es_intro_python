## Introducción a Python para Inteligencia de Negocio

--- 

## ¿Por qué Python?

Python es un lenguaje muy usado en *Análisis de Datos* e *Inteligencia de Negocio*.  

- Lenguaje fácil de aprender. 

- Muy alto nivel (manejo de datos).

- Buenas herramientas de visualización.

- Librerías fáciles de **Machine Learning**. 

- Fácil de integrar con otras librerías/entornos.

---

# Lenguaje fácil de aprender

## Se diseño para ser sencillo. 

+++

## Hello World

```
print("Hello, World")
```

- No requiere ";" tras cada sentencia. 

- No requiere definir clase o main, sólo código.

+++ 

## tabulación, no llaves 

```
sumcars = 0
sumwords = 0

for word in ['hola', 'a', 'todos']:
    print("Frase: ", word)
    sumcars += len(word)
    sumwords += 1
    
print("Se han mostrado ", sumwords, " palabras y ", sumwords, " caracteres")
```

@[1-4,9](código al primer nivel)
@[4-7](Identifica el cuerpo del for/if por la tabulación)


+++

## Condiciones

```
if a < 0:
   print("a must be positive")
elif a > 10:
   print("a is too large")
else: 
   print("Perfect!")
```

@[1-2]
@[1-2,5-6]
@[1-4]

## Formato

- Las condiciones terminan en ":".
- *elif* implica *else if*. 
- La tabulación indica el cuerpo.

---



# Uso científico

![stack](stack.jpg)

+++

## Librerías científicas

![scikit-learn](scikit-learn.png)
![numpy](numpy.jpg)
![pandas](pandas.png)

+++

## Numpy

- Permite trabajar con vectores de reales. 

```
>>> import numpy as np
>>> a = np.arange(15).reshape(3, 5)
>>> a
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
>>> a.shape
(3, 5)
>>> a.ndim
2
```

+++

## Numpy:  Expresiones

```
>>> a = np.array( [20,30,40,50] )
>>> b = np.arange( 4 )
>>> b
array([0, 1, 2, 3])
>>> c = a-b
>>> c
array([20, 29, 38, 47])
>>> b**2
array([0, 1, 4, 9])
>>> 10*np.sin(a)
array([ 9.12945251, -9.88031624,  7.4511316 , -2.62374854])
>>> a<35
array([ True, True, False, False], dtype=bool)
```

--- 

