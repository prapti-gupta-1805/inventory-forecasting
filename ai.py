import pandas as pd
from prophet import Prophet

# Sample Sales Data (Date, Sales)
data = {
    "ds": ["2024-01-01", "2024-02-01", "2024-03-01", "2024-04-01", "2024-05-01"],
    "y": [120, 150, 170, 200, 250],  # Past sales data
}

# Convert to DataFrame
df = pd.DataFrame(data)
df["ds"] = pd.to_datetime(df["ds"])

# Train Prophet Model
model = Prophet()
model.fit(df)

# Predict Future Demand for Next 3 Months
future = model.make_future_dataframe(periods=3, freq="M")
forecast = model.predict(future)

# Print Forecast
print(forecast[["ds", "yhat"]])  # yhat = predicted demand