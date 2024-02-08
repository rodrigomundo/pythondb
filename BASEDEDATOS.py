#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.path.append(r"C:\Users\rodri\Documents\GitHub\pythondb")

from LIBRERIACLASE import clasesilla

SERVER = 'LAPTOP-0DFDCEIG'
DATABASE = 'AdventureWorksLT2019'
USERNAME = 'rod'
PASSWORD = 'Borges2017'
#objeto = clasesilla(SERVER, DATABASE, USERNAME, PASSWORD)
#valores = (4, 5)
#resultado3 = objeto.recivalores ("EXECUTE [dbo].[un_storprosellur] ?, ?", valores)
#resultado2 = objeto.micursorcito ("SELECT ProductID, Name, Culture FROM SalesLT.vProductAndDescription")
#for x in resultado3:
#           print (x[0], "-", x[1], "-", x[2], "-", x[4], "-", x[5])
#for x in resultado2:
#           print (x[0], "-", x[1])
#objeto.micursorcito ("SELECT * FROM SalesLT.vGetAllCategories")

objeto2 = clasesilla(SERVER, 'MUSIKA', USERNAME, PASSWORD)
valores2 = ('Hammer smashed face', 2)
resultado4 = objeto2.insertar ("EXEC [dbo].[CreaRola] ?, ?", valores2)


# In[ ]:




