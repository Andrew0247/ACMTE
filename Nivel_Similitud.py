import easygui as eg, nltk, re, spacy
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from spacy.matcher import Matcher
from Seccionar_Partes import Seccionar_Partes
import pandas as pd

sec_part=Seccionar_Partes()

archivos = []
archiv = []
nivelSim=[]
art1_6=[]
art2_6=[]
art3_6=[]
art4_6=[]
art5_6=[]

# ============ Metodo Para El Proceso: Nivel de Similitud ==============
class Nivel_Similitud():

    def nivel_similitud(self, articulo, proceso, archivos):
        texto=[]
        arch=len(archivos)
        # Realizamos el seccionamiento de las partes
        for i in range(arch):
            texto = archivos[i]
            frag = sec_part.seccionar_partes(texto, proceso,1)
            # archiv.append(frag)
                   
        nlp = spacy.load('en_core_web_lg')#importamos un modelo grande
        
        # articulos del 1-2 al 1-6
        for i in range(1,6):
        	doc1 = frag[0]
        	doc2 = frag[i]
        	doc1_1=nlp(doc1)
        	doc2_2=nlp(doc2)
        	niv = round(doc1_1.similarity(doc2_2), 4)
        	art1_6.append(niv)
            
        # articulos del 2-3 al 2-6
        for j in range(2,6):
        	doc1 = frag[1]
        	doc2 = frag[j]
        	doc1_1=nlp(doc1)
        	doc2_2=nlp(doc2)
        	niv = round(doc1_1.similarity(doc2_2), 4)
        	art2_6.append(niv)

        # articulos del 3-4 al 3-6
        for j in range(3,6):
        	doc1 = frag[2]
        	doc2 = frag[j]
        	doc1_1=nlp(doc1)
        	doc2_2=nlp(doc2)
        	niv= round(doc1_1.similarity(doc2_2), 4)
        	art3_6.append(niv)

        # articulos del 4-5 al 4-6
        for j in range(4,6):
        	doc1 = frag[3]
        	doc2 = frag[j]
        	doc1_1=nlp(doc1)
        	doc2_2=nlp(doc2)
        	niv = round(doc1_1.similarity(doc2_2), 4)
        	art4_6.append(niv)

        # articulos del 2-3 al 2-6
        for j in range(5,6):
        	doc1 = frag[4]
        	doc2 = frag[j]
        	doc1_1=nlp(doc1)
        	doc2_2=nlp(doc2)
        	niv = round(doc1_1.similarity(doc2_2), 4)
        	art5_6.append(niv)

        nivelSim.append(art1_6)
        nivelSim.append(art2_6)
        nivelSim.append(art3_6)
        nivelSim.append(art4_6)
        nivelSim.append(art5_6)
        print(nivelSim)
        
        # Retornamos el nivel de similitud
        return (nivelSim)