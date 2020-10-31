from nltk.corpus import wordnet as wn
import pandas as pd, spacy
from collections import Counter
#Importando todos los métodos de la biblioteca MyNLP
from Tesauros_NLP import * 

class Graphs():

    def graphs(self, archivos):

        texto = archivos[0]
        texto = str(texto)

        # Load the small English model
        nlp = spacy.load("en_core_web_lg")

        # Process a text
        doc = nlp(texto)

        #Para nombres mas comunes
        sustantivos=[w.text for w in nlp(texto) if w.is_stop!=True and w.is_punct!=True and w.pos_=='NOUN']
        #Para Verbos mas comunes
        # nombres=[w.text for w in nlp(texto) if w.is_stop!=True and w.is_punct!=True and w.pos_=='VERB']
        # print(nombres)

        # Colocamos los 2 sustantivos mas comunes en cada articulo y el numero de veces que es repetido
        sus_freq = Counter(sustantivos)
        words=[word for (word, freq) in sus_freq.most_common(5)]
        
        # Código para encontrar los synsets de los sustantivos de os articulos
        lst_definition=[]
        for w in words:
            for synset in wn.synsets(w):
                lst_definition.append({'key': w, 'synset': synset, 'definition':synset.definition()})
        df=pd.DataFrame(lst_definition)

        # Método para seleccionar los synset con mayor similitud
        def seleccionarSynsets(verbose=False):    
            groups=getGroups(words,df)
            mc=combinar(groups)   
            vecmay=[]
            sumamay=0    
            for vec in mc:
                md=MatrizTriangularDeMetricas(vec)  
                sm=sumaMat(md)   
                if(len(vecmay)==0):
                    vecmay=vec
                    sumamay=sm
                elif(sm>sumamay):
                    vecmay=vec
                    sumamay=sm            
            return {"synsets":vecmay, "distancia": sumamay}
        #Utilización del método seleccionar Synset
        # print("Combinaciones y distancias")
        selss=seleccionarSynsets()
        # print("Synset seleccionado\n")
        synsetseleccionado=selss['synsets']
        # print("synsets",synsetseleccionado,"distancia",selss['distancia'])

        # Método para encontrar los synonimos de un listado de synset
        def sinonimos(syntsets):    
            for syn in syntsets:         
                s=""
                for lemma in syn.lemmas():
                    s+=lemma.name()+", "

        #Método para encontrar los hipónimos de un listado de synset
        def hiponimos(syntsets):    
            for syn in syntsets:                
                s=""
                for hyponym in syn.hyponyms():
                    s+=hyponym.name()+", "

        #Mostramos la salida de los dos métodos anteriores
        sinonimos(synsetseleccionado)
        hiponimos(synsetseleccionado)

        # Método para encontrar los hyperónimos de un listado de synset 
        # retorna una lista de pares de valores relacionados
        def hiperónimos(syntsets):  
            graph=[]
            for syn in syntsets:
                for hypernyms in syn.hypernym_paths():
                    n=len(hypernyms)
                    for i,hypernym in enumerate(hypernyms):
                        if(i<n-1):
                            n1=hypernyms[i].name().split(".")[0]
                            n2=hypernyms[i+1].name().split(".")[0]
                            graph.append((n1,n2))                    

            return graph

        graph=hiperónimos(synsetseleccionado)

        # Dibujamos el graph
        # graph_science(graph)

        return(graph)