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

        if proceso==1:
            titulo_ini = "Objective"
            titulo_fin = "Methods"
            if num == 1:
                textoMn=text
                tituloInicial=titulo_ini
                li=re.search(tituloInicial,textoMn)
                tituloFinal=titulo_fin
                ls=re.search(tituloFinal,textoMn)
                textoAl=textoMn[li.start():ls.start()]
                textoAl_A.append(textoAl)

                return (textoAl_A)

        elif proceso==2:
            titulo_ini = "Methods"
            titulo_fin = "Results"
            if num == 1:
                textoMn=text#.lower()#Colocamos todo en minusculas para que las palabras coincidan
                #Realizamos la segmentacion de partes
                tituloInicial=titulo_ini
                li=re.search(tituloInicial,textoMn)#li=threading.Thread(re.search(tituloInicial,textoMn))
                tituloFinal=titulo_fin
                ls=re.search(tituloFinal,textoMn)#ls=threading.Thread(re.search(tituloFinal,textoMn))
                textoAl=textoMn[li.start():ls.start()]#textoAl= textoMn[li.start():ls.start()]
                textoAl_A.append(textoAl)

                return (textoAl_A)

        elif proceso==3:
            titulo_ini = "Results"
            titulo_fin = "Conclusion"
            if num == 1:
            	textoMn=text#.lower()#Colocamos todo en minusculas para que las palabras coincidan
            	#Realizamos la segmentacion de partes
            	tituloInicial=titulo_ini
            	li=re.search(tituloInicial,textoMn)
            	tituloFinal=titulo_fin
            	ls=re.search(tituloFinal,textoMn)
            	textoAl=textoMn[li.start():ls.start()]
            	textoAl_A.append(textoAl)

            	return (textoAl_A)

        elif proceso==4:
            if num == 1:
                textoMn=text#.lower()#Colocamos todo en minusculas para que las palabras coincidan
                #Realizamos la segmentacion de partes
                tituloInicial=titulo_ini
                li=re.search(tituloInicial,textoMn)#li=threading.Thread(re.search(tituloInicial,textoMn))
                tituloFinal=titulo_fin
                ls=re.search(tituloFinal,textoMn)#ls=threading.Thread(re.search(tituloFinal,textoMn))
                textoAl=textoMn[li.start():ls.start()]#textoAl= textoMn[li.start():ls.start()]
                #print(textoAl)
                textoAl_A.append(textoAl)

                return (textoAl_A)
        # else:            
        #     if proceso==0:
        #         titulo_ini = "objective"
        #         titulo_fin = "methods"
        #         if num == 1:
        #             for i in text:
        #                 textoMn=i#.lower()#Colocamos todo en minusculas para que las palabras coincidan
        #                 #print(textoMn)
        #                 #Realizamos la segmentacion de partes
        #                 tituloInicial=titulo_ini
        #                 li=re.search(tituloInicial,textoMn)#li=threading.Thread(re.search(tituloInicial,textoMn))
        #                 tituloFinal=titulo_fin
        #                 ls=re.search(tituloFinal,textoMn)#ls=threading.Thread(re.search(tituloFinal,textoMn))
        #                 textoAl=textoMn[li.start():ls.start()]#textoAl= textoMn[li.start():ls.start()]
        #                 #print(textoAl)
        #                 textoAl_A.append(textoAl)

        #             return (textoAl_A)

        #     elif proceso==0:
        #         titulo_ini = "methods"
        #         titulo_fin = "results"
        #         if num == 1:
        #             for i in text:
        #                 textoMn=i#.lower()#Colocamos todo en minusculas para que las palabras coincidan
        #                 #print(textoMn)
        #                 #Realizamos la segmentacion de partes
        #                 tituloInicial=titulo_ini
        #                 li=re.search(tituloInicial,textoMn)#li=threading.Thread(re.search(tituloInicial,textoMn))
        #                 tituloFinal=titulo_fin
        #                 ls=re.search(tituloFinal,textoMn)#ls=threading.Thread(re.search(tituloFinal,textoMn))
        #                 textoAl=textoMn[li.start():ls.start()]#textoAl= textoMn[li.start():ls.start()]
        #                 #print(textoAl)
        #                 textoAl_A.append(textoAl)

        #             return (textoAl_A)
        #         elif num == 0:
        #             textoMn=text#.lower()#Colocamos todo en minusculas para que las palabras coincidan
        #             #print(textoMn)
        #             #Realizamos la segmentacion de partes
        #             tituloInicial=titulo_ini
        #             li=re.search(tituloInicial,textoMn)#li=threading.Thread(re.search(tituloInicial,textoMn))
        #             tituloFinal=titulo_fin
        #             ls=re.search(tituloFinal,textoMn)#ls=threading.Thread(re.search(tituloFinal,textoMn))
        #             textoAl=textoMn[li.start():ls.start()]#textoAl= textoMn[li.start():ls.start()]
        #             #print(textoAl)
        #             textoAl_A.append(textoAl)

        #             return (textoAl_A)
        #     elif proceso==0:
        #         titulo_ini = "results"
        #         titulo_fin = "conclusion"
        #         if num == 1:
        #             for i in text:
        #                 textoMn=i#.lower()#Colocamos todo en minusculas para que las palabras coincidan
        #                 #print(textoMn)
        #                 #Realizamos la segmentacion de partes
        #                 tituloInicial=titulo_ini
        #                 li=re.search(tituloInicial,textoMn)#li=threading.Thread(re.search(tituloInicial,textoMn))
        #                 tituloFinal=titulo_fin
        #                 ls=re.search(tituloFinal,textoMn)#ls=threading.Thread(re.search(tituloFinal,textoMn))
        #                 textoAl=textoMn[li.start():ls.start()]#textoAl= textoMn[li.start():ls.start()]
        #                 #print(textoAl)
        #                 textoAl_A.append(textoAl)

        #             return (textoAl_A)
        #         elif num == 0:
        #             textoMn=text#.lower()#Colocamos todo en minusculas para que las palabras coincidan
        #             #print(textoMn)
        #             #Realizamos la segmentacion de partes
        #             tituloInicial=titulo_ini
        #             li=re.search(tituloInicial,textoMn)#li=threading.Thread(re.search(tituloInicial,textoMn))
        #             tituloFinal=titulo_fin
        #             ls=re.search(tituloFinal,textoMn)#ls=threading.Thread(re.search(tituloFinal,textoMn))
        #             textoAl=textoMn[li.start():ls.start()]#textoAl= textoMn[li.start():ls.start()]
        #             #print(textoAl)
        #             textoAl_A.append(textoAl)

        #             return (textoAl_A)
        #     elif proceso==0:
        #         titulo_ini = "conclusion"
        #         titulo_fin = "keywords"
        #         if num == 1:
        #             for i in text:
        #                 textoMn=i#.lower()#Colocamos todo en minusculas para que las palabras coincidan
        #                 #print(textoMn)
        #                 #Realizamos la segmentacion de partes
        #                 tituloInicial=titulo_ini
        #                 li=re.search(tituloInicial,textoMn)#li=threading.Thread(re.search(tituloInicial,textoMn))
        #                 tituloFinal=titulo_fin
        #                 ls=re.search(tituloFinal,textoMn)#ls=threading.Thread(re.search(tituloFinal,textoMn))
        #                 textoAl=textoMn[li.start():ls.start()]#textoAl= textoMn[li.start():ls.start()]
        #                 #print(textoAl)
        #                 textoAl_A.append(textoAl)

        #             return (textoAl_A)
        #         elif num == 0:
        #             textoMn=text#.lower()#Colocamos todo en minusculas para que las palabras coincidan
        #             #print(textoMn)
        #             #Realizamos la segmentacion de partes
        #             tituloInicial=titulo_ini
        #             li=re.search(tituloInicial,textoMn)#li=threading.Thread(re.search(tituloInicial,textoMn))
        #             tituloFinal=titulo_fin
        #             ls=re.search(tituloFinal,textoMn)#ls=threading.Thread(re.search(tituloFinal,textoMn))
        #             textoAl=textoMn[li.start():ls.start()]#textoAl= textoMn[li.start():ls.start()]
        #             #print(textoAl)
        #             textoAl_A.append(textoAl)

        #             return (textoAl_A)