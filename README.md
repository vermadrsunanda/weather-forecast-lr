
#  Weather Forecasting using Linear Regression

This project predicts the average temperature for the next 10 years using historical daily/monthly temperature data. It uses Linear Regression and visualizes the forecast using Plotly.

##  Files

- `forecast_temperature.py` – Core Python script
- `sample_temperature_data.csv` – Sample input dataset
- `Weather_Forecast_10_Years.csv` – Output file (generated after running)

## How to Run

1. Install requirements:
   ```
   pip install pandas scikit-learn plotly
   ```

2. Run the script in Python environment:
   ```python
   from forecast_temperature import forecast_temperature
   forecast_temperature("sample_temperature_data.csv")
   ```

## Output

- Forecasted temperature for the next 10 years (CSV)
- Interactive Plotly graph of historical + forecasted trends

## Dataset Format

CSV file must include:
- A date/time column (e.g., `Date`, `Timestamp`)
- A temperature column (e.g., `Temperature`, `Avg Temperature (°C)`)
