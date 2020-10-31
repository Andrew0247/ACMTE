import tkinter as tk, nltk, numpy as np, gensim
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure
from gensim import corpora, models #Para construir una matriz de términos de documento
from PIL import ImageTk, Image
import os
from Cargar_Archivos import Cargar
from Frecuencia_Palabras import Frec_Pab
from Padre_Sintactico import Padre_Sintactico
from Nivel_Similitud import Nivel_Similitud
from LDA import LDA
from Graphs import Graphs
# Importamos la biblioteca MyNLP
from Tesauros_NLP import *

carga_arc=Cargar()
frec_pab=Frec_Pab()
pad_sintac=Padre_Sintactico()
niv_simi=Nivel_Similitud()
lda_modelo = LDA()
graphs_load = Graphs()

# variables globales para imagenes en las ventanas 
# "padre sintactico" y "nivel de similitud"
global imgo, imgm, imgr, imgc
 
root= tk.Tk()
root.title("  Graphs Of Sciencie  ")

# Canvas para graficar figuras, imagenes, etc
canvas1 = tk.Canvas(root, width = 1000, height = 680)
canvas1.pack(side=tk.LEFT)

# Funcion donde se realiza el proceso para la frecuencia de palabras
def proceso_frecpab():
    global bar1

    archiv=carga_arc.cargar_archivos()
    # Aqui Creamos la Ventana donde se mostrara  la frecuencia de Palabras
    frecp=tk.Toplevel()
    frecp.title("Frecuencia de Palabras")

    frecuencia = frec_pab.frecuencia_palabras(archiv) # se llama la funcion para realizar la frecuencia de palabras
    # print(frecuencia) # Descomentas este para ver el pandas de las frecuencias de palabras
    figure1 = Figure(figsize=(16,8), dpi=80) # Se realiza una instancia de Figura dandole un tamaño (8,4) con un dpi de 100, CONSULTAR "dpi"
    subplot1 = figure1.add_subplot(321) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt1 = frecuencia.palabras.loc[0]
    xArt1 = frecuencia.frecuencia.loc[0]
    subplot1.plot(xArt1,yArt1, 'b-.') # Graficamos la frecuencia de palabras en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[0])
    subplot1.grid()
    
    subplot1 = figure1.add_subplot(322) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt2 = frecuencia.palabras.loc[1]
    xArt2 = frecuencia.frecuencia.loc[1]
    subplot1.plot(xArt2,yArt2, 'r-.') # Graficamos la frecuencia de palabras en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[1])
    subplot1.grid()

    subplot1 = figure1.add_subplot(323) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt3 = frecuencia.palabras.loc[2]
    xArt3 = frecuencia.frecuencia.loc[2]
    subplot1.plot(xArt3,yArt3, 'g-.') # Graficamos la frecuencia de palabras en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[2])
    subplot1.grid()

    subplot1 = figure1.add_subplot(324) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt4 = frecuencia.palabras.loc[3]
    xArt4 = frecuencia.frecuencia.loc[3]
    subplot1.plot(xArt4,yArt4, 'c-.') # Graficamos la frecuencia de palabras en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[3])
    subplot1.grid()

    subplot1 = figure1.add_subplot(325) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt5 = frecuencia.palabras.loc[4]
    xArt5 = frecuencia.frecuencia.loc[4]
    subplot1.plot(xArt5,yArt5, 'm-.') # Graficamos la frecuencia de palabras en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[4])
    subplot1.grid()

    subplot1 = figure1.add_subplot(326) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt6 = frecuencia.palabras.loc[5]
    xArt6 = frecuencia.frecuencia.loc[5]
    subplot1.plot(xArt6,yArt6, 'y-.') # Graficamos la frecuencia de palabras en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[5])
    subplot1.grid()

    bar1 = FigureCanvasTkAgg(figure1, frecp) # Añadimos dicho grafico a la Interfaz grafica
    bar1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=0) # damos la posicion para que aparezca la grafica
    toolbar = NavigationToolbar2Tk(bar1, frecp)# barra de iconos para guardar o configurar el grafico
    toolbar.update()
    bar1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Funcion donde se realiza el proceso del padre sintactico
