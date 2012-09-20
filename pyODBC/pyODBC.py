'''
Created on Sep 3, 2012

@author: ealkl
'''
import pyodbc

server = '192.168.8.130'
database = 'exam2'
table = 'table5'
uid = 'testacc'
pwd = 'testacc'


# cnxn = pyodbc.connect('DSN=spnetwork51')

cnxn = pyodbc.connect('DRIVER={MySQL ODBC 5.1 Driver};SERVER=' + server + ';DATABASE=' + database + ';UID=' + uid + ';PWD=' + pwd)

cursor = cnxn.cursor()
                     
cursor.execute('select * from table5')
for row in cursor.fetchall():
    print row