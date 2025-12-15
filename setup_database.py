import sqlite3
import pandas as pd
import os

DB_NAME = "restaurant_inspections.db"
SCHEMA_FILE = "restaurant_inspection_schema.sql"

def init_db():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
        print(f"Removed existing database: {DB_NAME}")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Execute Schema
    with open(SCHEMA_FILE, "r") as f:
        schema_sql = f.read()
        cursor.executescript(schema_sql)
    print("Schema created successfully.")

    # Load Data
    files_to_tables = {
        "establishment.csv": "establishment",
        "employee.csv": "employee",
        "inspection.csv": "inspection",
        "inspection_point.csv": "inspection_point",
        # violation.csv might not exist or be empty, handled below
    }

    for csv_file, table_name in files_to_tables.items():
        if os.path.exists(csv_file):
            try:
                # Load CSV
                df = pd.read_csv(csv_file)
                
                # Data Cleaning / Type Conversion
                if "fine" in df.columns:
                    df["fine"] = pd.to_numeric(df["fine"], errors='coerce').fillna(0)
                
                # specific date parsing if needed, though sqlite handles text dates mostly fine
                # if table_name == "inspection":
                #     df["inspection_date"] = pd.to_datetime(df["inspection_date"])

                df.to_sql(table_name, conn, if_exists="append", index=False)
                print(f"Loaded {len(df)} records into {table_name}.")
            except Exception as e:
                print(f"Error loading {csv_file}: {e}")
        else:
            print(f"Warning: {csv_file} not found. Skipping {table_name}.")

    conn.commit()
    conn.close()
    print("Database setup complete.")

if __name__ == "__main__":
    init_db()
