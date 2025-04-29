
# 🛠️ ETL Pipeline with MongoDB

This project demonstrates a basic **ETL (Extract, Transform, Load)** pipeline using Python, where data is extracted from a CSV file, cleaned, and then loaded into a **MongoDB** collection.

---

## 📁 Project Structure
```

etl_project/
│
├── etl/
│ ├── extract.py # Extract data from CSV
│ ├── transform.py # Clean/transform data
│ ├── load.py # Load data into MongoDB
│ └── run_etl.py # Orchestrates the ETL process
│
├── sales_data.csv # Sample raw data file
├── requirements.txt # Python dependencies
└── README.md # Project documentation

````

---

## 🔄 ETL Process

1. **Extract**: Reads data from `sales_data.csv`.
2. **Transform**: Cleans the data (e.g., handles missing values, formats dates).
3. **Load**: Loads the cleaned data into a MongoDB collection.

---

## 🧪 Example: Running the Pipeline

```bash
python etl/run_etl.py
````

Ensure that MongoDB is running locally or update the MongoDB connection URI in `load.py`.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/etl-mongo-pipeline.git
cd etl-mongo-pipeline
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the mainfile

```bash
python run_etl.py
```

### 3. Ensure MongoDB is Running

Start your MongoDB instance on `localhost:27017` or update the connection string accordingly.

---

## 📦 Requirements

- Python 3.7+
- pandas
- pymongo

Add any required libraries to `requirements.txt` if missing.

---

## 📌 Notes

- You can replace the CSV source or MongoDB collection name by modifying the parameters in `run_etl.py`.
- This is a simplified version for educational or POC purposes. For production, consider adding logging, validation, and error handling.

---

## 📧 Contact

For questions or feedback, contact [Himanshu Raj](nebula3477@gmail.com)

```

---

Let me know if you'd like the README saved as a file or extended with badges, visuals, or MongoDB setup steps.
```