def padre_sintac():
    padS=tk.Toplevel()
    padS.title(" Padre Sintactico ")
    padS.geometry('400x430')

    # Imagen para Objetivo
    imgo = Image.open("img\objetivo.jpg")
    imgo = imgo.resize((120,130), Image.ANTIALIAS)
    imgo = ImageTk.PhotoImage(imgo)
    label_1 = tk.Label(padS, image=imgo)
    label_1.image = imgo
    label_1.place(x = 30, y = 20)

    button1 = tk.Button (padS, text=' Objetivo ',command=objetivo, font=('Arial', 11, 'bold'))
    button1.place(x = 43, y = 163)

    # Imagen para Metodo
    imgm = Image.open("img\metodos.png")
    imgm = imgm.resize((120,130), Image.ANTIALIAS)
    imgm = ImageTk.PhotoImage(imgm)
    label_1 = tk.Label(padS, image=imgm)
    label_1.image = imgm
    label_1.place(x = 250, y = 20)

    button1 = tk.Button (padS, text=' Metodo ',command=metodo, font=('Arial', 11, 'bold'))
    button1.place(x = 275, y = 163)

    # Imagen para Resultados
    imgr = Image.open("img\Resultados.png")
    imgr = imgr.resize((120,130), Image.ANTIALIAS)
    imgr = ImageTk.PhotoImage(imgr)
    label_1 = tk.Label(padS, image=imgr)
    label_1.image = imgr
    label_1.place(x = 30, y = 220)

    button1 = tk.Button (padS, text=' Resultados ',command=resultado, font=('Arial', 11, 'bold'))
    button1.place(x = 40, y = 365)

    # Imagen para Conclusion
    imgc = Image.open("img\conclusion2.jpg")
    imgc = imgc.resize((120,130), Image.ANTIALIAS)
    imgc = ImageTk.PhotoImage(imgc)
    label_1 = tk.Label(padS, image=imgc)
    label_1.image = imgc
    label_1.place(x = 250, y = 220)

    button1 = tk.Button (padS, text=' Conclusion ',command=conclusion, font=('Arial', 11, 'bold'))
    button1.place(x = 260, y = 365)

