import pandas as pd
import random

product_list = [
    ("Minoxidil", "Hair", 25.99, True, "HairGrow Labs", "Topical solution to treat hair loss and promote hair regrowth."),
    ("Finasteride", "Hair", 39.99, True, "HairGrow Labs", "Oral medication for male pattern baldness; helps prevent hair loss."),
    ("Melatonin", "Sleep", 12.99, False, "SleepWell Inc", "Supplement to support healthy sleep cycles and combat insomnia."),
    ("Sertraline", "Mental Health", 44.99, True, "MindCare Pharmaceuticals", "Prescription antidepressant used to treat depression and anxiety disorders."),
    ("Tretinoin", "Skincare", 29.99, True, "SkinRenew Co", "Topical retinoid for acne treatment and skin renewal."),
    ("Ashwagandha", "Mental Health", 19.99, False, "Herbal Remedies", "Herbal supplement to support stress relief and mental clarity."),
    ("Vitamin D", "Health", 10.99, False, "Sunshine Pharma", "Essential vitamin for bone health and immune support."),
    ("Hydroxyzine", "Allergy", 22.99, True, "AllerGuard", "Prescription antihistamine for allergy relief and itching."),
    ("Ibuprofen", "Pain Relief", 8.99, False, "ReliefRx", "Non-prescription pain reliever for headaches, muscle aches, and fevers."),
]

product_rows = []
for i, prod in enumerate(product_list):
    product_id = f"P{1000+i}"
    name, category, price, rx, manufacturer, description = prod
    stock_quantity = random.randint(100, 10000)
    product_rows.append([
        product_id, name, category, price, rx, manufacturer, stock_quantity, description
    ])

df_products = pd.DataFrame(product_rows, columns=[
    "product_id","product_name","product_category","price_usd","prescription_required",
    "manufacturer","stock_quantity","description"
])
df_products.to_csv("products.csv", index=False)