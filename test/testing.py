import os 
import polars as pl
import pandas as df

DIR_PATH ="files_dump/clean_data/"
dfs = []

for filename in os.listdir(DIR_PATH):
    if filename.endswith(".parquet"): #Suponiendo que los archivos son parquet
        file_path=os.path.join(DIR_PATH,filename)
        df= pl.read_parquet(file_path)
        dfs.append(df)

#concatenar todos los dataframes en uno solo
combined_df =pl.concat(dfs)

# mostrar el dataframe combinado
print(combined_df.shape)
print(combined_df.select(pl.col("vendorid").unique()))