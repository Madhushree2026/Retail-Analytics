
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Retail Sales Analytics",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def load_data():
    data = pd.read_csv("Retail_Sales_Data_Unlox (1).csv")
    data["Date"] = pd.to_datetime(data["Date"])
    return data

df = load_data()

st.title("📊 Retail Analytics & AI-Powered Sales Forecasting")
st.write(
    "Analyze retail revenue, product categories, regional performance "
    "and future sales forecasts."
)

# Sidebar filters
st.sidebar.header("Dashboard Filters")

regions = sorted(df["Region"].dropna().unique())
selected_regions = st.sidebar.multiselect(
    "Select Region",
    regions,
    default=regions
)

categories = sorted(df["Product_Category"].dropna().unique())
selected_categories = st.sidebar.multiselect(
    "Select Product Category",
    categories,
    default=categories
)

filtered_df = df[
    df["Region"].isin(selected_regions)
    & df["Product_Category"].isin(selected_categories)
]

# KPI cards
total_revenue = filtered_df["Revenue"].sum()
total_units = filtered_df["Units_Sold"].sum()
total_stores = filtered_df["Store_ID"].nunique()
average_rating = filtered_df["Store_Rating"].mean()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
c2.metric("Units Sold", f"{total_units:,.0f}")
c3.metric("Stores", f"{total_stores}")
c4.metric("Average Store Rating", f"{average_rating:.2f}/5")

st.divider()

# Monthly revenue chart
st.subheader("Monthly Revenue Trend")

if not filtered_df.empty:
    monthly = (
        filtered_df.set_index("Date")["Revenue"]
        .resample("MS")
        .sum()
        .reset_index()
    )

    fig_monthly = px.line(
        monthly,
        x="Date",
        y="Revenue",
        markers=True,
        title="Monthly Revenue"
    )
    st.plotly_chart(fig_monthly, use_container_width=True)

    # Region and category charts
    left, right = st.columns(2)

    with left:
        st.subheader("Revenue by Region")
        region_data = (
            filtered_df.groupby("Region", as_index=False)["Revenue"]
            .sum()
            .sort_values("Revenue", ascending=False)
        )
        fig_region = px.bar(
            region_data,
            x="Region",
            y="Revenue",
            title="Regional Revenue"
        )
        st.plotly_chart(fig_region, use_container_width=True)

    with right:
        st.subheader("Revenue by Product Category")
        category_data = (
            filtered_df.groupby("Product_Category", as_index=False)["Revenue"]
            .sum()
            .sort_values("Revenue", ascending=False)
        )
        fig_category = px.bar(
            category_data,
            x="Product_Category",
            y="Revenue",
            title="Category Revenue"
        )
        st.plotly_chart(fig_category, use_container_width=True)

    # Store performance
    st.subheader("Store Performance")
    store_data = (
        filtered_df.groupby(
            ["Store_ID", "Store_Location"], as_index=False
        )
        .agg(
            Revenue=("Revenue", "sum"),
            Units_Sold=("Units_Sold", "sum"),
            Average_Rating=("Store_Rating", "mean")
        )
        .sort_values("Revenue", ascending=False)
    )
    st.dataframe(store_data, use_container_width=True)

    # Forecast output
    st.subheader("30-Day Sales Forecast")

    try:
        forecast = pd.read_csv("outputs/next_30_days_forecast.csv")
        forecast["Date"] = pd.to_datetime(forecast["Date"])

        fig_forecast = px.line(
            forecast,
            x="Date",
            y="Predicted_Revenue",
            markers=True,
            title="Predicted Daily Revenue"
        )
        st.plotly_chart(fig_forecast, use_container_width=True)

        st.download_button(
            "Download Forecast CSV",
            data=forecast.to_csv(index=False).encode("utf-8"),
            file_name="next_30_days_forecast.csv",
            mime="text/csv"
        )
    except FileNotFoundError:
        st.info("Run python forecast.py to generate the forecast first.")

    st.subheader("Explore Sales Records")
    st.dataframe(filtered_df.head(100), use_container_width=True)

    st.download_button(
        "Download Filtered Sales Data",
        data=filtered_df.to_csv(index=False).encode("utf-8"),
        file_name="filtered_retail_sales.csv",
        mime="text/csv"
    )
else:
    st.warning("No records match your selected filters.")
