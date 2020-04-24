# En este no necesitamos tener instalado el spacy
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.probability import ConditionalFreqDist
from stop_words import get_stop_words
import pandas as pd

en_stop = get_stop_words('en')

palabras = []
frecuencia = []

# ============ Metodo Para El Proceso: Frecuencia de Palabras ==============
class Frec_Pab():
    
    def frecuencia_palabras(self, archivos):
        nume=len(archivos)
        for i in range(nume):
            texto = archivos[i]
            texto = str(texto)
            token = RegexpTokenizer(r'\w+')
            texto1 = texto.lower()
            tokens = token.tokenize(texto1)

            tokens_clean = [i for i in tokens if not i in en_stop]

            #Realizamos la grafica de la frecuencia de palabra
            freq = nltk.FreqDist(tokens_clean)
            pal=[word for (word, freq) in freq.most_common(10)]
            fre=[freq for (word, freq) in freq.most_common(10)]
            palabras.append(pal)
            frecuencia.append(fre)

        data={'palabras':palabras,'frecuencia':frecuencia}
        grafica=pd.DataFrame(data)  

        return (grafica) 