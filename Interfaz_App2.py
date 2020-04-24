import tkinter as tk, nltk, numpy as np, gensim
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure
from gensim import corpora, models #Para construir una matriz de términos de documento
from Cargar_Archivos import Cargar
from Frecuencia_Palabras import Frec_Pab
from Padre_Sintactico import Padre_Sintactico
from Nivel_Similitud import Nivel_Similitud
from LDA import LDA

carga_arc=Cargar()
frec_pab=Frec_Pab()
pad_sintac=Padre_Sintactico()
niv_simi=Nivel_Similitud()
lda_modelo = LDA()
 
root= tk.Tk()
root.title("  PROTOTIPO INTERFAZ TRABAJO DE GRADO  ")

# Canvas para graficar figuras, imagenes, etc
canvas1 = tk.Canvas(root, width = 600, height = 300)
canvas1.pack(side=tk.LEFT)

# Funcion donde se realiza el proceso para la frecuencia de palabras
def proceso_frecpab():
    global bar1

    numero = int(6)
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
    subplot1.bar(xArt1,yArt1, align='center') # Graficamos la frecuencia de palabras en un diagrama de barras
    # subplot1.title(' Art1 ', fontsize=12)
    
    subplot1 = figure1.add_subplot(322) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt2 = frecuencia.palabras.loc[1]
    xArt2 = frecuencia.frecuencia.loc[1]
    subplot1.bar(xArt2,yArt2, align='center') # Graficamos la frecuencia de palabras en un diagrama de barras
    # subplot1.title(' Art2 ', fontsize=12)

    subplot1 = figure1.add_subplot(323) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt3 = frecuencia.palabras.loc[2]
    xArt3 = frecuencia.frecuencia.loc[2]
    subplot1.bar(xArt3,yArt3, align='center') # Graficamos la frecuencia de palabras en un diagrama de barras
    # subplot1.title(' Art3 ', fontsize=12)

    subplot1 = figure1.add_subplot(324) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt4 = frecuencia.palabras.loc[3]
    xArt4 = frecuencia.frecuencia.loc[3]
    subplot1.bar(xArt4,yArt4, align='center') # Graficamos la frecuencia de palabras en un diagrama de barras
    # subplot1.title(' Art4 ', fontsize=12)

    subplot1 = figure1.add_subplot(325) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt5 = frecuencia.palabras.loc[4]
    xArt5 = frecuencia.frecuencia.loc[4]
    subplot1.bar(xArt5,yArt5, align='center') # Graficamos la frecuencia de palabras en un diagrama de barras
    # subplot1.title(' Art5 ', fontsize=12)

    subplot1 = figure1.add_subplot(326) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt6 = frecuencia.palabras.loc[5]
    xArt6 = frecuencia.frecuencia.loc[5]
    subplot1.bar(xArt6,yArt6, align='center') # Graficamos la frecuencia de palabras en un diagrama de barras
    # subplot1.title(' Art6 ', fontsize=12)

    bar1 = FigureCanvasTkAgg(figure1, frecp) # Añadimos dicho grafico a la Interfaz grafica
    bar1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=0) # damos la posicion para que aparezca la grafica
    toolbar = NavigationToolbar2Tk(bar1, frecp)# barra de iconos para guardar o configurar el grafico
    toolbar.update()
    bar1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Funcion donde se realiza el proceso del padre sintactico