def objetivo():
    global bar1
    archiv=carga_arc.cargar_archivos()
    pad_sintac1=pad_sintac.padre_sintactico(1, 1, archiv) # Toca modificar el numero 2 para que realice con respecto al resumen, objetivo, etc...
    # print(pad_sintac1) # Descomentas esta linea para ver el pandas de los padres sintacticos

    padS=tk.Toplevel()
    padS.title(" Padre Sintactico Resumen ")
    figure1 = Figure(figsize=(16,8), dpi=80) # Se realiza una instancia de Figura dandole un tamaño (8,4) con un dpi de 100, CONSULTAR "dpi"
    subplot1 = figure1.add_subplot(321) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt1 = pad_sintac1.padres.loc[0]
    xArt1 = pad_sintac1.frecuencia.loc[0]
    subplot1.plot(xArt1,yArt1, 'b-.') # Graficamos la frecuencia de padres en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[0])
    subplot1.grid()
    
    subplot1 = figure1.add_subplot(322) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt2 = pad_sintac1.padres.loc[1]
    xArt2 = pad_sintac1.frecuencia.loc[1]
    subplot1.plot(xArt2,yArt2, 'r-.') # Graficamos la frecuencia de padres en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[1])
    subplot1.grid()
    # subplot1.title(' Art2 ', fontsize=12)

    subplot1 = figure1.add_subplot(323) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt3 = pad_sintac1.padres.loc[2]
    xArt3 = pad_sintac1.frecuencia.loc[2]
    subplot1.plot(xArt3,yArt3, 'g-.') # Graficamos la frecuencia de padres en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[2])
    subplot1.grid()

    subplot1 = figure1.add_subplot(324) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt4 = pad_sintac1.padres.loc[3]
    xArt4 = pad_sintac1.frecuencia.loc[3]
    subplot1.plot(xArt4,yArt4, 'c-.') # Graficamos la frecuencia de padres en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[3])
    subplot1.grid()

    subplot1 = figure1.add_subplot(325) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt5 = pad_sintac1.padres.loc[4]
    xArt5 = pad_sintac1.frecuencia.loc[4]
    subplot1.plot(xArt5,yArt5, 'm-.') # Graficamos la frecuencia de padres en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[4])
    subplot1.grid()

    subplot1 = figure1.add_subplot(326) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt6 = pad_sintac1.padres.loc[5]
    xArt6 = pad_sintac1.frecuencia.loc[5]
    subplot1.plot(xArt6,yArt6, 'y-.') # Graficamos la frecuencia de padres en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[5])
    subplot1.grid()

    bar1 = FigureCanvasTkAgg(figure1, padS) # Añadimos dicho grafico a la Interfaz grafica
    bar1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=0) # damos la posicion para que aparezca la grafica
    toolbar = NavigationToolbar2Tk(bar1, padS)# barra de iconos para guardar o configurar el grafico
    toolbar.update()
    bar1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def metodo():
    global bar1
    archiv=carga_arc.cargar_archivos()
    pad_sintac1=pad_sintac.padre_sintactico(1, 2, archiv) # Toca modificar el numero 2 para que realice con respecto al resumen, objetivo, etc...
    # print(pad_sintac1) # Esta linea muestra en consola la grafica de la frecuencia de los padres sintacticos

    padS=tk.Toplevel()
    padS.title(" Padre Sintactico Metodo ")
    figure1 = Figure(figsize=(16,8), dpi=80) # Se realiza una instancia de Figura dandole un tamaño (8,4) con un dpi de 100, CONSULTAR "dpi"
    subplot1 = figure1.add_subplot(321) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt1 = pad_sintac1.padres.loc[0]
    xArt1 = pad_sintac1.frecuencia.loc[0]
    subplot1.plot(xArt1,yArt1, 'b-.') # Graficamos la frecuencia de padres en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[0])
    subplot1.grid()
    
    subplot1 = figure1.add_subplot(322) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt2 = pad_sintac1.padres.loc[1]
    xArt2 = pad_sintac1.frecuencia.loc[1]
    subplot1.plot(xArt2,yArt2, 'r-.') # Graficamos la frecuencia de padres en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[1])
    subplot1.grid()
    # subplot1.title(' Art2 ', fontsize=12)

    subplot1 = figure1.add_subplot(323) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt3 = pad_sintac1.padres.loc[2]
    xArt3 = pad_sintac1.frecuencia.loc[2]
    subplot1.plot(xArt3,yArt3, 'g-.') # Graficamos la frecuencia de padres en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[2])
    subplot1.grid()

    subplot1 = figure1.add_subplot(324) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt4 = pad_sintac1.padres.loc[3]
    xArt4 = pad_sintac1.frecuencia.loc[3]
    subplot1.plot(xArt4,yArt4, 'c-.') # Graficamos la frecuencia de padres en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[3])
    subplot1.grid()

    subplot1 = figure1.add_subplot(325) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt5 = pad_sintac1.padres.loc[4]
    xArt5 = pad_sintac1.frecuencia.loc[4]
    subplot1.plot(xArt5,yArt5, 'm-.') # Graficamos la frecuencia de padres en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[4])
    subplot1.grid()

    subplot1 = figure1.add_subplot(326) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt6 = pad_sintac1.padres.loc[5]
    xArt6 = pad_sintac1.frecuencia.loc[5]
    subplot1.plot(xArt6,yArt6, 'y-.') # Graficamos la frecuencia de padres en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[5])
    subplot1.grid()

    bar1 = FigureCanvasTkAgg(figure1, padS) # Añadimos dicho grafico a la Interfaz grafica
    bar1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=0) # damos la posicion para que aparezca la grafica
    toolbar = NavigationToolbar2Tk(bar1, padS)# barra de iconos para guardar o configurar el grafico
    toolbar.update()
    bar1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def resultado():
    global bar1
    archiv=carga_arc.cargar_archivos()
    pad_sintac1=pad_sintac.padre_sintactico(1, 3, archiv) # Toca modificar el numero 2 para que realice con respecto al resumen, objetivo, etc...
    # print(pad_sintac1) Esta linea es la que muestra la grafica por consola
    
    padS=tk.Toplevel()
    padS.title(" Padre Sintactico Resultado ")
    figure1 = Figure(figsize=(16,8), dpi=80) # Se realiza una instancia de Figura dandole un tamaño (8,4) con un dpi de 100, CONSULTAR "dpi"
    subplot1 = figure1.add_subplot(321) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt1 = pad_sintac1.padres.loc[0]
    xArt1 = pad_sintac1.frecuencia.loc[0]
    subplot1.plot(xArt1,yArt1, 'b-.') # Graficamos la frecuencia de padres en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[0])
    subplot1.grid()
    
    subplot1 = figure1.add_subplot(322) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt2 = pad_sintac1.padres.loc[1]
    xArt2 = pad_sintac1.frecuencia.loc[1]
    subplot1.plot(xArt2,yArt2, 'r-.') # Graficamos la frecuencia de padres en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[1])
    subplot1.grid()
    # subplot1.title(' Art2 ', fontsize=12)

    subplot1 = figure1.add_subplot(323) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt3 = pad_sintac1.padres.loc[2]
    xArt3 = pad_sintac1.frecuencia.loc[2]
    subplot1.plot(xArt3,yArt3, 'g-.') # Graficamos la frecuencia de padres en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[2])
    subplot1.grid()

    subplot1 = figure1.add_subplot(324) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt4 = pad_sintac1.padres.loc[3]
    xArt4 = pad_sintac1.frecuencia.loc[3]
    subplot1.plot(xArt4,yArt4, 'c-.') # Graficamos la frecuencia de padres en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[3])
    subplot1.grid()

    subplot1 = figure1.add_subplot(325) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt5 = pad_sintac1.padres.loc[4]
    xArt5 = pad_sintac1.frecuencia.loc[4]
    subplot1.plot(xArt5,yArt5, 'm-.') # Graficamos la frecuencia de padres en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[4])
    subplot1.grid()

    subplot1 = figure1.add_subplot(326) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt6 = pad_sintac1.padres.loc[5]
    xArt6 = pad_sintac1.frecuencia.loc[5]
    subplot1.plot(xArt6,yArt6, 'y-.') # Graficamos la frecuencia de padres en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[5])
    subplot1.grid()

    bar1 = FigureCanvasTkAgg(figure1, padS) # Añadimos dicho grafico a la Interfaz grafica
    bar1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=0) # damos la posicion para que aparezca la grafica
    toolbar = NavigationToolbar2Tk(bar1, padS)# barra de iconos para guardar o configurar el grafico
    toolbar.update()
    bar1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def conclusion():
    global bar1
    archiv=carga_arc.cargar_archivos()
    pad_sintac1=pad_sintac.padre_sintactico(1, 4, archiv) # Toca modificar el numero 2 para que realice con respecto al resumen, objetivo, etc...
    # print(pad_sintac1) # Esta linea muestra la grafica por consola
    
    padS=tk.Toplevel()
    padS.title(" Padre Sintactico Conclusion ")
    figure1 = Figure(figsize=(16,8), dpi=80) # Se realiza una instancia de Figura dandole un tamaño (8,4) con un dpi de 100, CONSULTAR "dpi"
    subplot1 = figure1.add_subplot(321) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt1 = pad_sintac1.padres.loc[0]
    xArt1 = pad_sintac1.frecuencia.loc[0]
    subplot1.plot(xArt1,yArt1, 'b-.') # Graficamos la frecuencia de padres en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[0])
    subplot1.grid()
    
    subplot1 = figure1.add_subplot(322) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt2 = pad_sintac1.padres.loc[1]
    xArt2 = pad_sintac1.frecuencia.loc[1]
    subplot1.plot(xArt2,yArt2, 'r-.') # Graficamos la frecuencia de padres en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[1])
    subplot1.grid()
    # subplot1.title(' Art2 ', fontsize=12)

    subplot1 = figure1.add_subplot(323) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt3 = pad_sintac1.padres.loc[2]
    xArt3 = pad_sintac1.frecuencia.loc[2]
    subplot1.plot(xArt3,yArt3, 'g-.') # Graficamos la frecuencia de padres en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[2])
    subplot1.grid()

    subplot1 = figure1.add_subplot(324) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt4 = pad_sintac1.padres.loc[3]
    xArt4 = pad_sintac1.frecuencia.loc[3]
    subplot1.plot(xArt4,yArt4, 'c-.') # Graficamos la frecuencia de padres en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[3])
    subplot1.grid()

    subplot1 = figure1.add_subplot(325) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt5 = pad_sintac1.padres.loc[4]
    xArt5 = pad_sintac1.frecuencia.loc[4]
    subplot1.plot(xArt5,yArt5, 'm-.') # Graficamos la frecuencia de padres en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[4])
    subplot1.grid()

    subplot1 = figure1.add_subplot(326) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt6 = pad_sintac1.padres.loc[5]
    xArt6 = pad_sintac1.frecuencia.loc[5]
    subplot1.plot(xArt6,yArt6, 'y-.') # Graficamos la frecuencia de padres en un diagrama de barras
    subplot1.set_title(archiv.Titulo.loc[5])
    subplot1.grid()

    bar1 = FigureCanvasTkAgg(figure1, padS) # Añadimos dicho grafico a la Interfaz grafica
    bar1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=0) # damos la posicion para que aparezca la grafica
    toolbar = NavigationToolbar2Tk(bar1, padS)# barra de iconos para guardar o configurar el grafico
    toolbar.update()
    bar1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Funcion para el Nivel de Silimitud
