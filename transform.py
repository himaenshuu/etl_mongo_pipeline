# etl/transform.py
import pandas as pd

def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans and transforms the sales data."""
    
    # Remove duplicates (if any)
    df.drop_duplicates(inplace=True)

    # Convert 'sale_date' to datetime
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    
    # Handle missing values: Fill or drop
    df.fillna({'amount': 0}, inplace=True)
    
    df['Year'] = df['Year']
    df['Month'] = df['Month']
    
    print("Data cleaned and transformed successfully.")
    return df
