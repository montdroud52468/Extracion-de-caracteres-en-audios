# -*- coding: utf-8 -*-
"""
EXAMEN ORDINARIO 
RICARDO DANIEL MONTIEL JACINTO
1624273
INGENIERIA EN COMPUTACION 
UIVERSIDAD DEL ESTADO DE MEXICO
8-12-21
"""

import librosa
import matplotlib.pyplot as plt
import librosa.display

"""Leemos el archivo en formato wav"""
diraudio = 'C:\\Users\\ricar\\MusOrd\\Prueba.wav' """Modifica tu direccion conforme a donde tengas los archivos"""

"""Se realizara el audio como una matriz enumerada con su taza de muestreo """
val , sr = librosa.load(diraudio)


"""Obtendremos la forma de la aplitud de la onda y la mostraremos en una imagen """

plt.figure(figsize=(14, 5))
librosa.display.waveplot(val, sr=sr)


"""otro caracter que podemos obtener el su espectro del sonido """
dato = librosa.stft(val)
Xdb = librosa.amplitude_to_db(abs(dato))
plt.figure(figsize=(14, 5))
librosa.display.specshow(Xdb, sr=sr, x_axis='Tiempo', y_axis='Hz')
plt.colorbar()



