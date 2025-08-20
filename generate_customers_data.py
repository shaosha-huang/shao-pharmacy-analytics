import pandas as pd
import random
from faker import Faker
from datetime import date, timedelta

fake = Faker()
states = ["CA", "NY", "TX", "FL", "WA", "IL", "GA", "PA", "OH", "MI", "NC", "NJ", "VA", "MA"]
genders = ["M", "F", "Other"]
subscription_types = ["None", "Monthly", "Yearly"]
subscription_statuses = ["active", "paused", "canceled", "pending", "expired"]
num_customers = 1000

customer_rows = []
for i in range(num_customers):
    customer_id = f"C{500+i}"
    name = fake.first_name() + " " + fake.last_name()
    email = fake.email()
    
    min_age = 18
    max_age = 70
    age = random.randint(min_age, max_age)
    birth_date = (date.today() - timedelta(days=age*365 + random.randint(0, 364))).strftime("%Y-%m-%d")
    
    gender = random.choice(genders)
    state = random.choice(states)
    registration_date = (date.today() - timedelta(days=random.randint(0,5*365))).strftime("%Y-%m-%d")
    subscription_type = random.choice(subscription_types)
    subscription_status = random.choice(subscription_statuses)
    customer_rows.append([
        customer_id, name, email, birth_date, gender, state, registration_date, subscription_type, subscription_status
    ])

df_customers = pd.DataFrame(customer_rows, columns=[
    "customer_id","name","email","birth_date","gender","state","registration_date","subscription_type","subscription_status"
])

df_customers.to_csv("customers.csv", index=False)