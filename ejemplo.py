# Autor: kewapo
import os.path
import datetime

ruta = r'E:\libros'


def guardar_archivos(ruta, nombre_fichero):
    print('Leyendo archivos del directorio ' + ruta + ' ...')
    with open(nombre_fichero, 'w', encoding='latin_1', errors='ignore') as archivo:
        archivo.write('Directorio;Nombre;Tamaño;Fecha de creación\n')
        for root, directorios, ficheros in os.walk(ruta):
            for fichero in ficheros:
                if str(fichero).startswith('.'): continue
                nombre = os.path.join(root, fichero)
                tamanio = os.stat(nombre).st_size
                fecha = datetime.datetime.fromtimestamp(os.stat(nombre).st_ctime)
                archivo.write('' + root + ';' + fichero + ';' + str(tamanio) + ';' + str(fecha))
                archivo.write('\n')
    print('Escribiendo datos en ' + nombre_fichero)


def leer_archivos(nombre_fichero):
    archivos = set()
    with open(nombre_fichero) as archivo:
        for linea in archivo:
            directorio = linea.split(';')[0]
            nombre = linea.split(';')[1]
            archivos.add(os.path.join(directorio, nombre))
    return archivos

'''
He añadido un archivo nuevo a uno de los directorios
Debería immprimirse con este código
'''
if __name__ == '__main__':
    archivos = leer_archivos('archivos.csv')
    guardar_archivos(r'E:\libros', 'archivos1.csv')
    with open('archivos1.csv') as a:
        for linea in a:
            directorio = linea.split(';')[0]
            nombre = linea.split(';')[1]
            todo = os.path.join(directorio, nombre)
            if todo not in archivos:
                print(todo)
