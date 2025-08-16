import pandas as pd
import random
from faker import Faker
from datetime import date, timedelta

fake = Faker()
# Load customers and products
df_customers = pd.read_csv("generate_customers_data.csv")
df_products = pd.read_csv("generate_products_data.csv")

start_date = date.today() - timedelta(days=5*365)
end_date = date.today()
order_rows = []
order_id = 10000

doctor_suffixes = ["", " (D.O)", " (D.O.)", " (M.D)", " (MD)", " (DO)", " md", " do", " m.d.", " d.o.", " (PhD)"]

for n in range((end_date - start_date).days + 1):
    day = start_date + timedelta(days=n)
    for i in range(random.randint(1,4)):
        customer = df_customers.sample(1).iloc[0]
        product = df_products.sample(1).iloc[0]
        qty = random.randint(1,3)
        discount_code = random.choice(["SUMMER25", "DISCOUNT10", "FALL20", "SPRING5", "", "summer25"])
        shipping_delay = random.choice([random.randint(0,15), random.randint(16,40)])
        rating = round(random.uniform(1,5),1)
        delivery = day + timedelta(days=shipping_delay)
        refill = random.choice([True, False])
        prescribing_doctor = (
            fake.name() + random.choice(doctor_suffixes)
            if product["prescription_required"] else "N/A"
        )
        order_status = random.choice(["Shipped", "Delivered", "Processing", "Cancelled"])
        payment_method = random.choice(["Credit Card", "Paypal", "Apple Pay", "Google Pay"])
        order_total = qty * product["price_usd"]
        order_rows.append([
            order_id,
            customer["customer_id"],
            day.strftime("%Y-%m-%d"),
            product["product_id"],
            qty,
            discount_code,
            shipping_delay,
            rating,
            delivery.strftime("%Y-%m-%d"),
            refill,
            prescribing_doctor,
            order_status,
            payment_method,
            order_total
        ])
        order_id += 1

df_orders = pd.DataFrame(order_rows, columns=[
    "order_id","customer_id","order_date","product_id","quantity","discount_code","shipping_delay_days",
    "customer_rating","delivery_date","refill","prescribing_doctor","order_status","payment_method","order_total"
])
df_orders.to_csv("orders.csv", index=False)