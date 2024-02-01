#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyodbc
SERVER = 'LAPTOP-0DFDCEIG'
DATABASE = 'AdventureWorksLT2019'
USERNAME = 'rod'
PASSWORD = 'Borges2017'
class clasesilla:
    def __init__(self):
        connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}; Encrypt=no;TrustServerCertificate=yes'
        self.conn = pyodbc.connect(connectionString) 
        self.cursor = self.conn.cursor()
    def micursorcito(self, sqlstatement):
        #query = "SELECT ProductID, Name, Culture FROM SalesLT.vProductAndDescription"
        self.cursor.execute(sqlstatement)
        resultado = self.cursor.fetchall()
        return resultado
    def recivalores (self, sql, vals):
        self.cursor.execute(sql, vals)
        resultado = self.cursor.fetchall()
        return resultado
        
            
objeto = clasesilla()
valores = (4, 5)
resultado3 = objeto.recivalores ("EXECUTE [dbo].[un_storprosellur] ?, ?", valores)
resultado2 = objeto.micursorcito ("SELECT ProductID, Name, Culture FROM SalesLT.vProductAndDescription")
for x in resultado3:
            print (x[0], "-", x[1], "-", x[2], "-", x[4], "-", x[5])
for x in resultado2:
            print (x[0], "-", x[1])
objeto.micursorcito ("SELECT * FROM SalesLT.vGetAllCategories")


# In[ ]:




