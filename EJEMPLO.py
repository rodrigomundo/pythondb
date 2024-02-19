#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.path.append(r"C:\Users\rodri\Documents\GitHub\pythondb")

from LIBRERIACLASE import clasesilla
from LIBRERIACLASE import fruta

SERVER = 'LAPTOP-0DFDCEIG'
DATABASE = 'AdventureWorksLT2019'
USERNAME = 'rod'
PASSWORD = 'Borges2017'
chicho = ('https://www.fruityvice.com/api/fruit/all')
#objeto = clasesilla(SERVER, DATABASE, USERNAME, PASSWORD)
#valores = (4, 5)
#resultado3 = objeto.recivalores ("EXECUTE [dbo].[un_storprosellur] ?, ?", valores)
#resultado2 = objeto.micursorcito ("SELECT ProductID, Name, Culture FROM SalesLT.vProductAndDescription")
#for x in resultado3:
#           print (x[0], "-", x[1], "-", x[2], "-", x[4], "-", x[5])
#for x in resultado2:
#           print (x[0], "-", x[1])
#objeto.micursorcito ("SELECT * FROM SalesLT.vGetAllCategories")

#objeto2 = clasesilla(SERVER, 'MUSIKA', USERNAME, PASSWORD)
#valores2 = ('Hammer smashed face', 2)
#resultado4 = objeto2.insertar ("EXEC [dbo].[CreaRola] ?, ?", valores2)

lainstancia = fruta()
respuesta = lainstancia.getapi(chicho)
respuesta = respuesta.rename(columns={'name': 'nombre'})
respuesta = respuesta.rename(columns={'family': 'familia'})
print (respuesta)
respuesta2 = lainstancia.putapi(chicho, {
    "genus": "Fragari",
    "name": "Strawberri",
    "family": "Rosacea",
    "order": "Rosale",
    "nutritions": {
        "carbohydrates": 5.2,
        "protein": 1,
        "fat": 0.7,
        "calories": 28,
        "sugar": 5.4
    }
})
print (respuesta2)


# In[ ]:




