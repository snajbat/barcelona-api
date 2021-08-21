# My Barcelona Population API

La API devuelve los datos de la población de Barcelona en un función del barrio o distrito deseado. Además, usando diferentes *query parameters* podemos agrupar dichos datos por sexos, edades quinquenales o simplemente, ver el total de habitantes de los mismos.

## Estructura

En la carpeta **front** del repo puedes encontrar el código referente al dashboard de streamlit donde poder visualizar gráficas creadas a partir de los datos extraídos de la API.

En la carpeta **src** se encuentra el código de la API en sí. En la raíz de esta se encuentran la configuración de las variables de entorno y el arranque de la API y en las otras dos carpetas se organiza el resto del código: **controllers** contiene las diferentes rutas de la API, y **utils** contiene archivos con diferentes funciones útiles para el funcionamiento de la API.

## Technologies

[![Python][https://www.python.org/static/img/python-logo@2x.png]][https://www.python.org/] [![Flask][https://flask.palletsprojects.com/en/2.0.x/_images/flask-logo.png]][https://flask.palletsprojects.com/en/2.0.x/] [![Mongodb][https://angularfrontenders.com/wp-content/uploads/2021/01/MONGO-DB-logo-300x470-x.png]][https://www.mongodb.com/es] [![Streamlit][https://cdn-images-1.medium.com/max/1024/1*u9U3YjxT9c9A1FIaDMonHw.png]][https://streamlit.io/] [![Pandas][https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/768px-Pandas_logo.svg.png]][https://pandas.pydata.org/] [![Plotly][https://upload.wikimedia.org/wikipedia/commons/3/37/Plotly-logo-01-square.png]][https://plotly.com/] [![Docker][https://d1.awsstatic.com/acs/characters/Logos/Docker-Logo_Horizontel_279x131.b8a5c41e56b77706656d61080f6a0217a3ba356d.png]][https://www.docker.com/] [![Heroku][https://estebanromero.com/wp-content/uploads/2018/02/heroku1.png]][https://www.heroku.com/platform]

## Manual de uso

Usando el endpoint /neighborhood/\<neigh\> y sustituyendo *neigh* por el nombre del barrio o código (*ver códigos más abajo*), podemos obtener la información de la población de un barrio por edad quinquenal y sexo. El endpoint /district/\<district\> tiene el mismo funcionamiento que el anterior, mostrando todos los documentos de la base de datos correspondientes a ese distrito de Barcelona.

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
