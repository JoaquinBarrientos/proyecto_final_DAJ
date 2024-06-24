import pandas as pd

# Crear un DataFrame con las correspondencias
data_categoria = {
    'payment_type': [1, 2, 3, 4, 5, 6],
    'payment_info': ['Credit Card', 'Cash', 'No charge','Dispute','Unknown','Voided Trip']
}
df_categoria = pd.DataFrame(data_categoria)

# Guardar como CSV
df_categoria.to_csv('payment_info.csv', index=False)