# Aadhaar Demographic Intelligence  
*UIDAI Data Hackathon 2026 Project*

This project builds an end-to-end data intelligence pipeline on UIDAI Aadhaar demographic datasets to extract population structure insights across Indian states.

It transforms raw government data into:

- Cleaned and standardized datasets  
- State-wise demographic summaries  
- Child vs Adult population ratios  
- Top & Bottom ranked states  
- Analytical visualizations  
- An interactive dashboard  

The goal is to convert raw Aadhaar data into **policy-ready demographic intelligence**.

---

## Project Pipeline

The project is structured as a reproducible data pipeline:

| File | Purpose |
|------|---------|
| `clean.py` | Cleans and standardizes raw UIDAI CSV files |
| `merge.py` | Merges all cleaned CSVs into one dataset |
| `rank.py` | Computes demographic ratios and rankings |
| `visual.py` | Generates analytical graphs |
| `dashboard.py` | Interactive Streamlit dashboard |

Generated outputs:

- `state_demographic_summary.csv`  
- `state_child_top10.csv`  
- `state_adult_top10.csv`  
- `state_child_bottom10.csv`  
- `state_adult_bottom10.csv`  

---

## Key Insights Produced

- National Child vs Adult composition  
- State-wise demographic structure  
- Top 10 Child-Dominant States  
- Top 10 Adult-Dominant States  
- Bottom 10 Child-Ratio States  
- Bottom 10 Adult-Ratio States  
- Child population trend over time  

These outputs help identify:

- Youth-heavy regions for education planning  
- Adult-heavy states for workforce policy  
- Regional demographic imbalance  

---

## Data Source

This project uses publicly available UIDAI Aadhaar demographic datasets.

From:  
https://www.data.gov.in/

Files used:

- `api_data_aadhar_demographic_0_500000.csv`  
- `api_data_aadhar_demographic_500000_1000000.csv`  
- `api_data_aadhar_demographic_1000000_1500000.csv`  
- `api_data_aadhar_demographic_1500000_2000000.csv`  
- `api_data_aadhar_demographic_2000000_2071700.csv`  
