import pandas as pd
import numpy as np
import random
from datetime import datetime

# Load orders and products data
df_orders = pd.read_csv("orders.csv")
df_products = pd.read_csv("products.csv")

# Make sure columns match the nice format
def make_nice(col):
    return col.replace("_", " ").title()

df_products.columns = [make_nice(col) for col in df_products.columns]
df_orders.columns = [make_nice(col) for col in df_orders.columns]

# Convert Order Date to datetime and extract Year Month
df_orders['Order Date'] = pd.to_datetime(df_orders['Order Date'])
df_orders['Year Month'] = df_orders['Order Date'].dt.to_period('M').astype(str)

# Merge orders with products to get cost and price and product name (no new columns except Product Id/Product Name)
df_orders = df_orders.merge(
    df_products[['Product Id', 'Product Name', 'Price Usd', 'Cost Usd']],
    on='Product Id',
    how='left'
)

# Calculate actual cost per order (based on quantity and cost_usd)
df_orders['Actual Cost'] = df_orders['Quantity'] * df_orders['Cost Usd']

# Group orders by Year Month and Product
monthly_product_orders = df_orders.groupby(['Year Month', 'Product Id', 'Product Name']).agg({
    'Order Total': 'sum',
    'Actual Cost': 'sum'
}).reset_index()

# Realistic Forecast logic: add random bias and noise (sometimes forecast > actual, sometimes < actual)
forecast_rows = []
for i, row in monthly_product_orders.iterrows():
    year_month = row['Year Month']
    product_id = row['Product Id']
    product_name = row['Product Name']
    actual_revenue = round(row['Order Total'], 2)
    actual_cost = round(row['Actual Cost'], 2)
    actual_margin = round(actual_revenue - actual_cost, 2)

    # Simulate realistic forecast error (can be positive or negative)
    revenue_error = np.random.normal(loc=0.03, scale=0.10)  # mean 3% optimistic, std dev 10%
    cost_error = np.random.normal(loc=0.01, scale=0.08)     # mean 1% optimistic, std dev 8%

    forecasted_revenue = round(actual_revenue * (1 + revenue_error), 2)
    forecasted_cost = round(actual_cost * (1 + cost_error), 2)
    forecasted_margin = round(forecasted_revenue - forecasted_cost, 2)

    # Confidence is higher when forecast error is smaller
    error_magnitude = abs(revenue_error)
    confidence_score = round(max(0.65, 0.99 - error_magnitude), 2)

    trend_factor = round(1 + revenue_error, 3)
    forecast_date = datetime.now().strftime("%Y-%m-%d")

    forecast_rows.append([
        f"FM{i+1:06d}", year_month, product_id, product_name,
        actual_revenue, actual_cost, actual_margin,
        forecasted_revenue, forecasted_cost, forecasted_margin,
        confidence_score, forecast_date, trend_factor
    ])

# Set columns to Title Case with space separation (e.g., Birth Date)
def format_col(col):
    col = col.replace("_", " ").replace("-", " ")
    return " ".join([w.capitalize() for w in col.split()])

df_monthly_product_forecast = pd.DataFrame(forecast_rows, columns=[
    "Forecast Id", "Year Month", "Product Id", "Product Name",
    "Actual Revenue", "Actual Cost", "Actual Margin",
    "Forecasted Revenue", "Forecasted Cost", "Forecasted Margin",
    "Confidence Score", "Forecast Date", "Trend Factor"
])

df_monthly_product_forecast.columns = [format_col(col) for col in df_monthly_product_forecast.columns]

df_monthly_product_forecast.to_csv("forecasts.csv", index=False)
print(f"Generated {len(df_monthly_product_forecast)} forecasts and saved to forecasts.csv")