def nivel_simi():
    simiN=tk.Toplevel()
    simiN.title(" Nivel de Similitud ")
    simiN.geometry('400x430')

    # Imagen para Objetivo
    imgo = Image.open("img\objetivo.jpg")
    imgo = imgo.resize((120,130), Image.ANTIALIAS)
    imgo = ImageTk.PhotoImage(imgo)
    label_1 = tk.Label(simiN, image=imgo)
    label_1.image = imgo
    label_1.place(x = 30, y = 20)

    button1 = tk.Button (simiN, text=' Objetivo ',command=objetivo2, font=('Arial', 11, 'bold'))
    button1.place(x = 43, y = 163)

    # Imagen para Metodo
    imgm = Image.open("img\metodos.png")
    imgm = imgm.resize((120,130), Image.ANTIALIAS)
    imgm = ImageTk.PhotoImage(imgm)
    label_1 = tk.Label(simiN, image=imgm)
    label_1.image = imgm
    label_1.place(x = 250, y = 20)

    button1 = tk.Button (simiN, text=' Metodo ',command=metodo2, font=('Arial', 11, 'bold'))
    button1.place(x = 275, y = 163)

    # Imagen para Resultados
    imgr = Image.open("img\Resultados.png")
    imgr = imgr.resize((120,130), Image.ANTIALIAS)
    imgr = ImageTk.PhotoImage(imgr)
    label_1 = tk.Label(simiN, image=imgr)
    label_1.image = imgr
    label_1.place(x = 30, y = 220)

    button1 = tk.Button (simiN, text=' Resultados ',command=resultado2, font=('Arial', 11, 'bold'))
    button1.place(x = 40, y = 365)

    # Imagen para Conclusion
    imgc = Image.open("img\conclusion2.jpg")
    imgc = imgc.resize((120,130), Image.ANTIALIAS)
    imgc = ImageTk.PhotoImage(imgc)
    label_1 = tk.Label(simiN, image=imgc)
    label_1.image = imgc
    label_1.place(x = 250, y = 220)

    button1 = tk.Button (simiN, text=' Conclusion ',command=conclusion2, font=('Arial', 11, 'bold'))
    button1.place(x = 260, y = 365)

