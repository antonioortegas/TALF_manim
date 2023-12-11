# Recursiva implica WHILE-Computable

El Teorema de Equivalencia nos dice que todos los modelos de cómputo que históricamente se han propuesto son equivalentes, incluidos por supuesto los tres que hemos visto en el bloque anterior. Es decir, que todos ellos son diferentes formas de representar lo mismo. Todas computan las mismas funciones.
Para probar este Teorema, deberíamos establecer una serie de inclusiones circulares entre dichos modelos de cómputo, ya que de esta forma podríamos demostrar la equivalencia entre todos ellos.
Sin embargo, nos limitaremos a demostrar la inclusión más sencilla, y que podemos realizar con los conocimientos que tenemos hasta ahora. No obtante, quede claro que la inclusión inversa también es cierta, y cualquier otra inclusión entre modelos de cómputo válidos también lo es.

Como queremos demostrar que todas las funciones recursivas son WHILE-computables, debemos demostrar que todo programa recursivo puede ser expresado como un programa WHILE. Para ello, deberemos demostrar que el conjunto de funciones iniciales es computable, así como cualquier función obtenida a partir de ellas mediante composición, recursión primitiva y minimización no acotada.

Comencemos por las funciones iniciales, que son casi triviales.

La función cero. Queremos una función que dada 0 argumentos de entrada, siempre devuelva 0. Esto es muy sencillo. Sabemos que tenemos 0 variables de entrada, y que necesitamos una variable de salida, que será por lo tanto la variable auxiliar Xsub1. Como siempre queremos que devuelva 0, podemos escribir el siguiente programa, que simplemente asigna 0 a Xsub1 y termina.

Vamos con el sucesor, igualmente simple. Queremos una función que dada una variable de entrada, devuelva su sucesor. Sabemos que tenemos 1 variable de entrada que sera Xsub1, y que necesitamos una variable de salida, que será la misma Xsub1. Como queremos que devuelva el sucesor de la variable de entrada, podemos escribir el siguiente programa, que simplemente asigna a Xsub1 el valor de Xsub1 + 1 y termina.

Por últimos el conjunto de funciones proyección. Queremos una función que dada K variables de entrada, devuelva la i-ésima. Sabemos que tenemos K variables de entrada, bastará con asignar a la variable de salida Xsub1 el valor de la variable de entrada Xsubi, sin necesidad de variables auxiliares. Esto es, el siguiente programa.
Esto nos da un conjunto de programas WHILE equivalente al de las proyecciones.

Por lo tanto, hemos demostrado que el conjunto de funciones iniciales es computable.

Pasemos pues a las funciones derivadas de las mismas.

Primero, la composición. De forma general, supongamos que tenemos funciones f de N k en N, g de N m en N y m funciones h sub i de N k en N, todas computables según veíamos en el bloque anterior para la composición.
Simplemente, podemos escribir el siguiente programa, que, con k variables de entrada, y k + m variables en total, asigna una por una a cada variable auxiliar Xsubi el valor de la función h sub i de las variables de entrada, y finalmente asigna a la variable de salida Xsub1 el valor de la función g de las variables auxiliares.
Después, asigna a la variable de salida Xsub1 el valor de la función g con las variables auxiliares como argumentos, y termina.
Vemos que la función que calcula es f.

Para la recursión primitiva, supongamos que tenemos las funciones f, g y h que definiamos en el apartado de la recursión primitiva del bloque anterior, todas computables.
Podemos entonces escribir el siguiente programa, con k + 1 variables de entrada, y k + 3 variables en total. Primero usamos una de las dos variables auxiliares para calcular el valor de la función g de las variables de entrada desde la 1 hasta la k (nuestro "caso base" en la recursión). Vamos entonces en cada iteración calculando el valor de h, y sumándo uno a X sub k + 3. Una vez iterado las veces que dictaba X sub k + 1, asignamos a la variable de salida X sub 1 el valor de la X sub k + 2, que contenía nuestro resultado.

Finalmente, la minimización no acotada. Supongamos que tenemos las funciones que deciamos de nuevo en el bloque anterior en el apartado de la minimización no acotada, todas computables, f es mi de g, y g de N k + 1 en N.
Podemos expresarla mediante el siguinte macroprograma.
Tiene k entradas y una variable auxiliar. La condición del bucle es que la función g de las variables de entrada y la variable auxiliar sea distinta de 0. En cada iteración, simplemente incrementamos la variable auxiliar en 1 y volvemos a iterar. Una vez que la condición del bucle no se cumple, asignamos a la variable de salida X sub 1 el valor de la variable auxiliar, que contendrá el número de iteraciones que hemos realizado, o lo que es lo mismo, el valor mínimo del conjunto A que veíamos en la definición de la minimización no acotada. Vemos ahora fácilmente la razón de que la minimización no acotada pueda diverger (o no terminar), puesto que si la función g de las variables de entrada y la variable auxiliar nunca es 0, el bucle nunca terminará.

Con esto, hemos demostrado que todas las funciones recursivas son WHILE-computables, y por lo tanto, que el conjunto de funciones recursivas es un subconjunto del conjunto de funciones WHILE-computables. Recordemos que aunque no vamos a entrar en detalles, la implicación inversa también es cierta, y por lo tanto, ambos conjuntos son iguales, y ocurre lo mismo con el conjunto de funciones que podemos computar con una máquina de Turing, o un modelo de cómputo cualquiera.
