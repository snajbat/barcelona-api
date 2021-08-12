# My Barcelona API

Empiezo el proyecto usando pandas para revisar el formato de los datos y encontrar posibles errores. En el dataset no hay nulos, pero sí existen duplicados. Sin embargo, en este caso, no eliminamos los duplicados porque también aportan información.

Dado que no tengo interés en las variaciones en el tiempo de la población, voy a quedarme sólo con los datos del último año disponible. Ahora que la columna "Year" tiene un único valor (2017), la elimino del dataframe porque ya no aporta ninguna información.

Creo una columna númerica cogiendo el primer número de cada intervalo de la columna "Age" para facilitar más adelante la representacióm de los datos.

Usando la API geocode.xyz, busco los valores de latitud y longitud de cada barrio existente en mi dataframe y añado una columna con cada uno.

Por último, llevo mis datos a Mongodb y agrego los documentos por barrio, edad y sexo, obteniendo la suma de la columna "Number", y creo un campo location en mis documentos con la longitud y latitud  en formato geojson. A partir de aquí, comienzo a crear mi API.

## Manual de uso

La API permite hacer búsquedas en un función del barrio o distrito del que se requieran los datos. Usando el endpoint /neighborhood/\<neigh\> y sustituyendo *neigh* por el nombre del barrio o código (*ver códigos más abajo*), podemos obtener la información de la población de un barrio por edad quinquenal y sexo.
El endpoint /district/\<district\> tiene el mismo funcionamiento que el anterior, mostrando todos los documentos de la base de datos correspondientes a ese distrito de Barcelona.

Por otro lado, también podemos pasar como query *group* con tres posibles valores, *gender, age y total*, para mostrar la población por sexos, edades quinquenales o la población total del barrio o distrito, respectivamente.

#### Barrios

Los números que preceden al barrio son los códigos a usar en la API.

1. el Raval
2. el Barri Gòtic
3. la Barceloneta
4. Sant Pere, Santa Caterina i la Ribera
5. el Fort Pienc
6. la Sagrada Família
7. la Dreta de l'Eixample
8. l'Antiga Esquerra de l'Eixample
9. la Nova Esquerra de l'Eixample
10. Sant Antoni
11. el Poble Sec - Parc Montjuïc
12. la Marina del Prat Vermell - Zona Franca
13. la Marina de Port
14. la Font de la Guatlla
15. Hostafrancs
16. la Bordeta
17. Sants - Badal
18. Sants
19. les Corts
20. la Maternitat i Sant Ramon
21. Pedralbes
22. Vallvidrera, el Tibidabo i les Planes
23. Sarrià
24. les Tres Torres
25. Sant Gervasi - la Bonanova
26. Sant Gervasi - Galvany
27. el Putxet i el Farró
28. Vallcarca i els Penitents
29. el Coll
30. la Salut
31. la Vila de Gràcia
32. el Camp d'en Grassot i Gràcia Nova
33. el Baix Guinardó
34. Can Baró
35. el Guinardó
36. la Font d'en Fargues
37. el Carmel
38. la Teixonera
39. Sant Genís dels Agudells
40. Montbau
41. la Vall d'Hebron
42. la Clota
43. Horta
44. Vilapicina i la Torre Llobeta
45. Porta
46. el Turó de la Peira
47. Can Peguera
48. la Guineueta
49. Canyelles
50. les Roquetes
51. Verdun
52. la Prosperitat
53. la Trinitat Nova
54. Torre Baró
55. Ciutat Meridiana
56. Vallbona
57. la Trinitat Vellaç
58. Baró de Viver
59. el Bon Pastor
60. Sant Andreu
61. la Sagrera
62. el Congrés i els Indians
63. Navas
64. el Camp de l'Arpa del Clot
65. el Clot
66. el Parc i la Llacuna del Poblenou
67. la Vila Olímpica del Poblenou
68. el Poblenou
69. Diagonal Mar i el Front Marítim del Poblenou
70. el Besòs i el Maresme
71. Provençals del Poblenou
72. Sant Martí de Provençals
73. la Verneda i la Pau  

#### Distritos

1. Ciutat Vella
2. Eixample
3. Sants-Montjuïc
4. Les Corts
5. Sarrià-Sant Gervasi
6. Gràcia
7. Horta-Guinardó
8. Nou Barris
9. Sant Andreu
10. Sant Martí
