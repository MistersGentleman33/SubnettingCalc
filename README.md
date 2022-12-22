# Calculadora de IP
##### HECHA POR:
- Caballero Perdomo Axel Lennyn
- Hernandez Garcia Luis Miguel

------------


------------



#### INTRODUCCION
¿Por qué realizar un Subneteo?

Cuando trabajamos con una red pequeña no encontramos muchos problemas para configurar el rango de direcciones IPv4 para conseguir un rendimiento óptimo. Pero a medida que se van agregando Host a la red, el desempeño empieza a verse afectado. Esto puede ser corregido, en parte, segmentando la red con switches, reduciendo los Dominios de colisión enviando las tramas solo al segmento correcto.

Subneteando la red tendremos, en su conjunto, una sola IP address divida en varias subredes más pequeñas perfectamente diferenciadas, consiguiendo un mayor control y reduciendo el congestionamiento por los broadcasts.

##### Subred

Es la agrupación física o lógica de dispositivos de red que conforman a una sección de un sistema autónomo o como tal puede ser un sistema autónomo.

##### Mascara de red

Denominado también Prefijo de red extendida, es el número que acompaña a una dirección IP, indicando los bits totales ocupados para la parte de red, que deben ser comunes para todos los clientes de una Red IP.

##### Subneteo IP

La función del Subneteo o Subnetting es dividir una red IP física en subredes lógicas para que cada una de estas trabaje a nivel envío y recepción de paquetes como una red individual, aunque todas pertenezcan a la misma red física y al mismo dominio.

![](https://upload.wikimedia.org/wikipedia/commons/7/7d/Redes_IP.png)

## ¿Cómo lo hace?
Empezemos desde el main donde podemos observar una serie de elementos de control donde le paseremos como parametro la IP y la subred mediante consola como argumento.

![](https://github.com/MistersGentleman33/SubnettingCalc/blob/main/src/img1.PNG?raw=true)

Esto es para que podamos usar el programa como si fuera un comando. Por ejemplo el comando "ping" que si lo digitamos por consola "ping -h" nos apareceran sus argumentos, para eso ocupamos la libreria sys.

Despues tenemos filtros para que si el usuario se equivoca en cualquier argumento le indique con un mensaje como se debe utilizar el programa y en donde está el error.
Posteriormente el argumento de la ip pasa por un proceso de separacion ya que el argumento llega de este tipo:
###### "192.168.1.1"

![](https://github.com/MistersGentleman33/SubnettingCalc/blob/main/src/img2.PNG?raw=true)

Con la funcion split() separamos por el token "." la cadena y la guardamos en una lista para que podamos manipular mas facilmente los datos, ahora nuestra ip luce algo asi:
###### [192, 168, 1, 1]
Posteriormente pasamos como argumento a la funcion "found_next_mask()"la ip y la submascara de subred que el usuario ingreso como segundo argumento.

![](https://github.com/MistersGentleman33/SubnettingCalc/blob/main/src/img3.PNG?raw=true)

La funcion encontrara la nueva mascara en base a la subred que le pasamos como argumento.
Para la creacion de la nueva mascara divido en octetos el numero se subred y de esta forma se en todo momento la cantidad de 1 que debo agregar. Mediante un while itero la cantidad de veces necesaria para rellenar de 1's y 0's.
Por ejemplo si la ip es 192.168.0.0 y la mascara de red es 27.
En el while se validará si 27 es mayor o igual a 8, esto para separar la mascara en octetos y si es mayor se agregaran ocho unos, a 27 le restaremos 8 y el ciclo volvera a empezar pero con 19, de esta forma se construira la mascara, cuando llegue al numero minimo que es 3, simplente agregara tres unos y agregara cinco ceros que corresponde a la diferencia de 8 menos 3.
Asi es como construimos la nueva mascara y dicha mascara se retorna como lista.
Aqui mismo se calcula la cantidad de redes posibles que se generaran con la nueva mascara, simplemente restando la mascara nueva menos la mascara por defecto, en nuestro ejemplo sería 27 - 24 y nos daria 3.  Si elevamos 2^3 nos da 8 que es la cantidad de redes para esta mascara de red.

Esto tres valores los retornamos.

![](https://github.com/MistersGentleman33/SubnettingCalc/blob/main/src/img4.PNG?raw=true)

Dependiendo si la IP es clase A, B o C entrará a su propio algoritmo de subneteo. Como se puede ver en la parte de los IFS donde se evalua la clase de la IP y en base a eso entra a una funcion con el nombre de la clase que contiene el algoritmo de subneteo para esa clase.

En todas las clases es casi lo mismo, solo que el algoritmo se implementa en la seccion de IP que corresponde dependiendo de la mascara.
Mediante la formula 256 - subnet = paso de red. Obtenemos el salto entre redes para las nuevas redes, en nuestro caso sería 256 -224 = 32 tomando en cuenta la ip 192.168.0.1 nuestras 8 redes tendran un salto de red de 32, para calcular el Host minimo sabemos que es 1 y el Host maximo es el salto de red - 2, y la direccion de broadcast es el salto de red -1. De esta forma es como se calculan las subredes y es el mismo algoritmo para cada clase de red, solo cambia el octeto en el que se manipulan los datos.
Y para la cantidad de host que permite conectar se calcula mediante la formula 2^m - 2 donde m es la cantidad de 0's que contiene la nueva mascara de red.


------------


###### Para la clase A

![](https://github.com/MistersGentleman33/SubnettingCalc/blob/main/src/img5.PNG?raw=true)

------------



###### Para la clase B

![](https://github.com/MistersGentleman33/SubnettingCalc/blob/main/src/Captura5.PNG?raw=true)

------------


###### Para la clase C

![](https://github.com/MistersGentleman33/SubnettingCalc/blob/main/src/Captura6.PNG?raw=true)

------------
## USO
Para usar la calculadora solo hay que ingresar por consola desde el path donde se encuentra el archivo .py lo siguiente:

###### SubnettingCalc.py IPADDRESS SUBNET

Ejemplo:

###### SubnettingCalc.py 192.168.1.0 27


## CONCLUSION
Con la creación de este proyecto pudimos reforzar los conocimientos y gracias a eso nace con el propósito de difundir información veraz y de calidad sobre las técnicas tradicionales y modernas del cálculo de redes empleando distintos algoritmos como los que aparecen en la calculadora IP.
Con la siguiente calculadora de subnetting y a partir de la dirección IP que pongamos en el campo y la subnet mask, podremos obtener el broadcast, la dirección de red, la wildcard mask y  el host range, además, podemos pasar a una nueva supernet si cambiamos la netmask consiguiendo de esta manera generar nuevas subnets (subredes ip).


## BIBLIOGRAFIA
- https://www.udb.edu.sv/udb_files/recursos_guias/informatica-tecnologico/redes-de-comunicacion/2020/i/guia-6.pdf

- https://www.geeksforgeeks.org/