def objetivo2():
    archiv=carga_arc.cargar_archivos()
    niv_simi1=niv_simi.nivel_similitud(1, 1, archiv) # Toca modificar el numero 2 para que realice con respecto al resumen, objetivo, etc...
    niv1=niv_simi1[0]
    niv2=niv_simi1[1]
    niv3=niv_simi1[2]
    niv4=niv_simi1[3]
    niv5=niv_simi1[4]
    simiN=tk.Toplevel()
    simiN.title(" Nivel de Similitud Resumen ")
    simiN.geometry('600x250')
    label=tk.Label(simiN, text="").pack(side=tk.TOP)
    label=tk.Label(simiN, text=" Articulos Combinados: 1-2 al 1-6 ").pack(side=tk.TOP)
    label=tk.Label(simiN, text=niv1).pack(side=tk.TOP)
    label=tk.Label(simiN, text=" Articulos Combinados: 2-3 al 2-6 ").pack(side=tk.TOP)
    label=tk.Label(simiN, text=niv2).pack(side=tk.TOP)
    label=tk.Label(simiN, text=" Articulos Combinados: 3-4 al 3-6 ").pack(side=tk.TOP)
    label=tk.Label(simiN, text=niv3).pack(side=tk.TOP)
    label=tk.Label(simiN, text=" Articulos Combinados: 4-5 al 4-6 ").pack(side=tk.TOP)
    label=tk.Label(simiN, text=niv4).pack(side=tk.TOP)
    label=tk.Label(simiN, text=" Articulos Combinados: 5-6 ").pack(side=tk.TOP)
    label=tk.Label(simiN, text=niv5).pack(side=tk.TOP)
    Button = tk.Button(simiN, command=mostrar_titulo_NS(archiv), font=('Arial', 11, 'bold')).pack(side = tk.RIGHT)

