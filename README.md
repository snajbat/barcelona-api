# My Barcelona API

Empiezo el proyecto usando pandas para revisar el formato de los datos y encontrar posibles errores. En el dataset no hay nulos, pero sí existen duplicados. Sin embargo, en este caso, no eliminamos los duplicados porque también aportan información.

Dado que no tengo interés en las variaciones en el tiempo de la población, voy a quedarme sólo con los datos del último año disponible. Ahora que la columna "Year" tiene un único valor, la elimino del dataframe porque ya no aporta ninguna información.

Creo una columna númerica cogiendo el primer número de cada intervalo de la columna "Age" para facilitar más adelante la representacióm de los datos.

Usando la API geocode.xyz, busco los valores de latitud y longitud de cada barrio existente en mi dataframe y añado una columna con cada uno.

Por último, llevo mis datos a Mongodb y agrego los documentos por barrio, edad y sexo, obteniendo la suma de la columna "Number". A partir de aquí, comienzo a crear mi API.