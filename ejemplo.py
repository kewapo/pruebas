import os
import os.path
import datetime
ruta = r'E:\libros'
for root, directorios, ficheros in os.walk(ruta):
    for fichero in ficheros:
        if str(fichero).startswith('.'): continue
        fichero = os.path.join(root, fichero)
        tamanio = os.stat(fichero).st_size
        fecha = datetime.datetime.fromtimestamp(os.stat(fichero).st_ctime)
        print(fichero, tamanio, 'bytes. Creado en', fecha)