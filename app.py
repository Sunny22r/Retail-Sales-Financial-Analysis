import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Retail Sales & Financial Analysis", page_icon="📊", layout="wide")
st.title("📊 Retail Sales & Financial Performance Dashboard")
st.caption("MBA Business Analytics Project | Demonstration dataset (synthetic data)")

@st.cache_data
def load_data():
    path = Path(__file__).parent / "data" / "retail_sales.csv"
    data = pd.read_csv(path, parse_dates=["order_date"])
    data["month"] = data["order_date"].dt.to_period("M").astype(str)
    data["profit_margin_pct"] = (data["profit"] / data["revenue"].replace(0, pd.NA) * 100).fillna(0)
    return data

df = load_data()
st.sidebar.header("Filter the analysis")
regions = st.sidebar.multiselect("Region", sorted(df["region"].unique()), default=sorted(df["region"].unique()))
categories = st.sidebar.multiselect("Product category", sorted(df["category"].unique()), default=sorted(df["category"].unique()))
channels = st.sidebar.multiselect("Sales channel", sorted(df["sales_channel"].unique()), default=sorted(df["sales_channel"].unique()))
date_min, date_max = df["order_date"].min().date(), df["order_date"].max().date()
date_range = st.sidebar.date_input("Order date range", value=(date_min, date_max), min_value=date_min, max_value=date_max)

filtered = df[df["region"].isin(regions) & df["category"].isin(categories) & df["sales_channel"].isin(channels)].copy()
if isinstance(date_range, tuple) and len(date_range) == 2:
    filtered = filtered[(filtered["order_date"].dt.date >= date_range[0]) & (filtered["order_date"].dt.date <= date_range[1])]

if filtered.empty:
    st.warning("No records match the selected filters.")
    st.stop()

revenue = filtered["revenue"].sum()
profit = filtered["profit"].sum()
cost = filtered["cost"].sum() + filtered["shipping_cost"].sum()
margin = (profit / revenue * 100) if revenue else 0
orders = filtered["order_id"].nunique()

c1,c2,c3,c4 = st.columns(4)
c1.metric("Total Revenue", f"₹{revenue:,.0f}")
c2.metric("Total Profit", f"₹{profit:,.0f}")
c3.metric("Profit Margin", f"{margin:.1f}%")
c4.metric("Orders", f"{orders:,}")

st.divider()
left, right = st.columns(2)
with left:
    monthly = filtered.groupby("month", as_index=False)[["revenue","profit"]].sum()
    monthly_long = monthly.melt("month", var_name="Metric", value_name="Amount")
    st.subheader("Monthly revenue and profit")
    st.plotly_chart(px.line(monthly_long, x="month", y="Amount", color="Metric", markers=True), use_container_width=True)
with right:
    category = filtered.groupby("category", as_index=False)[["revenue","profit"]].sum().sort_values("revenue", ascending=False)
    st.subheader("Performance by product category")
    st.plotly_chart(px.bar(category, x="category", y="revenue", color="profit", color_continuous_scale="Blues"), use_container_width=True)

left, right = st.columns(2)
with left:
    region = filtered.groupby("region", as_index=False)[["revenue","profit"]].sum().sort_values("revenue", ascending=False)
    st.subheader("Regional sales performance")
    st.plotly_chart(px.bar(region, x="region", y="revenue", color="profit", color_continuous_scale="Teal"), use_container_width=True)
with right:
    channel = filtered.groupby("sales_channel", as_index=False)[["revenue","profit"]].sum()
    st.subheader("Online vs store channel")
    st.plotly_chart(px.pie(channel, names="sales_channel", values="revenue", hole=.45), use_container_width=True)

st.subheader("Key business insights")
best_cat = category.iloc[0]["category"]
best_region = region.iloc[0]["region"]
best_channel = channel.sort_values("revenue", ascending=False).iloc[0]["sales_channel"]
st.write(f"- Highest-revenue category in the selected data: **{best_cat}**.")
st.write(f"- Highest-revenue region in the selected data: **{best_region}**.")
st.write(f"- Leading sales channel by revenue: **{best_channel}**.")
st.write(f"- Overall profit margin for the selected data: **{margin:.1f}%**.")
st.caption("These insights are calculated from the selected filters. They are not claims about a real retailer.")

st.subheader("Filtered transaction data")
st.dataframe(filtered.drop(columns=["month","profit_margin_pct"]), use_container_width=True, hide_index=True)
st.download_button("Download filtered data as CSV", filtered.to_csv(index=False).encode("utf-8"), "filtered_retail_sales.csv", "text/csv")
