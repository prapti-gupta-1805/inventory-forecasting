from fastapi import FastAPI
import pandas as pd
from prophet import Prophet

app = FastAPI()

@app.get("/predict")
def predict_inventory():
    # Sample Sales Data
    data = {
        "ds": ["2024-01-01", "2024-02-01", "2024-03-01", "2024-04-01", "2024-05-01"],
        "y": [120, 150, 170, 200, 250],
    }
    df = pd.DataFrame(data)
    df["ds"] = pd.to_datetime(df["ds"])

    # Train Prophet Model
    model = Prophet()
    model.fit(df)

    # Predict for Next 3 Months
    future = model.make_future_dataframe(periods=3, freq="M")
    forecast = model.predict(future)

    # Convert Forecast to JSON
    return forecast[["ds", "yhat"]].to_dict(orient="records")
