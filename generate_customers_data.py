import pandas as pd
import random
from faker import Faker
from datetime import date, timedelta

fake = Faker()
states = ["CA", "NY", "TX", "FL", "WA", "IL", "GA", "PA", "OH", "MI", "NC", "NJ", "VA", "MA"]
genders = ["M", "F", "Other"]
subscription_types = ["Monthly", "Yearly"]
subscription_statuses = ["Active", "Paused", "Canceled", "Pending", "Expired", "None"]

num_customers = 4000

subs_history_rows = []
subs_change_id = 10000

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
    # Decide if this customer ever had a subscription
    ever_had_sub = random.choices([True, False], [0.8, 0.2])[0]
    # Initial record
    initial_change_date = date.today() - timedelta(days=random.randint(0,5*365))
    if ever_had_sub:
        initial_status = random.choice(subscription_statuses[:-1])  # Not 'None'
        initial_type = random.choice(subscription_types)
        # If status is Active, Paused, Pending, auto-renewal is likely True
        if initial_status in ["Active", "Paused", "Pending"]:
            auto_renewal = random.choices([True, False], [0.85, 0.15])[0]
        elif initial_status in ["Canceled", "Expired"]:
            auto_renewal = False
        else:
            auto_renewal = False
    else:
        initial_status = "None"
        initial_type = "None"
        auto_renewal = False
    status_history = [(initial_change_date, initial_status, initial_type, auto_renewal)]
    # How many status changes after initial?
    changes = random.choices([0,1,2,3], [0.7, 0.15, 0.10, 0.05])[0]
    last_change_date = initial_change_date
    last_status = initial_status
    last_type = initial_type
    last_auto_renewal = auto_renewal
    for j in range(changes):
        change_days = random.randint(30,900)
        change_date = last_change_date + timedelta(days=change_days)
        if change_date > date.today():
            break
        # Choose next status logically
        possible_statuses = subscription_statuses[:-1] if last_status != "None" else ["Active", "Pending", "None"]
        new_status = random.choice(possible_statuses)
        # Map type to status
        if new_status == "None":
            new_type = "None"
            new_auto_renewal = False
        else:
            new_type = random.choice(subscription_types)
            if new_status in ["Active", "Paused", "Pending"]:
                new_auto_renewal = random.choices([True, False], [0.85, 0.15])[0]
            elif new_status in ["Canceled", "Expired"]:
                new_auto_renewal = False
            else:
                new_auto_renewal = False
        status_history.append((change_date, new_status, new_type, new_auto_renewal))
        last_change_date = change_date
        last_status = new_status
        last_type = new_type
        last_auto_renewal = new_auto_renewal
    # Each change/history gets its own row
    for change_idx, (change_date, status, sub_type, auto_renew) in enumerate(status_history):
        subs_history_rows.append([
            subs_change_id, customer_id, name, email, birth_date, gender, state, sub_type, status, change_date.strftime("%Y-%m-%d"), auto_renew
        ])
        subs_change_id += 1

def make_nice(col):
    # Converts "Subs_Change_Id" -> "Subs Change Id"
    return col.replace("_", " ").title()

df_subs_history = pd.DataFrame(subs_history_rows, columns=[
    "Subs_Change_Id","Customer_Id","Name","Email","Birth_Date","Gender","State",
    "Subscription_Type","Subscription_Status","Subs_Change_Date","Auto_Renewal"
])

df_subs_history.columns = [make_nice(col) for col in df_subs_history.columns]

df_subs_history.to_csv("customers.csv", index=False)