import pandas as pd
import random
from faker import Faker
from datetime import date, datetime, timedelta

fake = Faker()

# Helper to convert column names to nice format
def make_nice(col):
    return col.replace("_", " ").title()

# Read customers and products, correcting column names for consistency
df_customers = pd.read_csv("customers.csv")
df_products = pd.read_csv("products.csv")
df_products.columns = [make_nice(col) for col in df_products.columns]  # Ensures nice column names for products

# Convert date column to datetime for comparison
df_customers["Subs Change Date"] = pd.to_datetime(df_customers["Subs Change Date"])

# Order generation parameters
start_date = date(2020, 1, 1)   # Start from January 1, 2020
end_date = date.today()
order_rows = []
order_id = 10000

doctor_suffixes = ["", " (D.O)", " (D.O.)", " (M.D)", " (MD)", " (DO)", " md", " do", " m.d.", " d.o.", " (PhD)"]
duplicate_pct = 0.03

order_statuses = [
    "Scheduled", "Processing", "Shipped", "Delivered", "Cancelled", "On Hold", "Returned", "Awaiting Payment",
    "Awaiting Shipment", "Completed", "Failed", "Partially Delivered", "Rescheduled"
]
order_status_probs = [
    0.05, 0.18, 0.15, 0.22, 0.04, 0.02, 0.01, 0.03, 0.03, 0.17, 0.02, 0.02, 0.04
]

# Main order generation loop
for n in range((end_date - start_date).days + 1):
    day = start_date + timedelta(days=n)
    year_month = day.strftime("%Y-%m")
    day_ts = pd.Timestamp(day)

    # Efficient: Only compute eligible customers once per day
    daily_status = (
        df_customers[df_customers["Subs Change Date"] <= day_ts]
        .sort_values("Subs Change Date")
        .groupby("Customer Id")
        .tail(1)
    )
    eligible_daily_customers = daily_status[daily_status["Subscription Status"].isin(["Active", "Paused", "Pending"])]

    num_orders = random.randint(6, 24)
    for i in range(num_orders):
        product = df_products.sample(1).iloc[0]
        qty = random.randint(1, 3)
        shipping_delay = random.choice([random.randint(0, 15), random.randint(16, 40)])
        rating = round(random.uniform(1, 5), 1)
        delivery = day + timedelta(days=shipping_delay)
        refill = random.choice([True, False])

        if product["Prescription Required"]:
            if eligible_daily_customers.empty:
                continue
            customer = eligible_daily_customers.sample(1).iloc[0]
            prescribing_doctor = fake.name() + random.choice(doctor_suffixes)
        else:
            customer = df_customers.sample(1).iloc[0]
            prescribing_doctor = "N/A"

        months_ago = (date.today().year - day.year) * 12 + (date.today().month - day.month)
        if months_ago > 1:
            status_choices = ["Completed", "Delivered", "Cancelled", "Returned", "Failed"]
            status_probs = [0.75, 0.15, 0.05, 0.03, 0.02]
            order_status = random.choices(status_choices, status_probs, k=1)[0]
        else:
            order_status = random.choices(order_statuses, order_status_probs, k=1)[0]

        payment_method = random.choice(["Credit Card", "Paypal", "Apple Pay", "Google Pay"])
        price_usd = product["Price Usd"]
        tax_rate = random.uniform(0.04, 0.11)  # 5% to 8.5%
        order_total = round(qty * price_usd * (1 + tax_rate), 2)

        ship_hour = random.randint(8, 18)
        ship_minute = random.randint(0, 59)
        shipping_datetime = datetime(day.year, day.month, day.day, ship_hour, ship_minute, 0)
        deliver_hour = random.randint(9, 20)
        deliver_minute = random.randint(0, 59)
        delivered_datetime = datetime(delivery.year, delivery.month, delivery.day, deliver_hour, deliver_minute, 0)

        order = [
            order_id,
            customer["Customer Id"],
            day.strftime("%Y-%m-%d"),
            year_month,
            product["Product Id"],
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

        # Occasionally create a duplicate order
        if random.random() < duplicate_pct:
            order_id += 1
            duplicate_order = list(order)
            duplicate_order[0] = order_id
            order_rows.append(duplicate_order)

        order_id += 1

df_orders = pd.DataFrame(order_rows, columns=[
    "Order Id", "Customer Id", "Order Date", "Year Month", "Product Id", "Quantity", "Shipping Delay Days",
    "Customer Rating", "Shipping Date", "Delivered Date", "Refill", "Prescribing Doctor", "Order Status",
    "Payment Method", "Order Total"
])

df_orders.columns = [make_nice(col) for col in df_orders.columns]

df_orders.to_csv("orders.csv", index=False)
print(f"Generated {len(df_orders)} orders and saved to orders.csv")