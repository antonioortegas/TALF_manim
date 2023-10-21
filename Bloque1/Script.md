# SCRIPT

## 0. Introducción

Apartado 2.11, Cierre de los Tipos de Lenguajes. Definidas en el apartado anterior algunas operaciones sobre lenguajes, cabe preguntarse de que tipo son los lenguajes que generan estas operaciones. En este apartado estudiaremos por lo tanto si dichas operaciones sobre lenguajes son cerradas o no dependiendo del tipo de lenguaje sobre el que se realicen.

## 1. ¿Qué significa que un tipo de lenguaje está cerrado para una operación?

Pero, ¿Qué significa que un tipo de lenguaje esté cerrado para una operación en concreto? Recordemos que decimos que un conjunto está cerrado para una operación si el resultado de aplicar dicha operación a elementos del conjunto es siempre un elemento del mismo conjunto.

Supongamos por ejemplo que tenemos el conjunto de los naturales. Este conjunto está formado por los número 0, 1, 2, 3, 4, ... Bien, apliquemos entonces la operación suma sobre dos elementos cualesquiera de este conjunto. Por ejemplo, 1 + 3 da como resultado 4. Ahora, para saber si el 4 pertenece al conjunto, debemos clasificarlo como un número natural. Comprobamos que efectivamente lo es, por lo tanto pertenece al conjunto original. Como podemos hacer esto para cualquier par de números naturales, podemos afirmar que el conjunto de los naturales está cerrado para la operación suma.

Veamos sin embargo ahora la operación resta. si a 1 restamos 3, obtenemos el número -2. Al clasificarlo, vemos que no es un número natural, por lo que no pertenece al conjunto original de Naturales. Por lo tanto, el conjunto de los naturales no está cerrado para la resta.

Traslademos ahora este concepto a los lenguajes.

## 2. Representación gráfica de los lenguajes dentro de la jerarquía de Chomsky

La siguiente figura es una representación gráfica de los lenguajes dentro de la jerarquía de Chomsky. Aquí se encuentran los lenguajes ya clasificados en su capa correspondiente. L0 o con Estructura de Frase, L1 o Sensibles al contexto, L2 o Contexto Libre, Lenguajes Lineales, y L3 o Regulares.

En el caso de los lenguajes, decimos que un tipo de lenguaje está cerrado para una operación si el resultado de aplicar dicha operación a lenguajes de ese tipo es siempre un lenguaje del mismo tipo.

## 3. De qué depende y por qué es difícil de determinar el tipo de lenguaje resultante

Intentemos hacer el procedimiento anterior. Necesitaremos una operación y una forma de clasificar los lenguajes resultantes. Como operación podemos usar de ejemplo la intersección, pero, ¿Cómo clasificamos los lenguajes? Si operamos sobre dos lenguajes Lineales, L1 y L2, y obtenemos un lenguaje L3, ¿Cómo podemos saber si L3 es Lineal?

Para clasificar una gramática recordemos que tenemos un mecanismo conclusivo: analizar cada una de sus reglas de producción y en función de su tipo podemos determinar el tipo de la gramática. Pero para clasificar un lenguaje la única opción que tenemos de momento es encontrar una gramática del mismo tipo que lo genere. Pero esto no es ni mucho menos trivial, y además no nos podemos asegurar de que no existe otra gramática de otro tipo que también lo genere que no se nos ha ocurrido.

Por ello, en este apartado buscamos ese mecanismo que nos diga si el lenguaje es o no del mismo tipo, es decir, si pertenece o no al conjunto de origen. Para ello, nos basaremos en la siguiente tabla, que hace las veces de nuestro método de clasificación.

## 4. Explicación de la tabla e implicaciones de un Sí o un No

Esta tabla muestra cinco tipos de lenguajes, las operaciones que podemos realizar sobre los mismos y si están cerrados o no para cada una de ellas. Por ejemplo, podemos ver que los lenguajes de contexto libre o de tipo 2 están cerrados para la concatenación, pero no para la intersección. Esto significa que si concatenamos dos lenguajes de tipo 2, el resultado siempre es un lenguaje de tipo 2, pero si intersectamos dos lenguajes de tipo 2, el resultado puede serlo o no. No podemos asegurarlo.

Para decir que un conjunto no es cerrado para una operación en concreta, podemos ver un contraejemplo, como en el caso de la resta de Naturales. Para ver que efectivamente los lenguajes de contexto libre o de tipo 2 no están cerrados para la intersección, nos basaremos en uno de los lenguajes para los que ya conocemos su tipo de un apartado anterior.

Sea L1 = { a^n b^n c^m | n,m >= 0 } y L2 = { a^n b^m c^m | n,m >= 0 }
Su intersección da como resultado el lenguaje L3 { a^n b^n c^n | n >= 0 }, que ya habíamos visto antes que no era de tipo 2.

Afirmar sin embargo que un tipo de leguaje es cerrado para una operación es mucho más costoso, puesto que como ya hemos dicho no tenemos ningún mecanismo de clasificación riguroso, y es este problema el que motiva los siguientes bloques de contenidos.

A modo de resumen:

- Podemos ver que sólo los lenguajes Regulares y los Sensibles al Contexto son cerrados para todas las operaciones descritas.

- Los lenguajes Lineales no son cerrados para la Intersección, el Complemento, Concatenación, Potencia, Cierre o el Cierre estricto.

- Los lenguajes de Contexto libre no son cerrados para la Intersección ni el complemento.

- Y los lenguajes con Estrucutra de frase no son cerrados para el Complemento. Esto significa que existen Lenguajes Representables (puesto que los podemos representar como complemento de un Lenguaje de tipo 0) que no son de tipo 0.

## 5. Inclusiones propias de los lenguajes

Teniendo en cuenta lo visto ya anteriormente, tenemos por lo tanto las siguientes inclusiones propias de los lenguajes:

Los Lenguajes Finitos están incluidos en los Regulares, los Regulares en los Lineales, los Lineales en los de Contexto Libre, los de Contexto Libre en los Sensibles al Contexto y los Sensibles al Contexto en los de Estructura de Frase. Como acabamos de ver, los Lenguajes con Estructura de Frase están incluidos en los Representables, y como ya sabíamos, los Representables en el conjunto de todos los lenguajes posibles sobre un alfabeto.

Aquí destacamos una frontera importante, la de la cardinalidad. Habíamos demostrado en un apartado enterior que el cardinal del conjunto de todos los posibles Lenguajes sobre un alfabeto es Alef-1, y que el cardinal del conjunto de los Lenguajes Representables es Alef-0. Por lo tanto, y según estas inclusiones, el cardinal de todos los conjuntos de Lenguajes que veíamos en la tabla es Alef-0.
