#Prueba 3 Nayibe Noguera
import json
import os

ruta_json='biblioteca.json'
ruta_reportes='Reportes_biblioteca_mundo_libro.json'

def crear_autor(ruta_json):
    buscar_autor(ruta_json)
    id=input('Ingrese ID: ')
    name=input('Ingrese nombre: ')
    nac=input('Ingrese Nacionalidad: ')
    nuevo_autor:[
        {
            "AutorID": id,
            "Nombre": name,
            "Nacionalidad": nac
        },]
    autores.append(nuevo_autor)
    return json.dump(buscar_autor(ruta_json))
nuevo_autor=crear_autor(ruta_json)
#print(nuevo_autor)

def buscar_autor(ruta_json):
    with open(ruta_json, 'r', encoding='utf-8') as lista:
        biblioteca = json.load(lista)
        return biblioteca['Autor']       
autores= buscar_autor(ruta_json)      
#print(autores)
def eliminar_autor():
    buscar_autor(ruta_json)
    id=input('Ingrese ID: ')
    name=input('Ingrese nombre: ')
    nac=input('Ingrese Nacionalidad: ')
    del_autor:[
        {
            "AutorID": id,
            "Nombre": name,
            "Nacionalidad": nac
        },]
    autores.pop(del_autor)
    return json.dump(buscar_autor(ruta_json))

def editar_autor():
    buscar_autor(ruta_json)
    id=input('Ingrese ID: ')
    name=input('Ingrese nombre: ')
    nac=input('Ingrese Nacionalidad: ')
    nuevos_datos:[
        {
            "Nombre": name,
            "Nacionalidad": nac
        },]
    autores.append(nuevos_datos)
    return json.dump(buscar_autor(ruta_json))

def menu_mantenedor():
    while True:
        try:
            print('-----------------------------')
            print('    Mantenedor de Autores    ')
            print('-----------------------------')
            print('[1]- Agregar Autor           ')
            print('[2]- Editar Autor            ')
            print('[3]- Eliminar Autor          ')
            print('[4]- Buscar Autor            ')
            print('[3]- Volver al menu principal')
            opcion=int(input('Ingrese una opcion:    '))
            if opcion == 1:
                crear_autor(ruta_json)
            elif opcion == 2:
                editar_autor()
            elif opcion ==3:
                eliminar_autor()
            elif opcion ==4:
                buscar_autor(ruta_json)
                print('Buscar Autor')
            elif opcion ==5:
                break
        except:
            print('Esta opcion no es valida, intente nuevamente')

def buscar_libro(ruta_json):
    with open(ruta_json, 'r', encoding='utf-8') as lista:
        biblioteca = json.load(lista)
        return biblioteca['Prestamo']       
libros_prestados= buscar_libro(ruta_json)

def reporte_libros_prestados():
    buscar_libro(ruta_json)
    with open(ruta_reportes, 'w') as prestamos:
        json.dump(prestamos)
        return[]

def menu_principal(): 
    while True:
        try:
            print('-----------------------------')
            print('  BIENVENIDO A MUNDO LIBROS  ')
            print('-----------------------------')
            print(' [1]- Mantenedor de Autores  ')
            print(' [2]- Reportes               ')
            print(' [3]- Salir                  ')
            opcion=int(input('Ingrese una opcion:  '))
            if opcion == 1:
                menu_mantenedor()
            elif opcion == 2:
                print('Genera un reporte')
            elif opcion ==3:
                print('Adios')
                break
        except:
            print('A ocurrido un error')


