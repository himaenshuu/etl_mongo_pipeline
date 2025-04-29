# etl/load.py
from pymongo import MongoClient
import pandas as pd

def to_mongo(df: pd.DataFrame, db_name: str, collection_name: str):
    """Loads the DataFrame into MongoDB."""
    
    # Define MongoDB connection (local or remote)
    client = MongoClient("mongodb://localhost:27017/")  # Use your MongoDB connection URI
    db = client[db_name]  # Specify the database name
    collection = db[collection_name]  # Specify the collection name

    try:
        # Convert DataFrame to dictionary and insert into MongoDB
        records = df.to_dict(orient='records')  # Convert DataFrame to a list of dicts
        collection.insert_many(records)  # Insert records into MongoDB collection
        print("Data loaded successfully into MongoDB")
    except Exception as e:
        print(f"Error loading data into MongoDB: {e}")
        raise
