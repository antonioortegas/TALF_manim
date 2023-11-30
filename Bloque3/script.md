# Apartado 8.5 Algunas consideraciones sobre las Maquinas de Turing

Supongamos que tenemos una maquina de Turing como la que hemos estado viendo hasta el momento. Es decir, tenemos una
cinta infinita, una cabeza lectora, que apunta a una de sus celdas, y nuestra maquina, que posee un conjunto de estados, funciones de transicion, etc.

Vamos a destacar entonces que en este modelo, al numerar la cinta para poder operar, no nos importa la posicion del cuadrado numero 0, ya que podemos
definir una nueva maquina, cinta, etc, que sea equivalente a la anterior, pero que tenga el cuadrado 0 en la posicion que queramos. Las maquinas de Turing
tendran el mismo funcionamiento.

Por otro lado, tampoco es importante el simbolo o alfabeto que usemos, ya que podemos definir una maquina equivalente que use el alfabeto que venimos usando hasta ahora. Por ejemplo,
si tenemos una maquina que usa el símbolo "@" en lugar de "|" , podemos simplemente usar el nuevo simbolo en lugar del anterior en nuestra maquina.

Si queremos utilizar mas de un simbolo, podemos hacerlo traduciendo cada simbolo a una secuencia de simbolos de nuestro alfabeto. Esto ya lo hemos visto apartados anteriores,
donde haciamos corresponder cada numero natural con una secuencia de simbolos de nuestro alfabeto, en concreto, n+1 símbolos.
Si queremos usar otros símbolos, basta con definir estas equivalencias o traducciones.

En estos casos, obviamente la maquina de Turing equivalente sera mas compleja y tendra mas estados, ya que tendra que realizar mas operaciones y pasos para traducir los simbolos,
pero el funcionamiento sera el mismo.

Destacamos tambien el hecho de que aunque las maquinas de turing son finitas por definicion, podemos definir maquinas de turing que tengan realicen procesos infinitos no
periodicos, es decir, que no se repitan. Por ejemplo, podemos definir una maquina de Turing que escriba en la cinta los numeros naturales desde el 0, con nuestra codificacion
de numeros naturales. Esta maquina no se detendra nunca, ya que siempre escribira un numero natural mayor que el anterior, y ademas no se repite una configuracion.

Con todo lo que hemos visto, podemos ver que, enseguida, al intentar confeccionar una maquina de Turing que realice una tarea minimamente compleja, nos encontraremos con
una maquina de Turing con un numero de estados muy elevado, y que sera muy dificil de entender y de manejar. Por ello, es habitual utilizar los llamados "diagramas de maquinas de Turing",
que son una forma de construir maquinas de Turing a partir de maquinas de Turing mas sencillas, que realizan tareas mas simples.
Este es un ejemplo sencillo, que utiliza maquinas de turing simples para sumar uno a un numero binario.

Con esto, queda definido el primer modelo de cómputo de los 3 que veremos en este bloque.
