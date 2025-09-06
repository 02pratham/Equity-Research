import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create DataFrame from the provided data
data = [
    {"date": "2023-01-02", "close": 1188.78, "volume": 5316175},
    {"date": "2023-06-01", "close": 1203.45, "volume": 8500000},
    {"date": "2023-12-01", "close": 1298.65, "volume": 12000000},
    {"date": "2024-03-01", "close": 1387.20, "volume": 15000000},
    {"date": "2024-06-01", "close": 1449.80, "volume": 11000000},
    {"date": "2024-09-01", "close": 1521.35, "volume": 9800000},
    {"date": "2024-12-01", "close": 1478.90, "volume": 13500000},
    {"date": "2025-03-01", "close": 1425.60, "volume": 16200000},
    {"date": "2025-06-01", "close": 1398.75, "volume": 14800000},
    {"date": "2025-09-01", "close": 1353.90, "volume": 11232181}
]

df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
df['volume_millions'] = df['volume'] / 1000000  # Convert to millions

# Create subplots
fig = make_subplots(
    rows=2, cols=1,
    row_heights=[0.7, 0.3],
    shared_xaxes=True,
    subplot_titles=('Price Chart', 'Volume'),
    vertical_spacing=0.05
)

# Add price line to top subplot
fig.add_trace(go.Scatter(
    x=df['date'],
    y=df['close'],
    mode='lines',
    name='Close Price',
    line=dict(color='#1FB8CD', width=3),
    hovertemplate='Date: %{x}<br>Price: ₹%{y:.2f}<extra></extra>'
), row=1, col=1)

# Add volume bars to bottom subplot
fig.add_trace(go.Bar(
    x=df['date'],
    y=df['volume_millions'],
    name='Volume',
    marker_color='#DB4545',
    hovertemplate='Date: %{x}<br>Volume: %{y:.1f}M<extra></extra>'
), row=2, col=1)

# Add horizontal lines for key levels to price chart
fig.add_hline(y=1551, line_dash="dash", line_color="#2E8B57", 
              annotation_text="52W High ₹1,551", annotation_position="right",
              row=1, col=1)

fig.add_hline(y=1115, line_dash="dash", line_color="#5D878F",
              annotation_text="52W Low ₹1,115", annotation_position="right",
              row=1, col=1)

fig.add_hline(y=1354, line_dash="dot", line_color="#D2BA4C",
              annotation_text="Current ₹1,354", annotation_position="right",
              row=1, col=1)

# Update layout
fig.update_layout(
    title="Reliance Industries Stock Analysis",
    showlegend=False
)

# Update axes
fig.update_xaxes(title_text="Date", row=2, col=1)
fig.update_yaxes(title_text="Price (₹)", row=1, col=1)
fig.update_yaxes(title_text="Volume (M)", row=2, col=1)

# Apply cliponaxis
fig.update_traces(cliponaxis=False)

# Save the chart
fig.write_image("reliance_stock_chart.png")