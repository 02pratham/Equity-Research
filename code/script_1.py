# Download the financial statements data
import requests
import pandas as pd

# Download income statement data
income_csv_url = "https://perplexity.ai/rest/finance/financials/RELIANCE.NS/csv?period=annual&statement_category=INCOME_STATEMENT"
response = requests.get(income_csv_url)
income_data = pd.read_csv(pd.io.common.StringIO(response.text))

print("Income Statement Data Shape:", income_data.shape)
print("\nColumns:", income_data.columns.tolist())
print("\nData range:")
print(income_data[['date', 'calendarYear', 'revenue', 'netIncome', 'eps']].head(10))

# Clean and process data
income_data['revenue_billions'] = income_data['revenue'] / 1e9
income_data['netIncome_billions'] = income_data['netIncome'] / 1e9

# Display key financial metrics for recent years
print("\n=== KEY FINANCIAL METRICS (Recent Years) ===")
recent_years = income_data[income_data['calendarYear'] >= 2020].sort_values('calendarYear')
for _, row in recent_years.iterrows():
    print(f"\nYear {int(row['calendarYear'])}:")
    print(f"  Revenue: ₹{row['revenue_billions']:.1f} billion")
    print(f"  Net Income: ₹{row['netIncome_billions']:.1f} billion")
    print(f"  EPS: ₹{row['eps']:.2f}")
    print(f"  Gross Profit Margin: {row['grossProfitRatio']*100:.1f}%")
    print(f"  Operating Margin: {row['operatingIncomeRatio']*100:.1f}%")
    print(f"  Net Margin: {row['netIncomeRatio']*100:.1f}%")