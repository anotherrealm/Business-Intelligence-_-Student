# Business Intelligence Report: Superstore Profitability Analysis

**Team:** Superstore BI Group (Squad C)
**Date:** November 23, 2025
**Framework:** EPIC (Engage, Propose, Illustrate, Close)

---

## Executive Summary 
Despite strong nationwide sales, Superstore is experiencing declining profitability. A detailed BI analysis using the Superstore dataset revealed three major drivers of financial loss:
1. Persistent losses in the **Furniture** category—especially Tables.
2. Excessive **discounting above 20%**.
3. High-cost operations in the **Central Region**, with Texas alone accounting for –$26,000 in losses.

Addressing these issues can immediately improve the contribution margin and potentially recover more than **$70,000** in annual profit.

---

## Methodology 
Our team used Python (Pandas, Matplotlib, Seaborn) to clean and analyze the dataset.

* **Preprocessing:** Key steps included removing duplicates, converting date fields, engineering new metrics (`Delivery_Days`, `Unit_Cost`), and exporting a cleaned dataset.
* **Scope:** Visual analysis focused on five dimensions: sales trends, logistics performance, product profitability, discount dynamics, and regional performance.

---

## Key Findings 

### 1. Product-Level Profitability
* The **Technology** category performs strongly, but **Furniture** consistently loses money.
* **Tables** are the single worst-performing sub-category, generating an estimated **–$17,000** total loss.
* Price vs. Quantity analysis shows low demand for high-cost furniture items, amplifying losses.

### 2. Discount Impact on Profit
Discount analysis reveals a clear threshold:
* **0%–20% discount:** Generally profitable.
* **>20% discount:** Almost always unprofitable.
* **Insight:** Some transactions include discounts as high as 60%–80% on high-value items, directly destroying margins. This aligns with the scatter visualization showing a steep profit decline as discounts rise.

### 3. Regional Performance
* State-level profit mapping shows uneven performance across the U.S.
* The **Central Region** is the poorest performing, with **Texas** generating **–$26,000** in net loss.
* Likely contributors include higher shipping costs, longer delivery times, and deeper discounting than other regions.

### 4. Logistics and Shipping Insights
* **Standard Class** shipping—though the most frequently used—also shows the longest delivery times.
* Extended delivery durations may impact cost structure and customer satisfaction, especially for large furniture items.

### 5. Trend Insights
* Sales peak in **Q4 (Nov–Dec)**, but profit does not increase proportionally. This suggests that seasonal holiday discounting is reducing margins despite the volume spike.

---

## Recommendations 

### 1. Implement a Discount Cap Policy
* **Action:** Set an automated discount ceiling of **20%**, especially for Furniture.
* **Impact:** Discounts above this threshold should require managerial approval. This change directly addresses the largest cause of negative profit.

### 2. Restructure Operations in the Central Region
* **Action:** Pause aggressive promotions in **Texas and Ohio** until shipping contracts are renegotiated or pricing is adjusted.
* **Impact:** Targeted interventions here can recover more than one-third of the company’s total losses.

### 3. Revise Pricing Strategy for Tables
* **Action:** Increase Table prices by **10%** to offset shipping and delivery costs.
* **Impact:** If certain models remain unprofitable after the adjustment, discontinue them from the catalog.

---

## Conclusion
The Superstore BI analysis reveals clear, data-driven actions that can immediately improve profitability. By enforcing a disciplined discount policy, restructuring loss-making states, and fixing the pricing strategy for Tables, the company can transition from high-volume/low-margin operations to a more sustainable and profitable retail model.
