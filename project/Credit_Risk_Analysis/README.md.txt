#  Credit Risk & Defaulter Analysis (Barclays Scenario)

##  Project Overview
The objective of this project is to analyze a bank's loan dataset to identify high-risk demographic segments and the root causes driving loan defaults. The goal is to optimize lending policies, reduce Non-Performing Assets (NPAs), and design better risk-based pricing models.

##  Tech Stack
* **Database & EDA:** SQLite, Python (Pandas)
* **Data Visualization & Analytics:** Power BI

##  Key Business Insights
1. **The Demographic Vulnerability:** The default crisis is heavily concentrated in the younger population. 'Youth (18-25)' and 'Young Adults (26-35)' account for almost the entirety of the defaulted amount.
2. **High-Risk Intents:** Loans disbursed for **Medical** and **Debt Consolidation** represent the highest risk categories.
3. **The Income-Interest Squeeze:** While average interest rates remain relatively flat across age groups (~11%), the 'Youth' segment defaults heavily because their significantly lower average income (~$59K vs ~$101K for Seniors) makes standard EMI structures unsustainable.

##  Strategic Recommendations
* **LTV & Collateral Optimization:** Enforce stricter Loan-To-Value (LTV) ratios or mandate secured collateral for Youth/Young Adults applying for Medical/Debt loans.
* **Income-Adjusted Amortization:** Restructure the repayment schedule for lower-income brackets to recover the principal amount faster in the initial months, rather than applying flat interest rates.
* **Risk-Based Pricing Adjustments:** Shift from purely risk-based penalty pricing (which forces low-income defaults) to customized, sustainable EMI plans.

##  Dashboard Preview
![Credit Risk Dashboard](credit_risk.png)