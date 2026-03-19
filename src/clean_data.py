import pandas as pd
import numpy as np

def remove_iso_duplicate(df: pd.DataFrame) -> pd.DataFrame:
    # Removes duplicate iso_a2 column:
    return df.drop(columns=["iso_a2.1"])


def remove_duplicate_rows(df: pd.DataFrame) -> pd.DataFrame:
    # Exact Duplicates Can Be Safely Removed: 
    clean_df = df.drop_duplicates()

    # Find & Remove remaining duplicates:
    duplicates_mask = clean_df.duplicated(subset=["iso_a2"], keep=False)
    return clean_df.drop(clean_df[(duplicates_mask) & ((clean_df.lifeExp < 1.0) | (clean_df.gdpPercap < 1.0))].index) 

def standardize_null_values(df: pd.DataFrame) -> pd.DataFrame:
    # --- Standardizes missing data by converting zero-values to NaN ---
    
    # Copy DataFrame:
    clean_df = df.copy()
    
    # Isolate the messy columns: 
    cols = ["pop", "lifeExp", "gdpPercap"]

    # Replace messy columns with standardised columns:
    clean_df[cols] = clean_df[cols].mask(clean_df[cols] <= 0)

    # Any lifeExp value that is over 100, set to NaN
    df["lifeExp"] = df["lifeExp"].mask(df["lifeExp"] > 100)

    return clean_df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    clean_df = df.copy()
    clean_df = remove_iso_duplicate(clean_df)
    clean_df = remove_duplicate_rows(clean_df)
    clean_df = standardize_null_values(clean_df)
    return clean_df
    
