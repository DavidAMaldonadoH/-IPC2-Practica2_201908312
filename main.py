import os

from clases import *

def menuPrincipal():
   opciones = '''1. Ingresar un Contacto Nuevo
2. Buscar Contacto
3. Visualizar Agenda
4. Salir'''
   incio = True
   agenda = ListaDobleAgenda()

   while incio:
      print('Menu Principal'.center(80))
      print(opciones)
      try:
         opcion = int(input('Ingrese la opción que desee: '))
         if opcion == 1:#Agregar Contacto
            print('Agregar Contacto'.center(80))
            nombre = input('Ingrese Nombre: ')
            apellido = input('Ingrese Apellido: ')
            telefono = int(input('Ingrese el Telefono: '))
            existe = agenda.buscar(telefono)
            if existe == None:
               contacto = NodoContacto(telefono, nombre, apellido)
               agenda.add(contacto)
               print('\nContacto agregado exitosamente\n')
            else:
               print('\n> El contacto ya existe.')
         elif opcion == 2:#Buscar Contacto
            if agenda.getSize() != 0:
               try:
                  telefono = int(input('Ingrese el número que deseea buscar: '))
                  contacto = agenda.buscar(telefono)
                  if contacto != None:
                     print('Contacto Seleccionado'.center(80))
                     print(f'Nombre: {contacto.getNombre()}')
                     print(f'Apellido: {contacto.getApellido()}')
                     print(f'Teléfono: {contacto.getTelefono()}')
                  else:
                     try:
                        print('\nEl número de teléfono no existe, ¿Desea Agregarlo?\n')
                        print('1. Si')
                        print('2. No')
                        entrada = int(input())
                        if entrada == 1:
                           print('Agregar Contacto'.center(80))
                           nombre = input('Ingrese Nombre: ')
                           apellido = input('Ingrese Apellido: ')
                           contacto = NodoContacto(telefono, nombre, apellido)
                           agenda.add(contacto)
                           print('\nContacto agregado exitosamente\n')
                        elif entrada == 2:
                           continue
                        else:
                           raise ValueError
                     except ValueError:
                        print('\n> El numero ingresado no es valido')
               except ValueError:
                  print('\n> El numero ingresado no es valido')
         elif opcion == 3:#Visualizar Agenda
            #abrir un archivo en forma de escritura
            f = open('archivo.dot', 'w',encoding='utf-8')
            #escribir en dot 
            f.write("digraph agenda {\n")
            f.write('bgcolor = "#caf0f8";\nfontcolor = "#03045e";\nlabelloc=t;\nlabel = "Agenda";\nedge[color="#03045e"];')
            f.write('\nfontname = "Arial";\nfontsize = "24.0";')
            f.write('\nnode[shape="rect" color="#03045e" fillcolor="#48cae4" style="filled"]')
            for i in range(agenda.getSize()):
               if i == 0:
                  f.write(f'\nnodo{i} -> nodo{i+1}')
                  f.write(f'\nnodo{i}[label="Nombre: {agenda.get(i).nombre}\\nApellido: {agenda.get(i).apellido}\\nTeléfono: {agenda.get(i).telefono}"]')
               elif i == agenda.getSize()-1:
                  f.write(f'\nnodo{i} -> nodo{i-1}')
                  f.write(f'\nnodo{i}[label="Nombre: {agenda.get(i).nombre}\\nApellido: {agenda.get(i).apellido}\\nTeléfono: {agenda.get(i).telefono}"]')
               else:
                  f.write(f'\nnodo{i} -> nodo{i+1}')
                  f.write(f'\nnodo{i} -> nodo{i-1}')
                  f.write(f'\nnodo{i}[label="Nombre: {agenda.get(i).nombre}\\nApellido: {agenda.get(i).apellido}\\nTeléfono: {agenda.get(i).telefono}"]')
            f.write('\n}')
            f.close()
            os.system(f"dot -Nfontname=Arial -Tpdf archivo.dot -o agenda.pdf")
            print('\n> Agenda generada exitosamente\n')
         elif opcion == 4:#Salir
            incio = False
            os.system('cls')
         else:
            raise ValueError
      except ValueError:
         print('\n> La opcion ingresada no es valida.')

if __name__ == "__main__":
   menuPrincipal()