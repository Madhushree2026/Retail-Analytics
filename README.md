# Retail Analytics & AI-Powered Sales Forecasting System

## Project Overview
This project analyzes retail sales data to identify revenue trends, compare regional and product-category performance, evaluate store performance, and forecast future revenue.

## Objectives
- Analyze retail sales and revenue.
- Compare revenue across regions and product categories.
- Evaluate store performance and customer-related metrics.
- Visualize monthly revenue trends.
- Forecast revenue for the next 30 days.
- Provide an interactive dashboard for exploring sales data.

## Dataset
The project uses a retail sales CSV dataset containing dates, store details, product categories, prices, units sold, revenue, discounts, customer types, payment modes, stock levels, ratings, and holiday indicators.

## Technologies Used
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Statsmodels
- Scikit-learn
- Streamlit
- Plotly

## Project Files
- `app.py` — initial data analysis and charts
- `forecast.py` — time-series forecasting and evaluation
- `dashboard.py` — interactive sales analytics dashboard
- `requirements.txt` — required Python libraries
- `charts/` — generated visualizations
- `outputs/` — forecast output files
- `Retail_Sales_Data_Unlox (1).csv` — retail sales dataset

## How to Run

### 1. Install dependencies
```bash
python -m pip install -r requirements.txt
```

### 2. Launch the dashboard
```bash
streamlit run dashboard.py
```

### 3. Open the dashboard
Open the local URL displayed in your terminal, usually `http://localhost:8501`.

## Forecasting
The forecasting script aggregates revenue by date, evaluates a time-series model using a train/test split, and generates a 30-day revenue forecast.

Forecasts are estimates, not actual sales. Model evaluation and limitations should be considered before using predictions for business decisions.

## Dashboard Features
- Revenue and units-sold KPIs
- Monthly revenue trend
- Regional revenue comparison
- Product-category revenue comparison
- Store performance table
- Region and product-category filters
- Forecast visualization and CSV downloads

## Future Improvements
- Compare multiple forecasting models.
- Improve forecast accuracy and validation.
- Add interactive date filters.
- Include inventory and demand-planning insights.
- Deploy the dashboard online.

## Author
Add your name and academic details here before submission.