def metodo2():
    archiv=carga_arc.cargar_archivos()
    niv_simi1=niv_simi.nivel_similitud(1, 2, archiv) # Toca modificar el numero 2 para que realice con respecto al resumen, objetivo, etc...
    niv1=niv_simi1[0]
    niv2=niv_simi1[1]
    niv3=niv_simi1[2]
    niv4=niv_simi1[3]
    niv5=niv_simi1[4]
    simiN=tk.Toplevel()
    simiN.title(" Nivel de Similitud Metodo ")
    simiN.geometry('600x250')
    label=tk.Label(simiN, text="").pack(side=tk.TOP)
    label=tk.Label(simiN, text=" Articulos Combinados: 1-2 al 1-6 ").pack(side=tk.TOP)
    label=tk.Label(simiN, text=niv1).pack(side=tk.TOP)
    label=tk.Label(simiN, text=" Articulos Combinados: 2-3 al 2-6 ").pack(side=tk.TOP)
    label=tk.Label(simiN, text=niv2).pack(side=tk.TOP)
    label=tk.Label(simiN, text=" Articulos Combinados: 3-4 al 3-6 ").pack(side=tk.TOP)
    label=tk.Label(simiN, text=niv3).pack(side=tk.TOP)
    label=tk.Label(simiN, text=" Articulos Combinados: 4-5 al 4-6 ").pack(side=tk.TOP)
    label=tk.Label(simiN, text=niv4).pack(side=tk.TOP)
    label=tk.Label(simiN, text=" Articulos Combinados: 5-6 ").pack(side=tk.TOP)
    label=tk.Label(simiN, text=niv5).pack(side=tk.TOP)
    Button = tk.Button(simiN, command=mostrar_titulo_NS(archiv), font=('Arial', 11, 'bold')).pack(side = tk.RIGHT)

def resultado2():
    # numero=1
    archiv=carga_arc.cargar_archivos()
    # art= int(entry2.get())
    niv_simi1=niv_simi.nivel_similitud(1, 3, archiv) # Toca modificar el numero 2 para que realice con respecto al resumen, objetivo, etc...
    niv1=niv_simi1[0]
    niv2=niv_simi1[1]
    niv3=niv_simi1[2]
    niv4=niv_simi1[3]
    niv5=niv_simi1[4]
    simiN=tk.Toplevel()
    simiN.title(" Nivel de Similitud Resultado ")
    simiN.geometry('600x250')
    label=tk.Label(simiN, text="").pack(side=tk.TOP)
    label=tk.Label(simiN, text=" Articulos Combinados: 1-2 al 1-6 ").pack(side=tk.TOP)
    label=tk.Label(simiN, text=niv1).pack(side=tk.TOP)
    label=tk.Label(simiN, text=" Articulos Combinados: 2-3 al 2-6 ").pack(side=tk.TOP)
    label=tk.Label(simiN, text=niv2).pack(side=tk.TOP)
    label=tk.Label(simiN, text=" Articulos Combinados: 3-4 al 3-6 ").pack(side=tk.TOP)
    label=tk.Label(simiN, text=niv3).pack(side=tk.TOP)
    label=tk.Label(simiN, text=" Articulos Combinados: 4-5 al 4-6 ").pack(side=tk.TOP)
    label=tk.Label(simiN, text=niv4).pack(side=tk.TOP)
    label=tk.Label(simiN, text=" Articulos Combinados: 5-6 ").pack(side=tk.TOP)
    label=tk.Label(simiN, text=niv5).pack(side=tk.TOP)
    Button = tk.Button(simiN, command=mostrar_titulo_NS(archiv), font=('Arial', 11, 'bold')).pack(side = tk.RIGHT)

