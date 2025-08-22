# 📊 Shao's Pharmacy: Data Analytics Project

Welcome to the portfolio repository for **Shao's Pharmacy**, a sample business analytics project.  
This project demonstrates the entire analytics workflow: synthetic data creation, SQL cleaning & analysis, and Tableau dashboarding.

> **Quality over quantity:**  
> Two stellar, business-relevant projects stand out much more than several mediocre ones.

Fork this repo, adapt it, and make it your own.  
**Happy portfolio-ing! 🚀**

---

## Project Overview

Hi! I created this project to showcase my ability to work across the data pipeline: generating realistic sample data with Python, using SQL to extract and transform information, and building dashboards that deliver actionable business insights.  
For this project, I focused on four dashboard perspectives that are especially valuable for a real-world team:

- **Customer Segmentation Dashboard:** Understand who your best customers are, their behaviors, and how segmentation impacts retention and growth.
- **Product Performance Dashboard:** Track top-selling products, seasonal trends, and the impact of promotions or prescription requirements.
- **Operations & Satisfaction Dashboard:** Monitor shipping delays, fulfillment bottlenecks, and customer feedback—enabling data-driven improvements in service.
- **Revenue Forecast Dashboard:** Project future monthly revenue, visualize trends, and communicate forecast confidence to support planning and growth.

Together, these dashboards demonstrate how technical skills can translate directly into business impact, supporting teams across marketing, product, operations, and finance.

---

## 🏢 Project Background

**Industry:** Telemedicine / Online Pharmacy  
**Active Years:** 2019–2024 (5 years of data)  
**Business Model:** Direct-to-consumer online prescription and over-the-counter medication sales, with monthly/yearly subscription options for recurring orders.  
**Key Metrics:** Order volume, customer retention, product category sales, prescription fulfillment rates, shipping times, customer satisfaction, revenue forecasts.

As a data analyst at Shao's Pharmacy, my goal is to generate actionable insights from sales, customer, product, and forecast data to improve growth, retention, and operational efficiency.

---

## 🔎 Key Areas of Insights & Recommendations

This portfolio includes hands-on analytics in five key business areas:
- **Customer Segmentation:** Who are our top segments? How do subscription types affect ordering patterns?
- **Product Performance:** Which products/categories drive revenue? What are seasonal trends?
- **Order Fulfillment & Operations:** Shipping delays, prescription completion rates, and refill behavior.
- **Customer Satisfaction:** Ratings, feedback, and their relationship to repeat business.
- **Revenue Forecasts:** Projected monthly revenues, trends over time, and confidence levels for planning.

- The SQL queries used for initial cleaning and inspection are [here](link).
- Targeted SQL queries for business questions are [here](link).
- The interactive Tableau dashboards are [here](link).

---

## 🗄️ Data Structure & Initial Checks

Shao's Pharmacy's database consists of **four main tables** with a total of **X** records.  
Here’s a description of each table:

- **customers:** Demographic and subscription info for each customer.
- **products:** Product catalog, pricing, and prescription status.
- **orders:** Transactional table linking customers and products, with order details, fulfillment info, and a `year_month` field for monthly aggregation.
- **forecast:** Monthly revenue forecasts, including actuals, projections, margin, trend factor, and confidence score.

### Entity Relationship Diagram

![Entity Relationship Diagram](ERD.png)

---

## 📝 Executive Summary

### **Overview of Findings**

Over five years, Shao's Pharmacy grew steadily, with monthly subscriptions increasing customer retention.  
Hair and mental health products accounted for the majority of sales, while shipping delays and prescription issues were key drivers of lower ratings.  
Revenue forecasting models show consistent growth, with trend factors indicating stronger performance in spring and fall.  
Targeting high-value segments, optimizing fulfillment, and leveraging forecast insights are critical opportunities.

[Dashboard snapshot or key trends visualization here]

---

## 📊 Dashboard Highlights

This project delivers four core dashboards, each designed to support strategic decision-making for business leaders and teams:

### 1. Customer Segmentation Dashboard
- Visualizes ordering patterns, subscription types, and top customer segments.
- Helps marketing and retention teams identify high-value groups and peak upgrade times.

