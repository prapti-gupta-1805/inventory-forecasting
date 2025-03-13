# Inventory Forecasting API

## Overview
This project is a **FastAPI-based inventory forecasting system** that uses **Facebook Prophet** to predict future sales trends based on historical data.

## Features
- 📊 **Forecasting with Prophet**: Predicts future sales based on historical trends.
- ⚡ **FastAPI Server**: Provides a `/predict` endpoint for real-time predictions.
- 📈 **Easy Deployment**: Works with minimal setup.

---

## Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/prapti-gupta-1805/inventory-forecasting.git
cd inventory-forecasting
```

### 2️⃣ Install Dependencies
```sh
pip install fastapi uvicorn pandas prophet
```

### 3️⃣ Run the FastAPI Server
```sh
uvicorn main:app --reload
```

### 4️⃣ Access the API
- Open `http://127.0.0.1:8000/docs` in your browser to test the API using **Swagger UI**.
- Or send a request directly:
```sh
curl -X 'GET' 'http://127.0.0.1:8000/predict' -H 'accept: application/json'
```

---

## API Endpoints
### **🔹 GET `/predict`**
**Description:** Predicts inventory sales for the next 3 months.

**Response Example:**
```json
[
    {"ds": "2024-06-01", "yhat": 270.5},
    {"ds": "2024-07-01", "yhat": 300.8},
    {"ds": "2024-08-01", "yhat": 320.2}
]
```

---

## Project Structure
```
📂 inventory-forecasting
├── 📄 main.py          # FastAPI server with prediction endpoint
├── 📄 sample_inventory.csv  # Example dataset for testing
├── 📄 README.md        # Project documentation
```

---

## Future Improvements
🚀 **Enhancements planned:**
- 🛒 Support for multiple products dynamically
- 📈 Better forecasting models with additional features
- 🌎 Deployment on cloud services

---

## Author
👩‍💻 **Prapti Gupta**

For questions, reach out via GitHub Issues! 🚀
