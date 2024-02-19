#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pyodbc
import requests
import pandas as pd
import json
from pandas.io.json import json_normalize
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
    
class fruta:
    def getapi (self, apiurl):
        df = pd.read_json(apiurl)
        return df
    def putapi (self, apiurl, payload):
        posti = requests.put(apiurl, data=payload)


# In[ ]:




