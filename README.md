# DATA PROJECT 1
![EDEM](https://datos.gob.es/sites/default/files/styles/success_image/public/success/images/idealista.jpg?itok=uX21SrOq)
Carlos Torres, Sara Adam, Pablo Martínez, Jorge Arce y Marina Pérez

## Descripción

El portl líder de compra de vivienda en España quiere sacar un piloto de calidad de vida aplicado a la vivienda y ha elegido Valencia como sede para su piloto.
La idea de este piloto es ofrecer un mapa de calidad de la vivienda en función de indicadores de datos abiertos. 
La calidad de la vivienda se medirá por ruido, hospitales, contaminación...teniendo que dar una nota a una zona en concreto en base a dichos parámetros.

Dentro de la carpeta encontramos los siguientes ficheros:

| Ficheros | Contenido |
| ------ | ------ |
| docker-compose | Código para construir los contenedores |
| main.py | Script de python con el código del ejercicio |
| visualización | Dashboard de Tableau donde una vez levantado el contenedor de la base de datos se puede interactuar con el mapa de Valencia |

## Elección de filtros
Los filtros por los que nuestros subscriptores pueden navegar en nuestra aplicación son los siguientes:
- Hospitales
- Colegios
- Parkings
- Zonas de carga vehículos eléctricos

**HOSPITALES**
Después de la realización de un riguroso Estudio de Mercado, nos encontramos con que el perfil del usuario medio de nuestra aplicación es Varón, con una edad comprendida entre los 35-45 años, con un nivel adquisitivo suficiente para la adquisición de una vivienda, padre de familia,  preocupado por la sostenibilidad pero acostumbra a una situación de bienestar. 
Hablar de salud es hablar de un pilar primordial para el bienestar de la vida de cualquier persona y es exactamente por eso que considerar la cercanía de hospitales a la hora de escoger la residencia está entre sus prioridades, tanto por el cuidado de la familia, como por la plusvalía que este factor le puede brindar a la propiedad. 
La salud a cualquier edad necesita ciertos cuidados, así que asegurarse de tener fácil acceso a un hospital ya sea para citas, tratamientos o revisiones es prevenir un gran beneficio para el futuro. Reducir el recorrido entre el hogar y el hospital es una gran ventaja sobre todo si la situación es de emergencia y requiere de una pronta atención.
Hoy en día, con el constante crecimiento de las ciudades y el tráfico, encontrar una propiedad que permita tener acceso a espacios de vital importancia para las actividades diarias es una gran ventaja, pero cuando la zona además brinda espacios para el cuidado de la salud representa un valor agregado.  Este aspecto aumenta el valor de la propiedad gracias a que es parte de la zona residencial para ofrecer una mejor calidad de vida a sus habitantes. 
Actualmente cuidar de la salud es un tema que ha tomado más fuerza en el estilo de vida de las personas. Considerar que un hospital se vuelve parte de su entorno brinda seguridad en caso de emergencia y la accesibilidad de volver las visitas de prevención parte de su rutina de vida.

**COLEGIOS**
La cercanía de la vivienda al centro educativo beneficia la conciliación y la autonomía de los hijos, disminuye los esfuerzos logísticos y revaloriza el inmueble. La ida y la vuelta al colegio puede convertirse en un desafío logístico y un gasto de tiempo cuando se depende del vehículo privado, del metro o el autobús para llevar y recoger a los hijos del colegio. Desde que comienzan su etapa escolar, estos dos momentos del día van a marcar los horarios laborales y la organización familiar, que se ve simplificada enormemente cuando el centro educativo está situado a solo un paseo de casa.
Vivir cerca del colegio ahorra tiempo en los desplazamientos, evita el problema que supone no disponer puntualmente del coche y también permite librarse de los problemas de aparcamiento en el entorno del centro educativo en horas punta. Además, los compañeros del colegio son el entorno de socialización más cercano durante la infancia, y vivir en las proximidades del colegio supone compartir el mismo barrio, además del aula.
Que la vivienda esté cerca del colegio implica que lo esté también en casa sus amigos cuando haya un cumpleaños, vayan a hacer un trabajo a casa de sus compañeros o queden con ellos, cuando sean un poco más mayores. Llegada la edad de poder ir al colegio solos o con otros compañeros de clase, esto será más fácil y ocurrirá antes cuanto más cerca se encuentre el colegio de casa; lo que además de ser un pequeño desahogo para los padres ayudará a que los hijos e hijas adquieran una mayor autonomía.

**ZONAS DE CARGA DE VEHÍCULOS ELÉCTRICOS**
Una encuesta realizada en 2020 por Consumer Reports mostró que el 71% de los conductores considerarían la posibilidad de comprar un vehículo eléctrico en el futuro. Esto es un gran numero de clientes potenciales y clientes que pueden estar buscando un lugar para cargar su vehículo eléctrico mientras realizan sus compras o comen, por ello nuestros usuarios buscan locales para desarrollar un negocio cerca de zonas de carga.
No sólo eso, sino que los sensación sobre la disponibilidad de carga entre los actuales propietarios de vehículos eléctricos es variada. Los conductores creen que no siempre pueden encontrar una estación de carga adecuada cuando la necesitan. Si sus clientes se están pasando a los vehículos eléctricos y tienen que elegir entre su negocio con un parking para cargar y el de un competidor sin puntos de recarga, ¿qué lugar cree que elegirán?

**PARKING**
Uno de los principales inconvenientes de vivir en las mejores zonas de la ciudad es precisamente el aparcamiento. Venir de trabajar y tener que perder tanto tiempo para estacionar el vehículo hace que la paciencia se agote y el estrés aumente sin parar.  Volver a casa se convierte en una odisea ¿Imagina todo el tiempo que has perdido aparcando tu coche en un sitio seguro y que podrías haber aprovechado para descansar, hacer deporte o disfrutar de un rato de diversión con los tuyos? 
Tener cerca de casa parkings librará de comederos de cabeza y de problemas de aparcamiento. Podrás salir del trabajo y en tan solo unos minutos estar con los tuyos.
Seguridad Rayones, robos, suciedad, problemas de arranque por el frío...son algunos de los factores negativos ligados a aparcar el coche en la calle. Sin embargo, un parking elimina todos estos riesgos y los reduce casi a cero. 

## MODELO DE DATOS
En la siguiente imagen se puede observar el modelo de datos de este proyecto. La base de datos está construida en base a estas relaciones. 
![Modelo de datos](https://github.com/marinapb16/DATA-PROJECT-1/blob/main/tablas.png)

## PASOS A SEGUIR
Con docker-compose creamos dos contenedores, uno que me va a levantar la base de datos postgres y el otro para poder abrir el pgadmin y visualizar la base de datos. 

Para levantar los contenedores docker:
```sh
docker-compose up -d
```
Con esto ya tenemos los contenedores en marcha. El siguiente paso es ir al navegador e introducir:
```sh
localhost:5050
```
Esto nos llevará a la página pgadmin donde introduciremos los siguientes datos para acceder a la plataforma:
```sh
user: raj@nola.com
password: admin
```
Creamos un nuevo servicio que nos haga la conexión con la base de datos que hemos creado llamada postgres. Una vez creado, volvemos a visual studio y ejecutamos el main.py, donde se ha creado todo el código que introduce los distintos datos descargados en la base de datos. Una vez la base de datos está cargada, ya podemos conectar Tableau a nuestra base de datos PostgreSQL.
