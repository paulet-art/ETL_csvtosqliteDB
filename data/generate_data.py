import csv
import random
from datetime import datetime, timedelta

def generate_fraud_data(num_records):
    fraud_data = []
    for i in range(num_records):
        fraud_id = f"FRAUD{i+1}"
        phone_number = f"07{random.randint(10000000, 99999999)}"
        fraud_type = random.choice(["Unauthorized Transfer", "Phishing Scam", "Identity Theft"])
        complaint_id = f"COMP{i+1}"
        complaint_details = f"Complaint filed regarding {fraud_type}"
        customer_care_id = f"CC{i+1}"
        customer_care_details = random.choice(["Under Investigation", "Resolved", "Pending"])
        status = random.choice(["Pending", "Solved"])
        
        fraud_data.append((fraud_id, phone_number, fraud_type, complaint_id, complaint_details,
                           customer_care_id, customer_care_details, status))
    return fraud_data

def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Fraud_ID', 'Phone_Numbers', 'Fraud_Type', 'Complaint_ID', 
                         'Complaint_Details', 'Customer_Care_ID', 'Customer_Care_Details', 'Status'])
        writer.writerows(data)

if __name__ == "__main__":
    num_records = 50
    fraud_data = generate_fraud_data(num_records)
    write_to_csv('mpesa_fraud_complaints.csv', fraud_data)
