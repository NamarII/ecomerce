# -*- coding: utf-8 -*-

from db import dba
import base64

class Producto():
    def __init__(self,marca,modelo,proveedor,cantidad):
        self.__ids=0
        self.__producto=producto
        self.__marca=marca
        self.__modelo=modelo
        self.__proveedor=proveedor
        self.__cantidad=cantidad
        
    def get_producto(self):
        return self.__producto
    
    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def get_proveedor(self):
        return self.__proveedor
    
    def get_cantidad(self):
        return self.__cantidad
    
    def set_producto(self,producto):
        self.__producto=producto
        
    def set_marca(self,marca):
        self.__marca=marca
    
    def set_modelo(self,modelo):
        self.__modelo=modelo
    
    def set_proveedor(self,proveedor):
        self.__proveedor=proveedor
        
    def set_cantidad(self,cantidad):
        self.__cantidad=cantidad
        
    def get_id(self):
        return self.__ids
    
    def set_id(self,ids):
        self.__ids=ids
    
    def save(self):
        sql=' insert into producto (producto, marca, modelo, proveedor, cantidad) values(%s,%s,%s,%s, %s)'
        val=(self.__producto, self.__marca,self.__modelo,self.__proveedor, self.__cantidad)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)
    
    def delete(self):
        sql='delete from producto where ID_producto=%s'
        val=(self.get_id(),)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
    
    def update_marca(self,marca):
        sql='update producto set marca=%s where ID_producto=%s '
        val=(marca,self.__ids)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
    
    def update_modelo(self,modelo):
        sql='update producto set modelo=%s where ID_producto=%s '
        val=(modelo,self.__ids)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
    
    def update_proveedor(self,proveedor):
        sql='update producto set proveedor=%s where ID_producto=%s '
        val=(proveedor,self.__ids)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        
    def update_cantidad(self,cantidad):
        sql='update producto set cantidad=%s where ID_producto=%s '
        val=(cantidad,self.__ids)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        
    
        
        
        



    


        
