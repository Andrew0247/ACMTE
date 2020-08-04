import easygui as eg
from os import scandir, getcwd

archivos = []
extension = ["*.txt"]

# ====== Clase para cargar los archivos ============
class Cargar():

    def cargar_archivos(self):
        directorio = eg.diropenbox(msg="Abrir directorio:",
                       title="Control: diropenbox",
                       default='')

        for archivo in self.ls(directorio):
            f=open(archivo,'r')
            texto=f.read()

            archivos.append(texto)

        return archivos

    def carga_individual(self):
        archivo = eg.fileopenbox(msg = "Abrir articulo a Graficar",
                    title = "Graphs: Articulo ",
                    default = '',
                    filetypes = ["*.txt"])

        f = open(archivo, 'r')
        texto = f.read()
        archivos.append(texto)

        return archivos

    def ls(self, ruta = getcwd()):
        return [arch.path for arch in scandir(ruta) if arch.is_file()]