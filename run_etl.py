# etl/run_etl.py
from extract import from_csv
from transform import clean_sales_data
from load import to_mongo

def run_etl():
    """Orchestrates the ETL process."""
    
    # Step 1: Extract data from CSV
    df = from_csv("sales_data.csv ")
    
    # Step 2: Transform the data (cleaning)
    df_cleaned = clean_sales_data(df)
    
    # Step 3: Load the cleaned data into PostgreSQL
    to_mongo(df_cleaned,"any","any")

if __name__ == "__main__":
    run_etl()
