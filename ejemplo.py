import os.path
import datetime
import csv

ruta = r'E:\libros'
with open('archivos.csv', 'w', encoding='latin_1', errors='ignore') as archivo:
    archivo.write('Directorio; Nombre;Tamaño;Fecha de creación\n')
    for root, directorios, ficheros in os.walk(ruta):
        for fichero in ficheros:
            if str(fichero).startswith('.'): continue
            nombre = os.path.join(root, fichero)
            tamanio = os.stat(nombre).st_size
            fecha = datetime.datetime.fromtimestamp(os.stat(nombre).st_ctime)
            print(nombre, tamanio, 'bytes. Creado en', fecha)
            archivo.write('' + root + ';' + fichero + ';' + str(tamanio) + ';' + str(fecha))
            archivo.write('\n')
