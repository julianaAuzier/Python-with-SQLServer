import pyodbc
import pandas as pd
pd.set_option('display.max_columns',1000)

data_conx = (
    'Driver={SQL Server};'
    'Server=DESKTOP-******\SQLEXPRESS;'
    'Database=AdventureWorks2017;'
    'Trusted_connection=yes;'
)

conx = pyodbc.connect(data_conx)
#print('connected!')

cursor = conx.cursor()
query = """select * from Person.Address where PostalCode like 98011"""
#print(cursor.execute(query).fetchall())

cursor.execute(query)

AddressID, AddressLine1, AddressLine2, City, StateProvinceID, PostalCode, SpatialLocation, rowguid, ModifiedDate = zip(*cursor.fetchall())

df = pd.concat([pd.DataFrame(k) for k in [AddressID, AddressLine1, AddressLine2, City, StateProvinceID, PostalCode, SpatialLocation, rowguid, ModifiedDate]], axis=1, ignore_index=True)
df.columns = [k for k in 'AddressID, AddressLine1, AddressLine2, City, StateProvinceID, PostalCode, SpatialLocation, rowguid, ModifiedDate'.split(', ')]
print(df)