def padre_sintac():
    padS=tk.Toplevel()
    padS.title(" Padre Sintactico ")
    padS.geometry('400x400')
    # canvas2=tk.Canvas(padS, width=900, height=400)

    button1 = tk.Button (padS, text=' Objetivo ',command=objetivo, font=('Arial', 11, 'bold'))
    button1.place(x=150, y=150)
    # canvas2.create_window(100, 50, window=button1)

    button1 = tk.Button (padS, text=' Metodo ',command=metodo, font=('Arial', 11, 'bold'))
    button1.place(x=150, y=200)

    button1 = tk.Button (padS, text=' Resultados ',command=resultado, font=('Arial', 11, 'bold'))
    button1.place(x=150, y=250)

    button1 = tk.Button (padS, text=' Conclusion ',command=conclusion, font=('Arial', 11, 'bold'))
    button1.place(x=150, y=300)

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
    subplot1.bar(xArt1,yArt1, align='center') # Graficamos la frecuencia de padres en un diagrama de barras
    # subplot1.title(' Art1 ', fontsize=12)
    
    subplot1 = figure1.add_subplot(322) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt2 = pad_sintac1.padres.loc[1]
    xArt2 = pad_sintac1.frecuencia.loc[1]
    subplot1.bar(xArt2,yArt2, align='center') # Graficamos la frecuencia de padres en un diagrama de barras
    # subplot1.title(' Art2 ', fontsize=12)

    subplot1 = figure1.add_subplot(323) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt3 = pad_sintac1.padres.loc[2]
    xArt3 = pad_sintac1.frecuencia.loc[2]
    subplot1.bar(xArt3,yArt3, align='center') # Graficamos la frecuencia de padres en un diagrama de barras
    # subplot1.title(' Art3 ', fontsize=12)

    subplot1 = figure1.add_subplot(324) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt4 = pad_sintac1.padres.loc[3]
    xArt4 = pad_sintac1.frecuencia.loc[3]
    subplot1.bar(xArt4,yArt4, align='center') # Graficamos la frecuencia de padres en un diagrama de barras
    # subplot1.title(' Art4 ', fontsize=12)

    subplot1 = figure1.add_subplot(325) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt5 = pad_sintac1.padres.loc[4]
    xArt5 = pad_sintac1.frecuencia.loc[4]
    subplot1.bar(xArt5,yArt5, align='center') # Graficamos la frecuencia de padres en un diagrama de barras
    # subplot1.title(' Art5 ', fontsize=12)

    subplot1 = figure1.add_subplot(326) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt6 = pad_sintac1.padres.loc[5]
    xArt6 = pad_sintac1.frecuencia.loc[5]
    subplot1.bar(xArt6,yArt6, align='center') # Graficamos la frecuencia de padres en un diagrama de barras
    # subplot1.title(' Art6 ', fontsize=12)

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
    subplot1.bar(xArt1,yArt1, align='center') # Graficamos la frecuencia de padres en un diagrama de barras
    # subplot1.title(' Art1 ', fontsize=12)
    
    subplot1 = figure1.add_subplot(322) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt2 = pad_sintac1.padres.loc[1]
    xArt2 = pad_sintac1.frecuencia.loc[1]
    subplot1.bar(xArt2,yArt2, align='center') # Graficamos la frecuencia de padres en un diagrama de barras
    # subplot1.title(' Art2 ', fontsize=12)

    subplot1 = figure1.add_subplot(323) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt3 = pad_sintac1.padres.loc[2]
    xArt3 = pad_sintac1.frecuencia.loc[2]
    subplot1.bar(xArt3,yArt3, align='center') # Graficamos la frecuencia de padres en un diagrama de barras
    # subplot1.title(' Art3 ', fontsize=12)

    subplot1 = figure1.add_subplot(324) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt4 = pad_sintac1.padres.loc[3]
    xArt4 = pad_sintac1.frecuencia.loc[3]
    subplot1.bar(xArt4,yArt4, align='center') # Graficamos la frecuencia de padres en un diagrama de barras
    # subplot1.title(' Art4 ', fontsize=12)

    subplot1 = figure1.add_subplot(325) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt5 = pad_sintac1.padres.loc[4]
    xArt5 = pad_sintac1.frecuencia.loc[4]
    subplot1.bar(xArt5,yArt5, align='center') # Graficamos la frecuencia de padres en un diagrama de barras
    # subplot1.title(' Art5 ', fontsize=12)

    subplot1 = figure1.add_subplot(326) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt6 = pad_sintac1.padres.loc[5]
    xArt6 = pad_sintac1.frecuencia.loc[5]
    subplot1.bar(xArt6,yArt6, align='center') # Graficamos la frecuencia de padres en un diagrama de barras
    # subplot1.title(' Art6 ', fontsize=12)

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
    subplot1.bar(xArt1,yArt1, align='center') # Graficamos la frecuencia de padres en un diagrama de barras
    # subplot1.title(' Art1 ', fontsize=12)
    
    subplot1 = figure1.add_subplot(322) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt2 = pad_sintac1.padres.loc[1]
    xArt2 = pad_sintac1.frecuencia.loc[1]
    subplot1.bar(xArt2,yArt2, align='center') # Graficamos la frecuencia de padres en un diagrama de barras
    # subplot1.title(' Art2 ', fontsize=12)

    subplot1 = figure1.add_subplot(323) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt3 = pad_sintac1.padres.loc[2]
    xArt3 = pad_sintac1.frecuencia.loc[2]
    subplot1.bar(xArt3,yArt3, align='center') # Graficamos la frecuencia de padres en un diagrama de barras
    # subplot1.title(' Art3 ', fontsize=12)

    subplot1 = figure1.add_subplot(324) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt4 = pad_sintac1.padres.loc[3]
    xArt4 = pad_sintac1.frecuencia.loc[3]
    subplot1.bar(xArt4,yArt4, align='center') # Graficamos la frecuencia de padres en un diagrama de barras
    # subplot1.title(' Art4 ', fontsize=12)

    subplot1 = figure1.add_subplot(325) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt5 = pad_sintac1.padres.loc[4]
    xArt5 = pad_sintac1.frecuencia.loc[4]
    subplot1.bar(xArt5,yArt5, align='center') # Graficamos la frecuencia de padres en un diagrama de barras
    # subplot1.title(' Art5 ', fontsize=12)

    subplot1 = figure1.add_subplot(326) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt6 = pad_sintac1.padres.loc[5]
    xArt6 = pad_sintac1.frecuencia.loc[5]
    subplot1.bar(xArt6,yArt6, align='center') # Graficamos la frecuencia de padres en un diagrama de barras
    # subplot1.title(' Art6 ', fontsize=12)

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
    subplot1.bar(xArt1,yArt1, align='center') # Graficamos la frecuencia de padres en un diagrama de barras
    # subplot1.title(' Art1 ', fontsize=12)
    
    subplot1 = figure1.add_subplot(322) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt2 = pad_sintac1.padres.loc[1]
    xArt2 = pad_sintac1.frecuencia.loc[1]
    subplot1.bar(xArt2,yArt2, align='center') # Graficamos la frecuencia de padres en un diagrama de barras
    # subplot1.title(' Art2 ', fontsize=12)

    subplot1 = figure1.add_subplot(323) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt3 = pad_sintac1.padres.loc[2]
    xArt3 = pad_sintac1.frecuencia.loc[2]
    subplot1.bar(xArt3,yArt3, align='center') # Graficamos la frecuencia de padres en un diagrama de barras
    # subplot1.title(' Art3 ', fontsize=12)

    subplot1 = figure1.add_subplot(324) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt4 = pad_sintac1.padres.loc[3]
    xArt4 = pad_sintac1.frecuencia.loc[3]
    subplot1.bar(xArt4,yArt4, align='center') # Graficamos la frecuencia de padres en un diagrama de barras
    # subplot1.title(' Art4 ', fontsize=12)

    subplot1 = figure1.add_subplot(325) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt5 = pad_sintac1.padres.loc[4]
    xArt5 = pad_sintac1.frecuencia.loc[4]
    subplot1.bar(xArt5,yArt5, align='center') # Graficamos la frecuencia de padres en un diagrama de barras
    # subplot1.title(' Art5 ', fontsize=12)

    subplot1 = figure1.add_subplot(326) # Se añade un subplot para el matplotlib donde se graficara dicha frecuencia
    yArt6 = pad_sintac1.padres.loc[5]
    xArt6 = pad_sintac1.frecuencia.loc[5]
    subplot1.bar(xArt6,yArt6, align='center') # Graficamos la frecuencia de padres en un diagrama de barras
    # subplot1.title(' Art6 ', fontsize=12)

    bar1 = FigureCanvasTkAgg(figure1, padS) # Añadimos dicho grafico a la Interfaz grafica
    bar1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=0) # damos la posicion para que aparezca la grafica
    toolbar = NavigationToolbar2Tk(bar1, padS)# barra de iconos para guardar o configurar el grafico
    toolbar.update()
    bar1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Funcion para el Nivel de Silimitud
def nivel_simi():
    simiN=tk.Toplevel()
    simiN.title(" Nivel de Similitud ")
    simiN.geometry('400x400')
    # canvas2=tk.Canvas(simiN, width=900, height=400)

    button1 = tk.Button (simiN, text=' Objetivo ',command=objetivo2, font=('Arial', 11, 'bold'))
    button1.place(x=150, y=150)
    # canvas2.create_window(100, 50, window=button1)

    button1 = tk.Button (simiN, text=' Metodo ',command=metodo2, font=('Arial', 11, 'bold'))
    button1.place(x=150, y=200)

    button1 = tk.Button (simiN, text=' Resultados ',command=resultado2, font=('Arial', 11, 'bold'))
    button1.place(x=150, y=250)

    button1 = tk.Button (simiN, text=' Conclusion ',command=conclusion2, font=('Arial', 11, 'bold'))
    button1.place(x=150, y=300)

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

# Boton para realizar la frecuencia de palabras
button1 = tk.Button (root, text=' Frecuencia de Palabras ',command=proceso_frecpab, font=('Arial', 11, 'bold'))
canvas1.create_window(150, 50, window=button1)

# Boton para realizar la frecuencia de palabras
button1 = tk.Button (root, text=' Padre Sintactico ',command=padre_sintac, font=('Arial', 11, 'bold'))
canvas1.create_window(350, 50, window=button1)

# Boton para realizar el Nivel de Similitud
button1 = tk.Button (root, text=' Nivel de Similitud ',command=nivel_simi, font=('Arial', 11, 'bold'))
canvas1.create_window(150, 100, window=button1)

# Boton para realizar LDA
button1 = tk.Button (root, text=' Temas Globales ',command=lda, font=('Arial', 11, 'bold'))
canvas1.create_window(350, 100, window=button1)
 
root.mainloop()