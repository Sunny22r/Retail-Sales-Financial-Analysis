"""Reusable summary analysis for the retail sales demonstration dataset."""
import pandas as pd
from pathlib import Path

DATA = Path(__file__).parent / "data" / "retail_sales.csv"

def main():
    df = pd.read_csv(DATA, parse_dates=["order_date"])
    total_revenue = df["revenue"].sum()
    total_profit = df["profit"].sum()
    total_cost = df["cost"].sum() + df["shipping_cost"].sum()
    print(f"Rows analysed: {len(df):,}")
    print(f"Revenue: ₹{total_revenue:,.2f}")
    print(f"Total costs: ₹{total_cost:,.2f}")
    print(f"Profit: ₹{total_profit:,.2f}")
    print(f"Profit margin: {total_profit / total_revenue * 100:.2f}%")
    print("\nRevenue by category:")
    print(df.groupby("category")["revenue"].sum().sort_values(ascending=False).round(2))
    print("\nProfit by region:")
    print(df.groupby("region")["profit"].sum().sort_values(ascending=False).round(2))

if __name__ == "__main__":
    main()
