# Airline Passenger Forecasting: A SARIMA Approach

## Executive Summary
This project aims to forecast monthly airline passenger numbers using Time Series Analysis. Moving beyond simplistic trend models, this solution leverages **SARIMA (Seasonal Autoregressive Integrated Moving Average)** to account for complex seasonal patterns and yearly cyclic variations inherent in the aviation industry.

## Key Findings
- **Model Evolution:** The journey began with a baseline ARIMA model, which failed to capture seasonality. Subsequent automated grid searches (Auto-ARIMA) provided a solid blueprint but suffered from overfitting.
- **The Pruning Methodology:** By manually pruning insignificant seasonal autoregressive terms identified during statistical validation, we achieved a mathematically robust model.
- **Performance:** The final SARIMA (0, 1, 1) x (0, 1, 0, 12) model achieved an AIC of 1020.63, significantly outperforming the baseline ARIMA (1353). All model parameters passed the statistical significance tests (P-value < 0.05), ensuring reliable and actionable forecasting.

## Business Impact
The finalized model provides high-precision seasonal forecasts, allowing airlines to optimize resource allocation, manage fleet schedules, and predict passenger demand surges during peak summer and winter seasons.