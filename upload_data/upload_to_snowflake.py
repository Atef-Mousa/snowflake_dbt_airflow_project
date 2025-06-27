import snowflake.connector
import pandas as pd
import yaml 
import os 
import subprocess

def load_snowflake_config():
    config_path = os.path.join(os.path.dirname(__file__), './snowflake_config.yaml')
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config['snowflake']

def main() : 
    snowflake_config = load_snowflake_config()# Snowflake connection parameters

    conn = snowflake.connector.connect(
                user=snowflake_config["user"],
                password=snowflake_config["password"],
                account=snowflake_config["account"],
                warehouse=snowflake_config["warehouse"],
                database=snowflake_config["database"],
                schema=snowflake_config["schema"],
            )



    #call real_time_data_creation
    result = subprocess.run(
    ["python", "/home/atef/project/E-Commerce-Order-Pipeline/upload_data/dummy_data_creation/real_time_data_creation.py"],
    check=True  # raises exception if script fails
)
    # subprocess.run(["python", "/home/atef/project/E-Commerce-Order-Pipeline/upload_data/dummy_data_creation/real_time_data_creation.py"])

    # Cursor
    cursor = conn.cursor()

    # Files and corresponding tables
    files_tables = [
        ("/home/atef/project/E-Commerce-Order-Pipeline/upload_data/dummy_data_creation/customers.csv", "raw.customers"),
        ("/home/atef/project/E-Commerce-Order-Pipeline/upload_data/dummy_data_creation/orders.csv", "raw.orders"),
        ("/home/atef/project/E-Commerce-Order-Pipeline/upload_data/dummy_data_creation/shipments.csv", "raw.shipments"),
    ]

    for file_name, table_name in files_tables:
        print(f"Loading {file_name} into {table_name}...")

        # Load CSV to pandas DataFrame
        df = pd.read_csv(file_name)

        # Create insert query dynamically
        columns = ",".join(df.columns)
        placeholders = ",".join(["%s"] * len(df.columns))
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        # Convert DataFrame to list of tuples
        data = [tuple(row) for row in df.values]

        # Insert data into Snowflake
        cursor.executemany(insert_query, data)

        print(f"{file_name} loaded successfully into {table_name}.")

    # Close connection
    cursor.close()
    conn.close()



if __name__ == "__main__":
    main()