### 2. Product Performance Dashboard
- Tracks sales by product and category, including seasonal fluctuations and the impact of prescription status.
- Supports product managers in optimizing the catalog and promotional strategies.

### 3. Operations & Satisfaction Dashboard
- Monitors shipping delays, prescription verification bottlenecks, and customer satisfaction metrics.
- Enables operations teams to address fulfillment issues and improve customer experience.

### 4. Revenue Forecast Dashboard
- Projects monthly revenue using historical order data, trend factors, and confidence scores.
- Visualizes forecasted growth, highlights periods of higher uncertainty, and supports planning for sales, staffing, and inventory.

---

## 🔬 Insights Deep Dive

### **Customer Segmentation**
- **Insight 1:** Monthly subscribers place 2.5x more orders per year than one-time buyers.
- **Insight 2:** Customers aged 25–40 are most likely to refill prescriptions and upgrade to yearly plans.
- **Insight 3:** CA, NY, and TX represent over 50% of total customer base.
- **Insight 4:** Subscription upgrades peak every January and July.

[Customer segmentation visualization]


### **Product Performance**
- **Insight 1:** Minoxidil and Sertraline are top-selling items, with seasonal spikes in spring and fall.
- **Insight 2:** Prescription-required products drive 70% of revenue.
- **Insight 3:** OTC products have lower customer ratings but higher repeat purchase rates.
- **Insight 4:** Manufacturer discounts correlate with order volume surges.

[Product sales visualization]


### **Order Fulfillment & Operations**
- **Insight 1:** Average shipping delay dropped from 12 days (2019) to 6 days (2024).
- **Insight 2:** 8% of orders experience prescription verification delays.
- **Insight 3:** Refills account for 30% of annual order volume.
- **Insight 4:** Most cancellations are concentrated among orders placed on weekends.

[Fulfillment visualization]

### **Revenue Forecasts**
- **Insight 1:** Forecasted revenue shows year-over-year growth, with trend factor indicating periods of accelerated demand.
- **Insight 2:** Confidence scores are highest in months with stable product launches and predictable customer behavior.
- **Insight 3:** Forecasted margin helps identify months with higher profitability and informs inventory planning.
- **Insight 4:** Outlier periods (e.g., new product launches) can be flagged for cautious business decisions using confidence score.

[Revenue forecast visualization]

### **Customer Satisfaction**
- **Insight 1:** 5-star ratings are highest among yearly subscribers.
- **Insight 2:** Lower ratings correlate with shipping delays over 10 days.
- **Insight 3:** N/A doctor names in orders are associated with OTC products and lower ratings.
- **Insight 4:** Customers who give a rating are 40% more likely to place a second order.

[Satisfaction visualization]

---

## 💡 Recommendations

_Based on the findings, I recommend the **operations, marketing, and finance teams** consider:_

- **Optimize shipping workflows,** focusing on high-delay regions (NY, FL, TX).
- **Develop targeted upsell campaigns** for monthly subscribers approaching renewal.
- **Partner with top manufacturers** to secure more product discounts.
- **Improve prescription verification systems** to reduce delays and cancellations.
- **Leverage high-satisfaction customer segments** for referral incentives and testimonials.
- **Use revenue forecast trends and confidence scores** to guide inventory purchases, staffing decisions, and budgeting.

---

## ⚠️ Assumptions and Caveats

- **Assumption 1:** All customer state codes are valid US states.
- **Assumption 2:** Doctor names for prescription orders may be unformatted and require SQL cleaning.
- **Assumption 3:** Some fields (e.g., email, manufacturer) are synthetically generated and not real.
- **Assumption 4:** Data for certain months may be sparser due to simulated business cycles.
- **Assumption 5:** Revenue forecasts are based on historical order data, monthly trend factors, and may have variable confidence scores.

---

**For HR and the team:**  
This project is designed to demonstrate not just technical skills in Python, SQL, and Tableau, but also the ability to translate data into insights and business value. The dashboards provide actionable information for real-world decision-making and team collaboration.