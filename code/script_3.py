# Create financial analysis datasets for Reliance Industries
import pandas as pd
import numpy as np

# Financial metrics data for charts
years = ['2021', '2022', '2023', '2024', '2025']
revenue_data = [4669.2, 6959.6, 8778.4, 9010.6, 9646.9]  # in billions INR
net_income_data = [491.3, 607.0, 667.0, 696.2, 696.5]  # in billions INR
eps_data = [38.19, 46.00, 49.30, 51.45, 51.47]

# Create comprehensive financial performance dataset
financial_df = pd.DataFrame({
    'Year': years,
    'Revenue_Billions_INR': revenue_data,
    'Net_Income_Billions_INR': net_income_data,
    'EPS_INR': eps_data
})

print("Financial Performance Dataset:")
print(financial_df)

# Business segment data for FY25 (from search results)
segments = ['Oil to Chemicals', 'Retail', 'Digital Services', 'Oil & Gas', 'Others']
segment_revenue_share = [53.12, 26.68, 11.05, 2.38, 6.77]  # % of total revenue
segment_revenue_values = [626921, 330943, 154119, 25211, 84170]  # in crores

segment_df = pd.DataFrame({
    'Segment': segments,
    'Revenue_Share_Percent': segment_revenue_share,
    'Revenue_Crores': segment_revenue_values
})

print("\nBusiness Segment Breakdown FY25:")
print(segment_df)

# Key valuation metrics
current_price = 1353.90
market_cap_trillions = 18.36
pe_ratio = 22.53
pb_ratio = 1.86
dividend_yield = 0.41
book_value = 623.09
debt_to_equity = 0.44

valuation_metrics = pd.DataFrame({
    'Metric': ['Current Price (INR)', 'Market Cap (₹ Trillion)', 'P/E Ratio', 'P/B Ratio', 
               'Dividend Yield (%)', 'Book Value (INR)', 'Debt-to-Equity'],
    'Value': [current_price, market_cap_trillions, pe_ratio, pb_ratio, 
              dividend_yield, book_value, debt_to_equity]
})

print("\nKey Valuation Metrics:")
print(valuation_metrics)

# Stock performance data (YTD and historical)
performance_periods = ['1 Day', '1 Week', '1 Month', '3 Months', '6 Months', '1 Year', '5 Year CAGR']
performance_returns = [-0.29, -3.69, -4.23, -4.27, 13.09, -10.76, 28.27]

performance_df = pd.DataFrame({
    'Period': performance_periods,
    'Returns_Percent': performance_returns
})

print("\nStock Performance Returns:")
print(performance_df)

# Export all datasets as CSV for chart creation
financial_df.to_csv('ril_financial_performance.csv', index=False)
segment_df.to_csv('ril_segment_breakdown.csv', index=False) 
valuation_metrics.to_csv('ril_valuation_metrics.csv', index=False)
performance_df.to_csv('ril_stock_performance.csv', index=False)

print("\nDatasets created and saved as CSV files for visualization.")