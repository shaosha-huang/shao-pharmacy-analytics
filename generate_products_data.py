import pandas as pd
import random
from faker import Faker

fake = Faker()
product_list = [
    ("Minoxidil", "Hair", 25.99, True, "HairGrow Labs"),
    ("Finasteride", "Hair", 39.99, True, "HairGrow Labs"),
    ("Melatonin", "Sleep", 12.99, False, "SleepWell Inc"),
    ("Sertraline", "Mental Health", 44.99, True, "MindCare Pharmaceuticals"),
    ("Tretinoin", "Skincare", 29.99, True, "SkinRenew Co"),
    ("Ashwagandha", "Mental Health", 19.99, False, "Herbal Remedies"),
    ("Vitamin D", "Health", 10.99, False, "Sunshine Pharma"),
    ("Hydroxyzine", "Allergy", 22.99, True, "AllerGuard"),
    ("Ibuprofen", "Pain Relief", 8.99, False, "ReliefRx"),
]
product_rows = []
for i, prod in enumerate(product_list):
    product_id = f"P{1000+i}"
    name, category, price, rx, manufacturer = prod
    stock_quantity = random.randint(100, 10000)
    description = fake.sentence(nb_words=10)
    product_rows.append([
        product_id, name, category, price, rx, manufacturer, stock_quantity, description
    ])

df_products = pd.DataFrame(product_rows, columns=[
    "product_id","product_name","product_category","price_usd","prescription_required",
    "manufacturer","stock_quantity","description"
])
df_products.to_csv("products.csv", index=False)