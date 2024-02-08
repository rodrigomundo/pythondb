#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyodbc
class clasesilla:
    def __init__(self, SERVER, DATABASE, USERNAME, PASSWORD):
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
    def insertar (self, sql, vals):
        self.cursor.execute(sql, vals)
        self.cursor.commit()
        self.cursor.close()
        return 0
        
            


# In[ ]:




