# -*- coding: utf-8 -*-

from db import dba
import validate_email
import base64

class Validator():
    
    def __init__(self):
        pass
            
        """if errores=={}:
            sql='select ID_celular from usuario where numero=%s'
            val=(datosFinales['numero'],)
            dba.get_cursor().execute(sql,val)
            result=dba.get_cursor().fetchone()
            if result is not None:
                errores['numero']='El numero existe en el sistema'
                return errores
        return errores"""
    
    def validar_usuario(self,dicc):
        datosFinales={}
        errores={}
        caracteresEspeciales=['$','@','#','%']
        
        #Elimino espacios entre caracteres        
        for x,y in dicc.items():
            datosFinales[x]=y.strip()
            
        #Si dejo vacio algún campo se completa en la lista de errores
        if datosFinales['ids']=='':
            errores['ids']='Campo id vacio'
        
        if datosFinales['nombre']=='':
            errores['nombre']='Campo nombre vacio'
            
        if datosFinales['apellido']=='':
            errores['apellido']='Campo apellido vacio'
            
        if datosFinales['domicilio']=='':
            errores['domicilio']='Campo domicilio vacio'
            
        if datosFinales['DNI']=='':
            errores['DNI']='Campo DNI vacio'
            
        if datosFinales['Fecha_nac']=='':
            errores['Fecha_nac']='Campo Fecha_nac vacio'
            
        if datosFinales['mail']=='':
            errores['mail']='Campo mail vacio'
            
        elif validate_email(datosFinales['mail'])==False:
            errores['mail']='No tiene formato de mail'
        
        if datosFinales['password']=='':
            errores['password']='Campo password vacio'
        
        #compruebo que la contraseña tenga la longitud adecuada, al menos 1 mayúscula, minúscula y caracter especial.
       #y que coincida con su confirmacón de password
        elif len(datosFinales['password'])<6:
            errores['password']='La password debe tener al menos 6 caracteres'
        elif not any(i.isupper() for i in datosFinales['password']):
            errores['password']='La password debe tener al menos 1 caracter con mayuscula'
        elif not any(i.islower() for i in datosFinales['password']):
            errores['password']='La password debe tener al menos 1 caracter con minuscula'
        elif not any(i in caracteresEspeciales  for i in datosFinales['password']):
            errores['password']='La password debe tener al menos 1 caracter con especial'
        elif datosFinales['password']!=datosFinales['cpassword']:
            errores['password']='la password no coincide'
            
    def validar_login(self,dicc):
        
        datosFinales={}
        errores={}
        
        #Elimino espacios entre caracteres
        for x,y in dicc.items():
            datosFinales[x]=y.strip()
        
        sql="select password from usuario where mail=%s"
        val=(datosFinales['mail'],)
        dba.get_cursor().execute(sql,val)
        
        result=dba.get_cursor().fetchone()
        
        print(base64.decodebytes(result[0].encode("UTF-8")).decode('utf-8'))
        
        if result is None:
            errores['mail']="el mail ingresado no existe en la base"
            return errores
        
        if base64.decodebytes(result[0].encode("UTF-8")).decode('utf-8')==datosFinales['password']:
            return result
        else:
            errores['password']="la password es incorrecta"
            return errores

val=Validator()
        
        
            
        
            