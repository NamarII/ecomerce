# -*- coding: utf-8 -*-

from validator import val 
from producto import Producto
from usuario import Usuario
from dataclasses import asdict
import logging

def registracion_usuario():
    i=False
    while not i==True:
        usuario={}
        usuario['nombre']=input('ingrese nombre\n')
        usuario['apellido']=input('ingrese apellido\n')
        usuario['domicilio']=input('ingrese domicilio\n')
        usuario['dni']=input('ingrese DNI\n')
        usuario['Fecha_nac']=input('ingrese fecha de nacimiento\n')
        usuario['mail']=input('ingrese mail\n')
        usuario['password']=input('ingrese password\n')
        usuario['cpassword']=input('ingrese de nuevo la password\n')
        errores=val.validar_usuario(usuario)
        if not errores:
            del usuario['cpassword']
            usuario1=Usuario(**usuario)
            usuario1.save()
            print('su usuario se agrego exitosamente')
            return usuario1
        for i in errores.values():
            print(i)
            
def menu_usuario_update():
    print(' Elija las siguientes opciones \n')
    print(' Opcion 1: Modificar el nombre \n')
    print(' Opcion 2: Modificar el apellido \n')
    print(' Opcion 3: Modificar el domicilio \n')
    print(' Opcion 4: Modificar el DNI \n')
    print(' Opcion 5:Modificar la fecha de nacimiento \n')
    print(' Opcion 6:Modificar el email \n')
    print(' Opcion 7:Modificar la password \n')
    print(' Opcion 8: Eliminar el usuario del sistema \n')
    print(' Opcion 9:Volver al menu principal \n')
    opcion=int(input ("ingrese la opcion"))
    if opcion==1:
        nombre=input("ingrese el nombre")
        usuario.update_nombre(nombre)
        print("se modifico correctamente el nombre")
    elif opcion==2:
        apellido=input("ingrese el apellido")
        usuario.update_apellido(apellido)
        print("se modifico correctamente el apellido")
    elif opcion==3:
        domicilio=int(input("ingrese el domicilio"))
        usuario.update_domicilio(domicilio)
        print("se modifico correctamente el domicilio")
    elif opcion==4:
        dni=int(input("ingrese el DNI"))
        usuario.update_DNI(DNI)
        print("se modifico correctamente el DNI")        
    elif opcion==5:
        Fecha_nac=int(input("ingrese la fecha de nacimiento"))
        usuario.update_Fecha_nac(Fecha_nac)
        print("se modifico correctamente la fecha de nacimiento")
    elif opcion==6:
        email=int(input("ingrese el e-mail"))
        usuario.update_email(email)
        print("se modifico correctamente el e-mail")
    elif opcion==7:
        password=int(input("ingrese la password"))
        usuario.update_password(password)
        print("se modifico correctamente el password")
    elif opcion==8:
        nombre=input("ingrese el nombre")
        apellido=input("ingrese el apellido")
        usuario.delete(Usuario)
        print("se eliminó exitosamente el usuario")
    else:
        menu()
        

def menu():
    print("Bienvenido a la aplicacion \n")
    print("Eliga las siguientes opciones \n")
    opcion=int(input("Opcion 1 Registracion  \n Opcion 2 Cierre aplicacion "))
    if opcion==1:
        usuario=registracion_usuario()
    print("Bienvenido a la registracion del usuario \n")
    
    else:
        quit()


login={}

login['nombre']=input('ingrese su nombre')
login['apellido']=input('ingrese su apellido')
login['domicilio']=input('ingrese su domicilio')
login['DNI']=input('ingrese su DNI')
login['Fecha_nac']=input('ingrese su fecha de nacimiento')
login['mail']=input('ingrese su email')
login['password']=input('ingrese su password')
print(val.validar_login(login))

def registro_producto():
  flag =False
  while not flag == True:
    datos = {}
    try:
      datos["nombre"]=input("Ingrese el nombre del producto\n")
      datos["marca"]=input("Ingrese el marca\n")
      datos["precio"]=float(input("Ingrese el precio\n"))
      datos["PrecioVenta"]=float(input("Ingrese el Precioventa\n"))
      datos["id_categoria"]=int(input("Ingrese el id_categoria\n"))
      datos["num_codigo"]=input("Ingrese el num_codigo\n")
      datos["id_proveedor"]=int(input("Ingrese el numero de ID del Proveedor\n"))

      errores=val.validar_producto(datos)
    except NameError:
      print("Error - registro_producto - Algo salió mal")
      print(NameError)
    except:
      print("Error - registro_producto - Revise los campos que son numericos y los que son texto")
    else:
      if not errores:
        art=producto(**datos)
        art.save()
        print('Se añadió un nuevo articulo a la DB')
        flag=True
        return art
        
      for error in errores.values():
        print(error)







