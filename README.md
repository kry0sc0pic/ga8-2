# Customer Engagement Correlation Matrix

This repository contains a Seaborn-based correlation matrix heatmap for customer engagement analytics, created for a major retail client of **Kohler Jenkins**, a data-driven customer experience company.

**Email:** 23f2000764@ds.study.iitm.ac.in  

---

## Business Context

Kohler Jenkins helps businesses understand and optimize their customer relationships through advanced analytics.  
A retail client requested a **publication-ready correlation matrix heatmap** to:

- Understand relationships between key customer engagement metrics
- Support data-driven recommendations in the quarterly business review
- Communicate insights clearly to executives and board members

The visualization focuses on how behavioral, marketing, and value metrics move together, such as:

- Visits, session duration, and pages per session  
- Email open rate and click-through rate  
- Purchase frequency, average order value, and customer lifetime value  
- NPS score as a loyalty / satisfaction signal  

---

## Files

- `chart.py` – Python script that:
  - Generates realistic synthetic customer engagement data
  - Computes a correlation matrix
  - Creates a Seaborn `heatmap` with professional styling
  - Saves the figure as `chart.png` (512x512 pixels)

- `chart.png` – Generated correlation matrix heatmap image.

---

## Requirements

- Python 3.8+
- `pandas`
- `numpy`
- `seaborn`
- `matplotlib`

Install with:

```bash
pip install pandas numpy seaborn matplotlib
