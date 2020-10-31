import easygui as eg, nltk, re, spacy # threading era para realizar el metodo.start
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from spacy.matcher import Matcher
from Seccionar_Partes import Seccionar_Partes
import pandas as pd

sec_part=Seccionar_Partes()
# p_sin=[]
palabras = []
frecuencia = []


# ============ Metodo Para El Proceso: Padre Sintactico ==============
class Padre_Sintactico():

	def padre_sintactico(self, articulo, proceso, archivos):
		texto=[]
		archivos = archivos['Archivos']
		arch=len(archivos)
		for i in range(arch):
			texto = archivos[i]
			frag = sec_part.seccionar_partes(texto, proceso,1)
			# print(frag)
			# archiv.append(frag)

		# print(archiv)
		nlp = spacy.load("en_core_web_lg") # se carga el modelo de vectores de palabras de spacy
		# matcher = Matcher(nlp.vocab) # necesitamos un vocabulario llamado vocab
		nume=len(frag)
		for i in range(nume):
			texto_sin=frag[i] # Añadimos el fragmento a una variable
			texto_sin=str(texto_sin) # la convertimos en string
			doc = nlp(texto_sin) # lo implementamos en un nlp de spacy
			s=[span.head.text for span in doc]
			freq = nltk.FreqDist(s)
			pal=[word for (word, freq) in freq.most_common(10)]
			fre=[freq for (word, freq) in freq.most_common(10)]
			palabras.append(pal)
			frecuencia.append(fre)
		
		data={'padres':palabras,'frecuencia':frecuencia}
		grafica=pd.DataFrame(data)
		# print(grafica) 

		return (grafica)