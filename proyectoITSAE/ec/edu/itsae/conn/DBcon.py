# coding:utf-8
'''
Created on 27/1/2015

@author: Programacion
'''

from flaskext.mysql import MySQL#importar mysql
from flask import Flask#importar flask

class DBcon():
    '''
    classdocs
    '''
    pass

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def conexion(self):
        mysql = MySQL()#llamando a mysql
        app = Flask(__name__)#instanciando a flask
        app.config['MYSQL_DATABASE_USER'] = 'python'#nombre de usuario
        app.config['MYSQL_DATABASE_PASSWORD'] = '123456'#contrase�a de ususario
        app.config['MYSQL_DATABASE_DB'] = 'sisventas'#nombre de la base de datos
        app.config['MYSQL_DATABASE_HOST'] = 'localhost'#servidor donde se encuantra
        mysql.init_app(app)
        return mysql
