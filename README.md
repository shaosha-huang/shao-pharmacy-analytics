# 📊 Shao's Pharmacy: Data Analytics Project

Welcome to Shao's Pharmacy—a portfolio project demonstrating the full analytics workflow, from synthetic data creation and SQL analysis to actionable Tableau dashboards.

> **Quality over quantity:**  
> Two comprehensive, business-relevant dashboards deliver what matters most.

---

## Project Overview

This project showcases my ability to generate realistic sample data (Python), extract insights (SQL), and build dashboards (Tableau) that drive business value.  
The focus: **three core dashboards** answering key business questions in a clear, actionable format:

- **Business & Financial Performance Dashboard:**  
  Unified view of sales, revenue, costs, forecasts, product performance, and customer trends.

- **Customer Insights & Retention Dashboard:**  
  Segmentation, churn/retention, repeat purchases, subscription lifecycle, and customer journey.

- **Product Supply Dashboard:**  
  Supply chain health, inventory levels, stockouts, supplier performance, and fulfillment metrics.

---

## 🏢 Background

**Industry:** Telemedicine / Online Pharmacy  
**Years:** 2020-2025  
**Business Model:** Direct-to-consumer online medication sales, subscriptions, and recurring orders.  
**Metrics:** Order volume, retention, category sales, fulfillment rates, shipping times, satisfaction, revenue forecasts.

---

## 🗄️ Data Structure

Four main tables power the analysis:
- **customers:** Demographics and subscriptions
- **products:** Catalog, pricing, prescription status
- **orders:** Transactions and fulfillment details
- **forecast:** Monthly revenue forecasts, actuals, projections, margin, trend factor, confidence score

![Entity Relationship Diagram](ERD.png)

---

## 📊 Business & Financial Performance Dashboard: Analysis & Value

### Dashboard Overview

The **Online Orders Performance Scorecard (YTD 2025)** provides a clear, actionable summary of Shao's Pharmacy's financial performance across key product categories: Allergy, Hair, Mental Health, Pain Relief, Skincare, and Sleep.

Each section shows:
- **Revenue to Date** and % of goal/progress
- **Gross Margin Trends** (quarterly)
- **Revenue Actual vs. Forecasted** (quarterly)
- **Contribution to Total Revenue**

---

### Strategic Insights & Business Value

#### 1. **Focus on Top Revenue Drivers**
- **Hair** and **Mental Health** categories contribute over **60% of total revenue** (32.6% Hair, 31.6% Mental Health), making them critical for growth, marketing, and inventory planning.
- High overall progress toward revenue goals (85%+ in all segments; >92% for Mental Health & Sleep) shows strong performance and healthy demand.

#### 2. **Margin Optimization Opportunities**
- **Pain Relief** maintains the highest margins (47%+), but lower revenue share (4.5%). Consider promoting or expanding this category for higher profitability.
- **Mental Health** margins are flat (30%)—review cost structures or pricing to improve profitability where possible.
- **Skincare** margins are lower (34%), but growth trends are positive.

#### 3. **Forecast Accuracy & Sales Planning**
- All categories display **quarterly actual vs. forecasted revenue**, enabling teams to assess sales accuracy, seasonality, and set realistic future targets.
- Most categories are meeting or nearing forecast, signaling reliable business planning and opportunity to further refine projections.

#### 4. **Balanced Portfolio Insights**
- **Allergy**, **Skincare**, and **Sleep** offer diversification—contributing a combined ~30% of revenue.
- **Sleep** category, while smaller in revenue (6.4%), has the highest progress to goal (92.5%), suggesting strong market fit or effective campaigns.

#### 5. **Actionable Next Steps for Teams**
- **Marketing:** Double down on Hair and Mental Health marketing; test new campaigns for Pain Relief and Sleep to boost their share.
- **Product Management:** Prioritize supply and innovation for top categories; investigate ways to improve margins in Mental Health and Skincare.
- **Finance:** Use forecast vs. actual insights for more accurate budgeting and resource allocation.
- **Operations:** Monitor inventory for high-performing segments; prepare for seasonal surges based on quarterly trends.

#### 6. **Visual Storytelling for Stakeholders**
- The dashboard's visual clarity (progress rings, line/bar charts, contribution bar) makes trends and targets instantly understandable—ideal for executive updates, cross-team planning, and investor presentations.

---

**Business & Financial Performance Dashboard**
- Revenue, cost, margin, growth/seasonality
- Forecasts (actual vs projected, confidence, trend)
- Top products/categories, order status, inventory alerts
- Customer trends and segmentation

**Live Tableau Business & Financial Performance Dashboard:**  
[View the interactive scorecard on Tableau Public](https://public.tableau.com/views/ShaosPharmacy-OnlineOrdersPerformanceScorecard/Scorecard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

Or see below:

![Shao’s Pharmacy – Online Orders Performance Scorecard | YTD 2025](Shao’s%20Pharmacy%20–%20Online%20Orders%20Performance%20Scorecard%20%7C%20YTD%202025.png)

---

## 🏆 Customer KPIs: High-Value & At-Risk Segmentation

### **High-Value Customers**
- Top RFM scores: recent, frequent, and high-spending
- Active or upgraded subscriptions
- Frequent buyers of high-margin/prescription products
- Consistent refills, high average order value

### **At-Risk Customers**
- Low RFM scores: no order in >6 months, declining frequency/spend
- Paused, canceled, or downgraded subscriptions
- Complaints, low satisfaction, or multiple cancellations
- Rising churn signals in segment or region

Segmentation is available by product, category, and region—enabling managers to set goals, track trends, and export customer lists for targeted retention or win-back campaigns.

**Sample Tableau Calculations:**

*Declining Order Frequency:*
```tableau
IF SUM([Recent 6 Months Order Count]) < SUM([Previous 6 Months Order Count]) THEN 'Declining' END
```
*Significant Spend Drop:*
```tableau
IF SUM([Recent 6 Months Spend]) < SUM([Previous 6 Months Spend]) * 0.7 THEN 'Significant Drop' END
```

---

## 🏆 Product Supply KPIs & Segmentation

### **Healthy Supply**
- Inventory levels above forecasted demand
- High supplier on-time delivery rate
- Low stockout and cancellation rates

### **At-Risk Supply**
- Inventory below reorder point
- Repeated supplier delays/missed deliveries
- High rate of backorders or supply-related cancellations

Segmentation by product, category, supplier, and region allows managers to monitor, target, and export supply lists for procurement and restocking.

**Sample Tableau Calculations:**

*Low Inventory Alert:*
```tableau
IF [Inventory Level] < [Reorder Point] THEN 'Low Inventory' END
```
*Supplier On-Time Delivery Rate:*
```tableau
SUM([On-Time Deliveries]) / SUM([Total Deliveries])
```
*Fulfillment Rate:*
```tableau
SUM([Orders Shipped On Time]) / SUM([Total Orders])
```
*Stockout Rate:*
```tableau
SUM([Orders Canceled Due to Stockout]) / SUM([Total Orders])
```

---

## 💾 Included Files

- SQL scripts
- CSV datasets
- Python ETL and synthetic data scripts
- ERD diagram
- Tableau workbook

---

**This project demonstrates end-to-end technical and business analytics skills—turning data into actionable insights and real-world value.**