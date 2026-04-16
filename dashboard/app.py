import streamlit as st
import pandas as pd

@st.cache_data(show_spinner="Loading sales data…")
def load_data() -> pd.DataFrame:
    df = pd.read_csv("data/sales.csv", low_memory=False)
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
    # Ensure revenue exists (some datasets provide it; others derive it).
    if "revenue" not in df.columns and {"sales", "price"}.issubset(df.columns):
        df["revenue"] = df["sales"] * df["price"]
    return df

df = load_data()

st.title("Retail Sales Analytics Dashboard")

# KPIs
total_revenue = float(df["revenue"].sum()) if "revenue" in df.columns else 0.0
st.metric("Total Revenue", f"${total_revenue:,.2f}")

# Revenue by store
st.subheader("Revenue by Store")
if {"store_id", "revenue"}.issubset(df.columns):
    store_rev = df.groupby("store_id")["revenue"].sum().sort_values(ascending=False)
    st.bar_chart(store_rev)
else:
    st.info("Missing columns for store revenue chart (need `store_id` and `revenue`).")

# Top products
st.subheader("Top Products")
if {"product_id", "revenue"}.issubset(df.columns):
    top_products = (
        df.groupby("product_id")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
    st.write(top_products)
else:
    st.info("Missing columns for top products table (need `product_id` and `revenue`).")