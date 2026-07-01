# 📊 Telecom Customer Churn Analytics: End-to-End EDA & Power BI Dashboard

###  Business Objective
The goal of this project is to analyze a dataset of 7,000+ telecom customers, identify the root causes behind a critical **26.5% churn rate** (resulting in $2.86M revenue leakage), and build an interactive Executive Dashboard to propose data-driven retention strategies.

### 🛠️ Tech Stack & Pipeline
* **Backend & EDA:** Python (Pandas, Matplotlib) via Jupyter Notebook.
* **Data Engineering:** Data Cleaning (Implicit Nulls in `TotalCharges`), Feature Engineering (Creating categorical `Tenure_Group` bins from continuous data).
* **Frontend & Visualization:** Power BI (Interactive Dashboards, DAX, Cross-filtering).

### Key Business Insights
1. **The Contract Trap:** Customers on 'Month-to-Month' contracts are highly volatile, accounting for the vast majority of the churn (88.5% of total churned users).
2. **The Premium Product Gap:** Fiber Optic is the premium internet service, but users who bought it *without* Tech Support have a massive ~49% churn rate. With Tech Support, this drops significantly to ~15%.
3. **The Tenure Danger Zone:** The highest attrition occurs in the very first year (0-1 Year). The company is losing its premium-paying customers extremely early in their lifecycle.

### Actionable Recommendations
* **Incentivize Long-Term Contracts:** Offer a one-time discount or OTT bundle to Month-to-month customers if they upgrade to a 1-year contract.
* **Bundle Tech Support:** Make basic Tech Support completely FREE or mandatory for the first 6 months for all Fiber Optic customers to reduce frustration.
* **Revamp Onboarding:** Create a proactive '90-Day Retention Program' for new customers, including feedback calls and issue-resolution check-ins.

### The Executive Dashboard
*(Note: I have uploaded the `.pbix` file in the repository. Below is a snapshot of the final interactive dashboard)*

![Power BI Dashboard](dashboard.png)