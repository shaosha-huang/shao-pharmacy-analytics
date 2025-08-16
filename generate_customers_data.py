import pandas as pd
import random
from faker import Faker
from datetime import date, timedelta

fake = Faker()
states = ["CA", "NY", "TX", "FL", "WA", "IL", "GA", "PA", "OH", "MI", "NC", "NJ", "VA", "MA"]
genders = ["M", "F", "Other"]
subscription_types = ["None", "Monthly", "Yearly"]
num_customers = 1000

customer_rows = []
for i in range(num_customers):
    customer_id = f"C{500+i}"
    name = fake.name()
    email = fake.email()
    age = random.randint(18, 70)
    gender = random.choice(genders)
    state = random.choice(states)
    registration_date = (date.today() - timedelta(days=random.randint(0,5*365))).strftime("%Y-%m-%d")
    subscription_type = random.choice(subscription_types)
    customer_rows.append([
        customer_id, name, email, age, gender, state, registration_date, subscription_type
    ])

df_customers = pd.DataFrame(customer_rows, columns=[
    "customer_id","name","email","age","gender","state","registration_date","subscription_type"
])

df_customers.to_csv("customers.csv", index=False)