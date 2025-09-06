import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the data from CSV
try:
    df = pd.read_csv("ril_segment_breakdown.csv")
    print("Data loaded from CSV:")
    print(df.head())
    print("\nColumn names:")
    print(df.columns.tolist())
    
    # Use the Revenue_Share_Percent column for accurate percentages
    segment_col = 'Segment'
    value_col = 'Revenue_Share_Percent'
    
except Exception as e:
    print(f"Error loading CSV: {e}")
    # If CSV not available, use the provided data
    data = {
        'Segment': ['Oil to Chemicals', 'Retail', 'Digital Services', 'Oil & Gas', 'Others'],
        'Revenue_Share_Percent': [53.12, 26.68, 11.05, 2.38, 6.77]
    }
    df = pd.DataFrame(data)
    segment_col = 'Segment'
    value_col = 'Revenue_Share_Percent'
    print("Using provided data:")
    print(df)

print(f"\nUsing segment column: {segment_col}")
print(f"Using value column: {value_col}")
print(f"\nData values:")
for i, row in df.iterrows():
    print(f"{row[segment_col]}: {row[value_col]}%")

# Define brand colors in the specified order
colors = ['#1FB8CD', '#DB4545', '#2E8B57', '#5D878F', '#D2BA4C']

# Create pie chart using the percentage column for accurate values
fig = go.Figure(data=[go.Pie(
    labels=df[segment_col], 
    values=df[value_col],
    textinfo='label+percent',
    textposition='inside',
    marker=dict(colors=colors),
    hovertemplate='<b>%{label}</b><br>%{percent}<br><extra></extra>'
)])

# Update layout with title and styling
fig.update_layout(
    title="RIL Business Segment Revenue (FY25)",
    uniformtext_minsize=14, 
    uniformtext_mode='hide'
)

# Save the chart
fig.write_image("ril_segment_breakdown_pie.png")
print("Chart saved as ril_segment_breakdown_pie.png")