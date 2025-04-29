# data_warehouse_creation.py

def extract():
    print("🔍 Extracting data from source systems...")
    # Simulated data
    data = [
        {"id": 1, "product": "Apple", "sales": 120},
        {"id": 2, "product": "Banana", "sales": 90},
    ]
    return data

def transform(data):
    print("🔧 Transforming data...")
    # Example transformation: uppercase product names
    for record in data:
        record["product"] = record["product"].upper()
    return data

def load(data):
    print("📦 Loading data into Data Warehouse (simulated)...")
    for row in data:
        print(f"Inserted record: {row}")

def create_data_warehouse():
    print("🏗️ Starting Data Warehouse creation process...\n")
    data = extract()
    transformed_data = transform(data)
    load(transformed_data)
    print("\n✅ Data Warehouse creation completed successfully.")

if __name__ == "__main__":
    create_data_warehouse()