def conclusion2():
    archiv=carga_arc.cargar_archivos()
    niv_simi1=niv_simi.nivel_similitud(1, 4, archiv) # Toca modificar el numero 2 para que realice con respecto al resumen, objetivo, etc...
    niv1=niv_simi1[0]
    niv2=niv_simi1[1]
    niv3=niv_simi1[2]
    niv4=niv_simi1[3]
    niv5=niv_simi1[4]
    simiN=tk.Toplevel()
    simiN.title(" Nivel de Similitud Conclusion ")
    simiN.geometry('600x250')
    label=tk.Label(simiN, text="").pack(side=tk.TOP)
    label=tk.Label(simiN, text=" Articulos Combinados: 1-2 al 1-6 ").pack(side=tk.TOP)
    label=tk.Label(simiN, text=niv1).pack(side=tk.TOP)
    label=tk.Label(simiN, text=" Articulos Combinados: 2-3 al 2-6 ").pack(side=tk.TOP)
    label=tk.Label(simiN, text=niv2).pack(side=tk.TOP)
    label=tk.Label(simiN, text=" Articulos Combinados: 3-4 al 3-6 ").pack(side=tk.TOP)
    label=tk.Label(simiN, text=niv3).pack(side=tk.TOP)
    label=tk.Label(simiN, text=" Articulos Combinados: 4-5 al 4-6 ").pack(side=tk.TOP)
    label=tk.Label(simiN, text=niv4).pack(side=tk.TOP)
    label=tk.Label(simiN, text=" Articulos Combinados: 5-6 ").pack(side=tk.TOP)
    label=tk.Label(simiN, text=niv5).pack(side=tk.TOP)
    Button = tk.Button(simiN, command=mostrar_titulo_NS(archiv), font=('Arial', 11, 'bold')).pack(side = tk.RIGHT)

# Función para mostrar los titulos de los articulos para el nivel de similitud
def mostrar_titulo_NS(archivos):
    titulos = tk.Toplevel()
    titulos.title(" Titulos de los Artículos ")
    titulos.geometry('510x400+300+250')
    label=tk.Label(titulos, text=" Articulo 1 = ").grid(row = 1, column = 2, padx = 20, pady = 20)
    label=tk.Label(titulos, text=archivos.Titulo.loc[0]).grid(row = 1, column = 3)
    label=tk.Label(titulos, text=" Articulo 2 = ").grid(row = 2, column = 2, padx = 20, pady = 20)
    label=tk.Label(titulos, text=archivos.Titulo.loc[1]).grid(row = 2, column = 3)
    label=tk.Label(titulos, text=" Articulo 3 = ").grid(row = 3, column = 2, padx = 20, pady = 20)
    label=tk.Label(titulos, text=archivos.Titulo.loc[2]).grid(row = 3, column = 3)
    label=tk.Label(titulos, text=" Articulo 4 = ").grid(row = 4, column = 2, padx = 20, pady = 20)
    label=tk.Label(titulos, text=archivos.Titulo.loc[3]).grid(row = 4, column = 3)
    label=tk.Label(titulos, text=" Articulo 5 = ").grid(row = 5, column = 2, padx = 20, pady = 20)
    label=tk.Label(titulos, text=archivos.Titulo.loc[4]).grid(row = 5, column = 3)
    label=tk.Label(titulos, text=" Articulo 6 = ").grid(row = 6, column = 2, padx = 20, pady = 20)
    label=tk.Label(titulos, text=archivos.Titulo.loc[5]).grid(row = 6, column = 3)

