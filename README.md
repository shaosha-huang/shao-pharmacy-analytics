# 📊 Shao's Pharmacy: Data Analytics Project

Welcome to the portfolio repository for **Shao's Pharmacy**, a sample business analytics project.  
This project demonstrates the entire analytics workflow: synthetic data creation, SQL cleaning & analysis, and Tableau dashboarding.

> **Quality over quantity:**  
> Two stellar, business-relevant projects stand out much more than several mediocre ones.

Fork this repo, adapt it, and make it your own.  
**Happy portfolio-ing! 🚀**

---

## 🏢 Project Background

**Industry:** Telemedicine / Online Pharmacy  
**Active Years:** 2019–2024 (5 years of data)  
**Business Model:** Direct-to-consumer online prescription and over-the-counter medication sales, with monthly/yearly subscription options for recurring orders.  
**Key Metrics:** Order volume, customer retention, product category sales, prescription fulfillment rates, shipping times, customer satisfaction.

As a data analyst at Shao's Pharmacy, your goal is to generate actionable insights from sales, customer, and product data to improve growth, retention, and operational efficiency.

---

## 🔎 Key Areas of Insights & Recommendations

Insights and recommendations are provided on the following key areas:
- **Customer Segmentation:** Who are our top segments? How do subscription types affect ordering patterns?
- **Product Performance:** Which products/categories drive revenue? What are seasonal trends?
- **Order Fulfillment & Operations:** Shipping delays, prescription completion rates, and refill behavior.
- **Customer Satisfaction:** Ratings, feedback, and their relationship to repeat business.

- The SQL queries used for initial cleaning and inspection are [here](link).
- Targeted SQL queries for business questions are [here](link).
- The interactive Tableau dashboard is [here](link).

---

## 🗄️ Data Structure & Initial Checks

Shao's Pharmacy's database consists of **three main tables** with a total of **X** records.  
Here’s a description of each table:

- **customers:** Demographic and subscription info for each customer.
- **products:** Product catalog, pricing, and prescription status.
- **orders:** Transactional table linking customers and products, with order details and fulfillment info.

### Entity Relationship Diagram

See below for a text diagram:

```mermaid
erDiagram
    CUSTOMERS ||--o{ ORDERS : places
    PRODUCTS ||--o{ ORDERS : includes

    CUSTOMERS {
        string customer_id PK
        string name
        string email
        int age
        string gender
        string state
        date registration_date
        string subscription_type
    }
    PRODUCTS {
        string product_id PK
        string product_name
        string product_category
        float price_usd
        boolean prescription_required
        string manufacturer
        int stock_quantity
        string description
    }
    ORDERS {
        int order_id PK
        string customer_id FK
        string order_date
        string product_id FK
        int quantity
        string discount_code
        int shipping_delay_days
        float customer_rating
        datetime shipping_date
        datetime delivered_date
        boolean refill
        string prescribing_doctor
        string order_status
        string payment_method
        float order_total
        # Note: Duplicates can exist for order_id, but are unique values
    }
```

---

## 📝 Executive Summary

### **Overview of Findings**

Over five years, Shao's Pharmacy grew steadily, with monthly subscriptions increasing customer retention.  
Hair and mental health