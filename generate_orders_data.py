import pandas as pd
import random
from faker import Faker
from datetime import date, datetime, timedelta

fake = Faker()
# Load customers and products
df_customers = pd.read_csv("customers.csv")
df_products = pd.read_csv("products.csv")

start_date = date.today() - timedelta(days=5*365)
end_date = date.today()
order_rows = []
order_id = 10000

doctor_suffixes = ["", " (D.O)", " (D.O.)", " (M.D)", " (MD)", " (DO)", " md", " do", " m.d.", " d.o.", " (PhD)"]

duplicate_pct = 0.03  # 3% of orders will be duplicates

# Expanded order status options
order_statuses = [
    "Scheduled", "Processing", "Shipped", "Delivered", "Cancelled", "On Hold", "Returned", "Awaiting Payment", 
    "Awaiting Shipment", "Completed", "Failed", "Partially Delivered", "Rescheduled"
]

for n in range((end_date - start_date).days + 1):
    day = start_date + timedelta(days=n)
    year_month = day.strftime("%Y-%m")
    for i in range(random.randint(1,4)):
        customer = df_customers.sample(1).iloc[0]
        product = df_products.sample(1).iloc[0]
        qty = random.randint(1,3)
        shipping_delay = random.choice([random.randint(0,15), random.randint(16,40)])
        rating = round(random.uniform(1,5),1)
        delivery = day + timedelta(days=shipping_delay)
        refill = random.choice([True, False])
        prescribing_doctor = (
            fake.name() + random.choice(doctor_suffixes)
            if product["prescription_required"] else "N/A"
        )
        order_status = random.choice(order_statuses)
        payment_method = random.choice(["Credit Card", "Paypal", "Apple Pay", "Google Pay"])
        price_usd = product["price_usd"]
        tax_rate = random.uniform(0.04, 0.11)  # random tax between 4% and 11%
        order_total = round(qty * price_usd * (1 + tax_rate), 2)

        # Generate shipping and delivered datetime
        ship_hour = random.randint(8, 18)
        ship_minute = random.randint(0, 59)
        shipping_datetime = datetime(day.year, day.month, day.day, ship_hour, ship_minute, 0)
        deliver_hour = random.randint(9, 20)
        deliver_minute = random.randint(0, 59)
        delivered_datetime = datetime(delivery.year, delivery.month, delivery.day, deliver_hour, deliver_minute, 0)

        order = [
            order_id,
            customer["customer_id"],
            day.strftime("%Y-%m-%d"),
            year_month,
            product["product_id"],
            qty,
            shipping_delay,
            rating,
            shipping_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            delivered_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            refill,
            prescribing_doctor,
            order_status,
            payment_method,
            order_total
        ]
        order_rows.append(order)

        # Randomly add a duplicate
        if random.random() < duplicate_pct:
            # Duplicate the order with a new order_id
            order_id += 1
            duplicate_order = list(order)
            duplicate_order[0] = order_id
            order_rows.append(duplicate_order)

        order_id += 1

df_orders = pd.DataFrame(order_rows, columns=[
    "order_id","customer_id","order_date","year_month","product_id","quantity","shipping_delay_days",
    "customer_rating","shipping_date","delivered_date","refill","prescribing_doctor","order_status","payment_method","order_total"
])
df_orders.to_csv("orders.csv", index=False)