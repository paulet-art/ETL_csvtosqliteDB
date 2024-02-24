import sqlite3
import csv
from datetime import datetime

def etl_process():
    # Extract
    with open('data/data.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

    # Transform
    transformed_data = []
    for row in data:
        row['date'] = datetime.strptime(row['date'], '%Y-%m-%d')
        transformed_data.append(row)

    # Load data into SQLite3
    conn = sqlite3.connect('data/fraud_data.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS fraud_cases
                 (fraud_id TEXT PRIMARY KEY, phone_number TEXT, fraud_type TEXT, 
                 complaint_id TEXT, complaint_details TEXT, customer_care_id TEXT, 
                 customer_care_details TEXT, status TEXT)''')

    for row in transformed_data:
        c.execute('''INSERT INTO fraud_cases (fraud_id, phone_number, fraud_type, 
                     complaint_id, complaint_details, customer_care_id, customer_care_details, status) 
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?)''')
    conn.commit()
    conn.close()
