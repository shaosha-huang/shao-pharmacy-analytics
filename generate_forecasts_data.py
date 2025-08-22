import pandas as pd
import random
from datetime import datetime

# Load orders and products data
df_orders = pd.read_csv("orders.csv")
df_products = pd.read_csv("products.csv")

# Convert order_date to datetime and extract year-month
df_orders['order_date'] = pd.to_datetime(df_orders['order_date'])
df_orders['year_month'] = df_orders['order_date'].dt.to_period('M').astype(str)

# Merge orders with products to get cost and price
df_orders = df_orders.merge(df_products[['product_id', 'price_usd', 'cost_usd']], on='product_id', how='left')

# Group orders by year-month
monthly_orders = df_orders.groupby('year_month').agg({
    'order_total': 'sum',
    'cost_usd': lambda x: (x * df_orders.loc[x.index, 'order_total'] / df_orders.loc[x.index, 'price_usd']).sum()
}).reset_index()

# Forecast logic: apply a random growth factor for each month
forecast_rows = []
for i, row in monthly_orders.iterrows():
    year_month = row['year_month']
    actual_revenue = round(row['order_total'], 2)
    actual_cost = round(row['cost_usd'], 2)
    trend_factor = round(random.uniform(1.02, 1.10), 3)
    forecasted_revenue = round(actual_revenue * trend_factor, 2)
    forecasted_cost = round(actual_cost * trend_factor, 2)
    forecasted_margin = round(forecasted_revenue - forecasted_cost, 2)
    confidence_score = round(random.uniform(0.7, 0.99), 2)
    forecast_date = datetime.now().strftime("%Y-%m-%d")
    
    forecast_rows.append([
        f"FM{i+1:04d}", year_month, actual_revenue, actual_cost, forecasted_revenue,
        forecasted_cost, forecasted_margin, confidence_score, forecast_date, trend_factor
    ])

df_monthly_forecast = pd.DataFrame(forecast_rows, columns=[
    "forecast_id", "year_month", "actual_revenue", "actual_cost", "forecasted_revenue", "forecasted_cost",
    "forecasted_margin", "confidence_score", "forecast_date", "trend_factor"
])

df_monthly_forecast.to_csv("forecasts.csv", index=False)