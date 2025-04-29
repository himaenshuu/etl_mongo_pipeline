# etl/extract.py
import pandas as pd

def from_csv(file_path: str) -> pd.DataFrame:
    """Extracts data from a CSV file into a pandas DataFrame."""
    try:
        df = pd.read_csv(file_path)
        print(f"Data extracted successfully from {file_path}")
        return df
    except Exception as e:
        print(f"Error extracting data from {file_path}: {e}")
        raise
