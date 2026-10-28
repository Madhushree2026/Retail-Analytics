
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import os

# Load the retail sales dataset
df = pd.read_csv("Retail_Sales_Data_Unlox (1).csv")
df["Date"] = pd.to_datetime(df["Date"])

# Aggregate revenue by day
daily_revenue = (
    df.groupby("Date")["Revenue"]
    .sum()
    .sort_index()
    .asfreq("D", fill_value=0)
)

# Split the data: train on earlier dates, test on later dates
split_point = int(len(daily_revenue) * 0.8)
train = daily_revenue.iloc[:split_point]
test = daily_revenue.iloc[split_point:]

# Fit the forecasting model
model = ExponentialSmoothing(
    train,
    trend="add",
    seasonal=None,
    initialization_method="estimated"
)

fitted_model = model.fit(optimized=True)

# Forecast the test period
test_predictions = fitted_model.forecast(len(test))

# Calculate evaluation metrics
mae = (test - test_predictions).abs().mean()
rmse = (((test - test_predictions) ** 2).mean()) ** 0.5

print("=" * 50)
print("RETAIL SALES FORECASTING")
print("=" * 50)
print("Training days:", len(train))
print("Testing days:", len(test))
print("Mean Absolute Error (MAE):", round(mae, 2))
print("Root Mean Squared Error (RMSE):", round(rmse, 2))

# Refit on all historical data for future forecasting
final_model = ExponentialSmoothing(
    daily_revenue,
    trend="add",
    seasonal=None,
    initialization_method="estimated"
).fit(optimized=True)

future_forecast = final_model.forecast(30)

forecast_df = pd.DataFrame({
    "Date": future_forecast.index,
    "Predicted_Revenue": future_forecast.values
})

os.makedirs("outputs", exist_ok=True)
forecast_df.to_csv("outputs/next_30_days_forecast.csv", index=False)

# Plot actual and predicted revenue
plt.figure(figsize=(12, 5))
plt.plot(test.index, test.values, label="Actual Revenue")
plt.plot(
    test_predictions.index,
    test_predictions.values,
    label="Forecast Revenue"
)
plt.title("Sales Forecast Model Evaluation")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.legend()
plt.tight_layout()
plt.savefig("charts/forecast_evaluation.png", dpi=150)
plt.close()

print("\nNext 30-day forecast saved to outputs/next_30_days_forecast.csv")
print("Evaluation chart saved to charts/forecast_evaluation.png")
print("\nFirst 5 forecast values:")
print(forecast_df.head().round(2).to_string(index=False))
