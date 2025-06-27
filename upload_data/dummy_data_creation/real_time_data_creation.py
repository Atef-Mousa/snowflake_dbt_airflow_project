import pandas as pd
import random
from datetime import datetime, timedelta

try : 
    first_id = int(pd.read_csv("/home/atef/project/E-Commerce-Order-Pipeline/upload_data/dummy_data_creation/shipments.csv").iloc[-1,0][1:])+1
except : 
    first_id=1

def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

# Generate Orders
orders = pd.DataFrame({
    'order_id': [f'O{i}' for i in range(first_id, first_id+20)],
    'customer_id': [f'C{random.randint(first_id, first_id+5)}' for _ in range(20)],
    'order_date': pd.date_range(start='2024-01-01', periods=20, freq='D')
})
orders.to_csv('/home/atef/project/E-Commerce-Order-Pipeline/upload_data/dummy_data_creation/orders.csv', index=False)

# Generate Customers
customers = pd.DataFrame({
    'customer_id': [f'C{i}' for i in range(first_id, first_id+5)],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'email': [f'user{i}@example.com' for i in range(first_id, first_id+5)]
})
customers.to_csv('/home/atef/project/E-Commerce-Order-Pipeline/upload_data/dummy_data_creation/customers.csv', index=False)

# Generate Shipments

start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 1, 20)


statuses = ['shipped', 'delivered']
shipments = pd.DataFrame({
    'shipment_id': [f'S{i}' for i in range(first_id, first_id+20)],
    'order_id': orders['order_id'],
    'status': [random.choice(statuses) for _ in range(20)],
    'shipped_at' : [random_date(start_date, end_date) for _ in range(20)]
})

shipments['delivered_at'] = [ random_date(shipped, shipped + timedelta(days=5)) for shipped in shipments['shipped_at']]


shipments.to_csv('/home/atef/project/E-Commerce-Order-Pipeline/upload_data/dummy_data_creation/shipments.csv', index=False)




