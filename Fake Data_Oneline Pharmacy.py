import pandas as pd
import random
from faker import Faker
from datetime import timedelta, date

fake = Faker()
start_date = date.today() - timedelta(days=5*365)
end_date = date.today()
product_list = [
    ("Minoxidil", "Hair", 25.99, True),
    ("Finasteride", "Hair", 39.99, True),
    ("Melatonin", "Sleep", 12.99, False),
    ("Sertraline", "Mental Health", 44.99, True),
    ("Tretinoin", "Skincare", 29.99, True),
    ("Ashwagandha", "Mental Health", 19.99, False),
]
discounts = ["SUMMER25", "DISCOUNT10", "FALL20", "SPRING5", "", "summer25"]
states = ["CA", "NY", "TX", "FL", "WA", "IL", "GA", "PA", "OH", "MI", "NC", "NJ", "VA", "MA"]
genders = ["M", "F", "Other"]
subscription_types = ["None", "Monthly", "Yearly"]

doctor_suffixes = ["", " (D.O)", " (D.O.)", " (M.D)", " (MD)", " (DO)", " md", " do", " m.d.", " d.o.", " (PhD)"]

def random_doctor_name():
    name = fake.name()
    # Randomly make lowercase, uppercase, or mixed case
    case_type = random.choice(["upper", "lower", "normal"])
    if case_type == "upper":
        name = name.upper()
    elif case_type == "lower":
        name = name.lower()
    # Randomly add a suffix
    suffix = random.choice(doctor_suffixes)
    return name + suffix

rows = []
order_id = 5000
customer_subscriptions = {}

for n in range((end_date - start_date).days + 1):
    day = start_date + timedelta(days=n)
    for i in range(random.randint(1,3)):
        prod = random.choice(product_list)
        p_name, p_cat, p_price, p_rx = prod
        qty = random.randint(1,3)
        cust_id = f"C{500 + n + i}"
        cust_age = random.randint(18,70)
        gender = random.choice(genders)
        rx_required = p_rx
        prescribing_doctor = random_doctor_name() if rx_required else "N/A"
        refill = random.choice([True, False])
        shipping_delay = random.choice([random.randint(0,15), random.randint(16,40)])
        rating = round(random.uniform(1,5),1)
        delivery = day + timedelta(days=shipping_delay)
        discount_code = random.choice(discounts)
        state = random.choice(states)

        # Subscription logic
        if cust_id not in customer_subscriptions:
            sub_plan = random.choice(subscription_types)
            customer_subscriptions[cust_id] = sub_plan
        else:
            prev_plan = customer_subscriptions[cust_id]
            if prev_plan == "Monthly" and random.random() < 0.1:
                sub_plan = "Monthly→Yearly"
                customer_subscriptions[cust_id] = sub_plan
            else:
                sub_plan = prev_plan

        row = [
            order_id,
            cust_id,
            day.strftime("%Y-%m-%d"),
            p_name,
            p_cat,
            qty,
            p_price,
            discount_code,
            state,
            cust_age,
            gender,
            rx_required,
            prescribing_doctor,
            refill,
            shipping_delay,
            rating,
            delivery.strftime("%Y-%m-%d"),
            sub_plan
        ]
        rows.append(row)
        order_id += 1

df = pd.DataFrame(rows, columns=[
    "order_id","customer_id","order_date","product_name","product_category","quantity","price_usd",
    "discount_code","state","customer_age","gender","prescription_required","prescribing_doctor",
    "refill","shipping_delay_days","customer_rating","delivery_date","subscription_type"
])

print(df.head(11))  # Shows the first 10 rows

df.to_csv("shao's_pharmacy_online_orders_5yrs.csv", index=False)