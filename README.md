# Extracion-de-caracteres-en-audios
Este es un código realizado en Python para poder extraer caracteres del audio, como por ejemplo sus ondas o niveles del sonido etc. 

Para el desarrollo de este programa haremos uso de la libreria librosa, el cual es un paquete python para análisis de música y audio. Proporciona los bloques de construcción necesarios para crear sistemas de recuperación de información musical.

Esta libreria solo permite archivos con formato WAV, yo estuve intentando usar otro formato como lo son MP3, OGG pero no obtuve ningun exito a la hora de la lectura, investigando un poco sobre el porque no podia, es porque el formato WAV es un fomato que no esta comprimido los datos y algo que medio recuerdo es que es un formato con informacion de onda y esto permitia que fuera mas facil a la hora de usar este formato 

Primero analizamos el audio de un ladrido de perro y obtenemos lo siguiente 

ONDAS DE AUDIO PERRO

![image](https://user-images.githubusercontent.com/39661323/145274267-5dd9f93c-65fb-42e1-b9d5-26eb02b1d279.png)

ESPECTRO DE SONIDO PERRO

![image](https://user-images.githubusercontent.com/39661323/145274315-878a28a2-07ed-4f06-b048-310216928bfe.png)

ONDAS DE AUDIO CLAXON

![image](https://user-images.githubusercontent.com/39661323/145275143-1aa8f032-4804-41ed-9d56-2ae0d1a0d449.png)

ESPECTRO DE SONIDO CLAXON

![image](https://user-images.githubusercontent.com/39661323/145275291-0984efdd-b823-407a-be88-e60cc129eedd.png)


Como podemos ver y siempre hemos notado los ladridos de un perro siempre tienen una mayor señal en hz 
