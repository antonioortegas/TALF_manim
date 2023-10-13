# SCRIPT

## 0. Introducción

Apartado 2.11, Cierre de los Tipos de Lenguajes. Definidas en el apartado anterior algunas operaciones sobre lenguajes, cabe preguntarse acerca de los lenguajes que generan estas operaciones. En este apartado se estudia el cierre de los tipos de lenguajes para dichas operaciones.

## 1. ¿Qué significa que un lenguaje está cerrado para una operación?

Recordemos que decimos que un conjunto está cerrado para una operación si el resultado de aplicar dicha operación a elementos del conjunto es siempre un elemento del mismo conjunto. Por ejemplo, el conjunto de los números naturales está cerrado para la suma (puesto que es el resultado de sumar dos números naturales es siempre un número natural), pero no está cerrado para la resta (puesto que el resultado de restar dos números naturales puede no ser un número natural).
En el caso de los lenguajes, decimos que un tipo de lenguaje está cerrado para una operación si el resultado de aplicar dicha operación a lenguajes de ese tipo es siempre un lenguaje del mismo tipo.

## 2. Representación gráfica de los lenguajes dentro de la jerarquía de Chomsky

La siguiente figura es una representación gráfica de los lenguajes dentro de la jerarquía de Chomsky. Aquí se encuentran los lenguajes ya clasificados en su capa correspondiente. El problema es el siguiente: Cuando realizamos una operación sobre lenguajes, estamos generando uno nuevo, pero ¿en qué capa se encuentra?

## 3. Operaciones como una caja negra

Bien, tratemos de realizar una operación y clasificar el lenguaje resultante.
Supongamos que tenemos un lenguaje Lineal y le aplicamos la operación "Complemento". Cogemos otros dos lenguajes y aplicamos la operación "Unión". Ambas operaciones dan como resultado nuevos lenguajes, pero ¿Cómo podemos clasificarlos?

## 4. De qué depende y por qué es difícil de determinar el tipo de lenguaje resultante

Habíamos visto que para clasificar gramáticas contamos con un mecanismo conclusivo, analizamos cada una de sus reglas de producción, y en función de su tipo podemos determinar el tipo de la gramática.
Sin embargo para clasificar un lenguaje en un tipo determinado la única opción que tenemos de momento es encontrar una gramática del mismo tipo que lo genere. Pero esto no es ni mucho menos trivial, y además no nos podemos asegurar de que no existe otra gramática de otro tipo que también lo genere.
Por esto de momento nos conformaremos con saber cuáles de los tipos de lenguajes son cerrados para qué operaciones y cuáles no. Veamos entonces la siguiente figura.

## 5. Explicación de la tabla e implicaciones de un Sí o un No

Esta tabla muestra cinco tipos de lenguajes, las operaciones que podemos realizar sobre los mismos y si están cerrados o no para cada una de ellas. Por ejemplo, podemos ver que los leguajes de contexto libre o de tipo 2 están cerrados para la concatenación, pero no para la intersección. Esto significa que si concatenamos dos lenguajes de tipo 2, el resultado siempre es un lenguaje de tipo 2, pero si intersectamos dos lenguajes de tipo 2, el resultado puede serlo o no.
Para decir que un conjunto no es cerrado para una operación en concreta, podemos ver un contraejemplo. Para ver que efectivamente los lenguajes de contexto libre o de tipo 2 no están cerrados para la intersección, nos basaremos en uno de los lenguajes para los que ya conocemos su tipo de un apartado anterior.
Sea L1 = { a^n b^n c^m | n,m >= 1 } y L2 = { a^n b^m c^m | n,m >= 1 }
Su intersección da como resultado el lenguaje L3 { a^n b^n c^n | n >= 1 }, que ya habíamos visto antes que no era de tipo 2.
Afirmar sin embargo que un tipo de leguaje es cerrado para una operación es mucho más costoso, puesto que como ya hemos dicho no tenemos ningún mecanismo de clasificación riguroso, y es este problema el que motiva el siguente bloque de contenidos, los Autómatas.

## 6. Inclusiones propias de los lenguajes

Podemos ver que sólo los lenguajes Regulares y los Sensibles al Contexto son cerrados para todas las operaciones descritas.
Los lenguajes Lineales no son cerrados para la Intersección, el Complemento, Concatenación, Potencia, Cierre o el Cierre estricto.
Los lenguajes de Contexto libre no son cerrados para la Intersección ni el complemento.
Y los lenguajes con Estrucutra de frase no son cerrados para el Complemento. Esto significa que existen Lenguajes Representables (puesto que los podemos representar como complemento de un Lenguaje de tipo 0) que no son de tipo 0.
Teniendo en cuenta lo visto ya anteriormente, tenemos por lo tanto las siguientes inclusiones propias de los lenguajes:
Los Lenguajes Finitos están incluidos en los Regulares, los Regulares en los Lineales, los Lineales en los de Contexto Libre, los de Contexto Libre en los Sensibles al Contexto y los Sensibles al Contexto en los de Estructura de Frase. Como acabamos de ver, los Lenguajes con Estructura de Frase están incluidos en los Representables, y como ya sabíamos, los Representables en el conjunto de todos los lenguajes posibles sobre un alfabeto.
Aquí destacamos una frontera importante, la de la cardinalidad. Habíamos demostrado en un apartado enterior que el cardinal del conjunto de todos los posibles Lenguajes sobre un alfabeto es Alef-1, y que el cardinal del conjunto de los Lenguajes Representables es Alef-0. Por lo tanto, y según estas inclusiones, el cardinal de todos los conjuntos de Lenguajes que veíamos en la tabla es Alef-0.
