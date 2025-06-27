E-Commerce Order Monitoring Pipeline

This project builds a data pipeline to load and transform order data using Snowflake, dbt, and Apache Airflow.

🔧 Technologies Used

Snowflake: Data warehouse

dbt: Data transformation tool

Airflow: Workflow scheduler

Python: Scripts for loading data

Project Structure

.
├── airflow_project/
│   └── dags/order_monitoring_dag.py       # Airflow DAG
├── upload_data/
│   ├── upload_to_snowflake.py            # Python script to load CSVs into Snowflake
│   └── dummy_data_creation/              # CSV files (customers, orders, shipments)
├── dbt_ecommerce/                        # dbt project
│   ├── dbt_project.yml
│   └── models/
└── snowflake_config.yaml      

Create Python Environments

python3 -m venv snowflake_env
source snowflake_env/bin/activate
pip install -r requirements_upload.txt

# For dbt
python3 -m venv dbt_env
source dbt_env/bin/activate
pip install dbt-snowflake==1.4.5

# For Airflow
python3 -m venv airflow_env
source airflow_venv_39/bin/activate
pip install apache-airflow


#for uploading real time data to snowflake 
python3 -m venv snowflake_env
source snowflake_env/bin/activate
pip install pip install snowflake-connector-python

note: i add the last venv becuase there was a conflict with dbt and airflow with snowflake connector liberary

