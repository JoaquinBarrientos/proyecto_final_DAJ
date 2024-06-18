"test and see the structure of the data"

import pandas as pd

path= r'files_dump\raw_data\yellow_tripdata_2023-01.parquet'

df = pd.read_parquet(path)
print(df.dtypes)
print(df.head(5))