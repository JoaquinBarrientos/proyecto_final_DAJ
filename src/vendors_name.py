import pandas as pd

# Crear un DataFrame con las correspondencias
data_categoria = {
    'vendorid': [1, 2, 6],
    'vendorname': ['Creative Mobile Technologies, LLC', 'VeriFone Inc', 'Unknow']
}
df_categoria = pd.DataFrame(data_categoria)

# Guardar como CSV
df_categoria.to_csv('vendorstable.csv', index=False)
