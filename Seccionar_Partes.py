import easygui as eg, nltk, re, spacy # threading era para realizar el metodo.start
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from spacy.matcher import Matcher

archivos = []
extension = ["*.txt"]
textoAl_A = []

# ========== Busqueda Por Partes ===============
class Seccionar_Partes():

    def seccionar_partes(self, text, proceso, num):

        def seg_partes(titulo_ini, titulo_fin, text):
            li = re.search(titulo_ini, text)
            ls = re.search(titulo_fin, text)
            textoAl = text[li.start():ls.start()]

            return(textoAl)

        if proceso==1:
            titulo_ini = "Objective"
            titulo_fin = "Methods"
            textoAl_A.append(seg_partes(titulo_ini, titulo_fin, text))

            return (textoAl_A)

        elif proceso==2:
            titulo_ini = "Methods"
            titulo_fin = "Results"
            textoAl_A.append(seg_partes(titulo_ini, titulo_fin, text))

            return (textoAl_A)

        elif proceso==3:
            titulo_ini = "Results"
            titulo_fin = "Conclusion"
            textoAl_A.append(seg_partes(titulo_ini, titulo_fin, text))

            return (textoAl_A)

        elif proceso==4:
            titulo_ini = "Conclusion"
            titulo_fin = "Keywords"
            textoAl_A.append(seg_partes(titulo_ini, titulo_fin, text))

            return (textoAl_A)
        