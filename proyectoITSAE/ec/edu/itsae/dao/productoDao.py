# coding:utf-8
'''
Created on 27/1/2015

@author: Programacion
'''

from ec.edu.itsae.conn import DBcon
import json 


class ProductoDao(DBcon.DBcon):#heredando
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass#sirve cuando no hay implementacion en el metodo
    
    
    def reportarproducto(self):
        con=self.conexion().connect().cursor()  #capturando de la clase DBcon
        con.execute(" select * from producto ")
        reporte=con.fetchall()
        return reporte #despues del return no se debe colocar nada

    def insertarproducto(self, codigo, nombre, precio, proveedor,fechacrea,fechavenc):
        con=self.conexion().connect()
        sql= """insert into producto(codigo_producto, nombre_producto, precio_producto, proveedor, fecha_crea, fecha_venc)
                             values ('%s', '%s', '%s','%s', '%s', '%s')
                             """ %(codigo,nombre,precio,proveedor,fechacrea,fechavenc) 
        print #sql   Para imprimir nuestra consulta para poder ver        
        with con:
            cursor=con.cursor()
            cursor.execute(sql)#aqui debe estar sql para que se ejecute el insert
    
        #deber actualizar y eliminar
    def eliminarproducto(self,datoelim):
        con=self.conexion().connect()
        sql= """ delete from producto where id_producto= %i """ %int(datoelim)
        #print sql    Para imprimir nuestra consulta para poder ver        
        with con:
            cursor=con.cursor()
            cursor.execute(sql)#aqui debe estar sql para que se ejecute el insert
    
    def buscarproductoNombre(self, datobusca):
        con=self.conexion().connect().cursor()  #capturando de la clase DBcon
        con.execute(""" select CONCAT (nombre_producto) as value, id_producto as id from producto where upper(CONCAT (nombre_producto)) like upper('%s') """ %("%"+datobusca+"%") )
        reporte=con.fetchall()
        columna=('value', 'id')
        lista=[]
        #print con.execute
        for row in reporte:
            lista.append(dict(zip(columna,row))) #dict = diccionario, zip = para unir las las dos columnas
        return json.dumps(lista, indent=2) 
    
    def buscarproductoDato(self, datobuscado):
        con=self.conexion().connect().cursor() 
        sql=""" select * from producto where upper(CONCAT (nombre_producto)) like upper('%s') """ %("%"+datobuscado+"%")
        #print sql
        con.execute(sql)
        reporte=con.fetchall() 
        return reporte 
    
    
    '''
    def validarUsuario(self, usuario,clave):
        con=self.conexion().connect().cursor() 
        con.execute(""" select * from trabajador where usuario='%s' and clave='%s' """ %(usuario, clave))
        reporte=con.fetchall() 
        return reporte '''

    
    