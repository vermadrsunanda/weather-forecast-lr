
# 📌 Step 1: Install Required Libraries
# Run these in your environment:
# pip install pandas scikit-learn plotly

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go

# 📌 Step 2: Load CSV File
def forecast_temperature(file_path):
    df = pd.read_csv(file_path)

    # Auto-detect date and temperature columns
    date_col = next((col for col in df.columns if 'date' in col.lower() or 'time' in col.lower()), None)
    temp_col = next((col for col in df.columns if 'temperature' in col.lower()), None)

    if not date_col or not temp_col:
        raise ValueError("Missing 'date' or 'temperature' column.")

    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df['Year'] = df[date_col].dt.year
    df = df.dropna(subset=['Year', temp_col])
    df[temp_col] = pd.to_numeric(df[temp_col], errors='coerce')
    df = df.dropna(subset=[temp_col])

    # Yearly average
    df_yearly = df.groupby('Year')[temp_col].mean().reset_index()
    df_yearly.columns = ['Year', 'Avg Temperature (°C)']

    # Train model
    X = df_yearly['Year'].values.reshape(-1, 1)
    y = df_yearly['Avg Temperature (°C)'].values
    model = LinearRegression().fit(X, y)

    # Forecast
    future_years = np.arange(df_yearly['Year'].max() + 1, df_yearly['Year'].max() + 11).reshape(-1, 1)
    predictions = model.predict(future_years)
    df_forecast = pd.DataFrame({'Year': future_years.flatten(), 'Avg Temperature (°C)': predictions})

    # Combine and save
    df_combined = pd.concat([df_yearly, df_forecast], ignore_index=True)
    df_combined.to_csv("Weather_Forecast_10_Years.csv", index=False)

    # Plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_yearly['Year'], y=df_yearly['Avg Temperature (°C)'], mode='lines+markers', name='Historical'))
    fig.add_trace(go.Scatter(x=df_forecast['Year'], y=df_forecast['Avg Temperature (°C)'], mode='lines+markers', name='Forecast', line=dict(dash='dash')))
    fig.update_layout(title="🌤️ Weather Forecast (Next 10 Years)", xaxis_title="Year", yaxis_title="Avg Temperature (°C)", template="plotly_white")
    fig.show()

# 📌 Example Usage
# forecast_temperature("sample_temperature_data.csv")
