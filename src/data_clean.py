import os
import pandas as pd
from tqdm import tqdm
from generals import DATA_RANGE

RAW_DATA_PATH = "C:\\Users\\joaqu\\OneDrive\\Documentos\\KODIGO\\Projects\\python_Cods\\proyecto_final_DAJ\\files_dump\\raw_data\\"
CLEAN_DATA_PATH = "C:\\Users\\joaqu\\OneDrive\\Documentos\\KODIGO\\Projects\\python_Cods\\proyecto_final_DAJ\\files_dump\\clean_data\\"
VEH_TYPE = "yellow_tripdata_"

def create_date_col(df_: pd.DataFrame) -> pd.DataFrame:
    """
    Create a new column with only the date part of the 'tpep_pickup_datetime' column.

    Args:
        df_ (pd.DataFrame): The DataFrame to modify.

    Returns:
        pd.DataFrame: The modified DataFrame.
    """
    df_["tpep_pickup_date"] = df_["tpep_pickup_datetime"].dt.date
    return df_

def order_cols(df_: pd.DataFrame) -> pd.DataFrame:
    """
    Move the last column to the 4th position.

    Args:
        df_ (pd.DataFrame): The DataFrame to modify.

    Returns:
        pd.DataFrame: The modified DataFrame.
    """
    cols = df_.columns.tolist()
    cols = cols[:2] + cols[-1:] + cols[2:-1]
    df_ = df_[cols]
    df_.columns = df_.columns.str.lower()
    return df_

def clean_data(df_: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the data by creating a new column with only the date part of the 'tpep_pickup_datetime' column
    and moving the last column to the 4th position.

    Args:
        df_ (pd.DataFrame): The DataFrame to modify.

    Returns:
        pd.DataFrame: The modified DataFrame.
    """
    df_ = create_date_col(df_)
    df_ = order_cols(df_)
    for col in df_.columns:
        if df_[col].dtype == 'int32':
            df_[col] = df_[col].astype('int64')
    return df_

def save_clean_data(data_range_: list = DATA_RANGE) -> None:
    """
    Save a DataFrame to a parquet file.

    Args:
        data_range_ (list): The list of dates for which the data needs to be processed and saved.
    """
    for date in tqdm(data_range_):
        file_name = f"{VEH_TYPE}{date}.parquet"
        raw_file_path = f"{RAW_DATA_PATH}{file_name}"
        clean_file_path = f"{CLEAN_DATA_PATH}{file_name}"
        
        try:
            df = pd.read_parquet(raw_file_path)
            df = clean_data(df)
            df.to_parquet(clean_file_path, index=False)
            print(f"Data for {date} cleaned and saved successfully")
        except FileNotFoundError as e:
            print(f"File not found: {raw_file_path}. Skipping...")
        except Exception as e:
            print(f"An error occurred while processing {raw_file_path}: {e}")

if __name__ == "__main__":
    save_clean_data()
