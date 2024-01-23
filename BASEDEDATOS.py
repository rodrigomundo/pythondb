#!/usr/bin/env python
# coding: utf-8

# In[20]:


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
    def micursorcito(self):
        query = "SELECT * FROM SalesLT.Customer"
        self.cursor.execute(query)
        
lavariablechingona=clasesilla()
lavariablechingona.micursorcito()
        


# In[ ]:





# In[ ]:




