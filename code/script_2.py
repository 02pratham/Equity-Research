# Download balance sheet data
balance_csv_url = "https://perplexity.ai/rest/finance/financials/RELIANCE.NS/csv?period=annual&statement_category=BALANCE_SHEET"
response = requests.get(balance_csv_url)
balance_data = pd.read_csv(pd.io.common.StringIO(response.text))

print("Balance Sheet Data Shape:", balance_data.shape)
print("\nColumns:", balance_data.columns.tolist())

# Display key balance sheet metrics for recent years
print("\n=== KEY BALANCE SHEET METRICS (Recent Years) ===")
balance_data['totalAssets_billions'] = balance_data['totalAssets'] / 1e9
balance_data['totalEquity_billions'] = balance_data['totalStockholdersEquity'] / 1e9
balance_data['totalDebt_billions'] = balance_data['totalDebt'] / 1e9

recent_years_bs = balance_data[balance_data['calendarYear'] >= 2020].sort_values('calendarYear')
for _, row in recent_years_bs.iterrows():
    print(f"\nYear {int(row['calendarYear'])}:")
    print(f"  Total Assets: ₹{row['totalAssets_billions']:.1f} billion")
    print(f"  Total Equity: ₹{row['totalEquity_billions']:.1f} billion")
    print(f"  Total Debt: ₹{row['totalDebt_billions']:.1f} billion")
    if row['totalEquity_billions'] > 0:
        print(f"  Debt-to-Equity: {row['totalDebt_billions']/row['totalEquity_billions']:.2f}")
    if row['totalAssets_billions'] > 0:
        print(f"  Return on Assets: {(income_data[income_data['calendarYear']==row['calendarYear']]['netIncome'].iloc[0] / row['totalAssets']) * 100:.1f}%")