# Se definira una funcionpara sacar los temas con el algoritmo LDA
def lda():
    archiv=carga_arc.cargar_archivos()
    temas=lda_modelo.lda(archiv)
    tema1=temas.temas.loc[0]
    # print(tema1) # Para imprimir los temas por separado a traves de consola    
    tema2=temas.temas.loc[1]
    tema3=temas.temas.loc[2]
    ldaventana=tk.Toplevel()
    ldaventana.title(" Modelado de Temas (LDA) ")
    ldaventana.geometry('1200x300')
    label=tk.Label(ldaventana, text="").pack(side=tk.TOP)
    label=tk.Label(ldaventana, text=" Tema 1 ").pack(side=tk.TOP)
    label=tk.Label(ldaventana, text=tema1).pack(side=tk.TOP)
    label=tk.Label(ldaventana, text=" Tema 2 ").pack(side=tk.TOP)
    label=tk.Label(ldaventana, text=tema2).pack(side=tk.TOP)
    label=tk.Label(ldaventana, text=" Tema 3 ").pack(side=tk.TOP)
    label=tk.Label(ldaventana, text=tema3).pack(side=tk.TOP)
    label=tk.Label(ldaventana, text="").pack(side=tk.TOP)
    label=tk.Label(ldaventana, text="      ¿Como interpretarlo?      ").pack()
    label=tk.Label(ldaventana, text="  Las palabras que aparecen significan que son palabras clave las cuales son principales y estas contribuyen al tema como tal.  ").pack()
    label=tk.Label(ldaventana, text="  Los numeros decimales que aparecen antes de cada palabra significan los pesos de esas palabras en cada tema.  ").pack()
    label=tk.Label(ldaventana, text="  Esto quiere decir que los pesos reflejan la importancia de una palabra clave para el tema como tal.  ").pack()

# Definimos la funcion para realizar el grafo con los 2 sustantivos mas comunes de cada documento
def graphs_of_science():
    archiv = carga_arc.carga_individual()
    grafo = graphs_load.graphs(archiv)
    graph_science(grafo)

# Imagen para Frecuencia de Palabras
imgf = Image.open("img\pf.jpg")
imgf = imgf.resize((180,160), Image.ANTIALIAS)
imgf = ImageTk.PhotoImage(imgf)
label_1 = tk.Label(root, image=imgf)
canvas1.create_window(250,150, window = label_1)

# Boton para realizar la frecuencia de palabras
button1 = tk.Button (root, text=' Frecuencia de Palabras ',command=proceso_frecpab, font=('Arial', 11, 'bold'))
canvas1.create_window(250, 280, window=button1)

# Imagen para Padre Sintactico
imgp = Image.open("img\padsin.jpg")
imp = imgp.resize((660,160), Image.ANTIALIAS)
imgp = ImageTk.PhotoImage(imgp)
label_2 = tk.Label(root, image=imgp)
canvas1.create_window(750,150, window = label_2)

# Boton para realizar Padre Sintactico
button1 = tk.Button (root, text=' Padre Sintactico ',command=padre_sintac, font=('Arial', 11, 'bold'))
canvas1.create_window(750, 275, window=button1)

# Imagen para Nivel de Similitud
imgs = Image.open("img\simi.png")
imgs = imgs.resize((180,160), Image.ANTIALIAS)
imgs = ImageTk.PhotoImage(imgs)
label_3 = tk.Label(root, image=imgs)
canvas1.create_window(250,450, window = label_3)

# Boton para realizar el Nivel de Similitud
button1 = tk.Button (root, text=' Nivel de Similitud ',command=nivel_simi, font=('Arial', 11, 'bold'))
canvas1.create_window(250, 570, window=button1)

# Imagen para LDA
imgld = Image.open("img\lda.jpg")
imgld = imgld.resize((180,160), Image.ANTIALIAS)
imgld = ImageTk.PhotoImage(imgld)
label_4 = tk.Label(root, image=imgld)
canvas1.create_window(750,450, window = label_4)

# Boton para realizar LDA
button1 = tk.Button (root, text=' Temas Globales ',command=lda, font=('Arial', 11, 'bold'))
canvas1.create_window(750, 570, window=button1)

# Imagen para graphs_of_science
imggs = Image.open("img\grafo.png")
imggs = imggs.resize((180,160), Image.ANTIALIAS)
imggs = ImageTk.PhotoImage(imggs)
label_5 = tk.Label(root, image=imggs)
canvas1.create_window(500,300, window = label_5)

# Boton para realizar graphs_of_science
button1 = tk.Button (root, text = ' Graphs Of Science ', command = graphs_of_science, font = ('Arial', 11, 'bold'))
canvas1.create_window(500, 420, window = button1)
 
root.mainloop()