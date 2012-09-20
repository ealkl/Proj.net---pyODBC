# -*- coding: uft-8 -*-
'''
Created on Sep 3, 2012

@author: ealkl
'''


import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=SQLSRV01;DATABASE=DATABASE;UID=USER;PWD=PASSWORD')
cursor = cnxn.cursor()

cursor.execute("SELECT WORK_ORDER.TYPE,WORK_ORDER.STATUS, WORK_ORDER.BASE_ID, WORK_ORDER.LOT_ID FROM WORK_ORDER")
for row in cursor.fetchall():
    print row









--------------
import pyodbc as p
import re #RegEx library

server = 'TWISEMAN-PC'
database = 'test'
table = 'salesData'
field = 'memo'

connStr = ( r'DRIVER={SQL Server};SERVER=' +
            server + ';DATABASE=' + database + ';' +
            'Trusted_Connection=yes'    )
        
#e-mail regex examples available at
#http://www.regular-expressions.info/email.html
pattern = r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b'
emailMatcher = re.compile(pattern, re.I)
emails = [] #create a list

conn = p.connect(connStr)
dbCursor = conn.cursor()
sql = ('select ' + field + ' as memo ' 
       ' from '+ table+
        ' where ' + field + ' like \'%@%\'') 
dbCursor = conn.cursor()
dbCursor.execute(sql)
for row in dbCursor:
    newEmails = emailMatcher.finditer(row.memo)
    if newEmails is not None:
        emails.extend([addr.group() for addr in newEmails])
        
conn.close()
print emails