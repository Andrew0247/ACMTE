import nltk
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words #Para eliminar las palabras de parada
from nltk.stem.porter import PorterStemmer #Para reducir palabras tópicamente similares a su raíz.
from gensim import corpora, models #Para construir una matriz de términos de documento
from gensim.models import CoherenceModel
import gensim
import pandas as pd

en_stop = get_stop_words('en')
p_stemmer = PorterStemmer()
textos_por = []

# ======= Clase LDA para realizar la busqueda de los temas globales ============
class LDA():

	def lda(self, archivos):
		archivos = archivos['Archivos']
		nume=len(archivos)
		for i in range(nume):
			texto = archivos[i]
			texto = str(texto)
			token = RegexpTokenizer(r'\w+')
			texto1 = texto.lower()
			tokens = token.tokenize(texto1)

			tokens_clean = [i for i in tokens if not i in en_stop]
			text = [p_stemmer.stem(i) for i in tokens_clean]
			textos_por.append(text)

		dictionary = corpora.Dictionary(textos_por)
		corpus = [dictionary.doc2bow(text) for text in textos_por]
		ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=3, id2word = dictionary, passes=80)
		temas_glo=ldamodel.print_topics()
		# print(temas_glo) # Vivualizacion de una lista de los temas

		grafica=pd.DataFrame(temas_glo, columns=['numero','temas'])
		print(grafica) # Se mira el dataframe de los temas por consola

		return (grafica)