## Retail Sales Analytics Dashboard

## Overview
Analyze retail sales data and explore key KPIs in an interactive Streamlit dashboard.

## Features
- Interactive Streamlit dashboard (reads from `data/sales.csv`)
- KPI: total revenue
- Revenue breakdowns (by store) and top products
- Optional ETL helpers in `src/` (transform/load)

## Tech Stack
- Python, Pandas
- Streamlit
- PostgreSQL (optional, only if you use `src/load.py`)

## Business Insights
- Identifies top-performing products
- Highlights which stores generate the most revenue
- Supports data-driven decision making from historical sales



## Dashboard Screenshots
![Dashboard Screenshot 1](assets/picture1.png)
![Dashboard Screenshot 2](assets/picture2.png)


<p align="center">
  <img src="assets/picture1.png" alt="Dashboard Screenshot 1" width="900" />
</p>
<p align="center">
  <img src="assets/picture2.png" alt="Dashboard Screenshot 2" width="900" />
</p>

## Data
The dashboard expects `data/sales.csv` with (at minimum) these columns:
- `product_id`
- `store_id`
- `date`
- `revenue` (or `sales` and `price`, so revenue can be derived)

## Run Locally
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run dashboard/app.py
```

## Run with Docker
```bash
docker build -t retail-sales-dashboard .
docker run --rm -p 8501:8501 retail-sales-dashboard
```